import json
import random
from typing import Awaitable, List

import openai
from pydantic import BaseModel

from openreward.environments import Environment, JSONObject, ToolOutput, tool, TextBlock

from utils import get_path_to_data_dir

DATA_DIR = get_path_to_data_dir()
GRADER_TEMPLATE = """Your job is to identify whether the model response is correct given the correct answer. Do a brief paragraph of analysis, then answer "CORRECT" or "INCORRECT".

Question: {question}
Reference Answer: {correct_answer}
Predicted Answer: {predicted_answer}
"""

def format_question(question: str, paper: str, source: str, ideal: str, distractors: list[str], task_id: str) -> tuple[str, str]:
    """Format a question with randomized multiple choice options"""
    # Create randomized options with fixed seed for reproducibility
    random.seed(hash(task_id))
    options = [ideal] + distractors
    random.shuffle(options)
    
    # Find correct letter
    correct_letter = chr(65 + options.index(ideal))
    

    formatted_question = f"Paper: {paper}\n\nSource: {source}\n\n"

    # Create formatted question
    formatted_question += f"{question}\n\n"
    for i, option in enumerate(options):
        letter = chr(65 + i)  # A, B, C, D
        formatted_question += f"{letter}) {option}\n"
    
    return formatted_question, correct_letter

# Load data from suppqa task file
all_data = []
task_file = "suppqa-v1-public.jsonl"

try:
    with open(DATA_DIR / task_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            all_data.append({
                "id": data["id"],
                "question": data["question"],
                "ideal": data["ideal"],
                "distractors": data["distractors"],
                "paper_title": data["paper-title"],
                "source": data["source"],
            })
except FileNotFoundError:
    print(f"Warning: Could not find {task_file}")

# Create examples with formatted questions for get_tasks
examples = []
full_examples = {}
for data in all_data:
    formatted_q, correct_letter = format_question(
        data["question"], 
        data["paper_title"],
        data["source"],
        data["ideal"], 
        data["distractors"], 
        data["id"]
    )

    full_examples[data["id"]] = {
        "id": data["id"],
        "answer": correct_letter,
        "question": formatted_q,
        "paper_title": data["paper_title"],
        "source": data["source"]
    }

    examples.append({
        "id": data["id"],
        "question": formatted_q,
        "paper_title": data["paper_title"],
        "source": data["source"]
    })

AVAILABLE_SPLITS = ["test"]

class TaskSpec(BaseModel):
    id: str
    question: str
    paper_title: str
    source: str

class AnswerInput(BaseModel, extra="forbid"):
    answer: str

class SuppQA(Environment):
    def __init__(self, task_spec: JSONObject, secrets: dict[str, str] = {}) -> None:
        super().__init__(task_spec)
        self.validated = TaskSpec.model_validate(task_spec)

        # Validate required API key
        api_key = secrets.get("openai_api_key")
        if not api_key:
            raise ValueError("OpenAI API key must be provided via secrets parameter")

        self.client = openai.AsyncClient(api_key=api_key)
        self.correct_letter = full_examples[self.validated.id]['answer']

    async def _grade_sample(self, predicted_answer: str) -> dict:
        grader_prompt = GRADER_TEMPLATE.format(
            question=self.validated.question,
            correct_answer=self.correct_letter,
            predicted_answer=predicted_answer,
        )

        res = await self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                { "role": "user", "content": grader_prompt }
            ],
            temperature=0,
            stream=False
        )
        
        grading_response = res.choices[0].message.content or ""
        is_correct = "CORRECT" in grading_response and 'INCORRECT' not in grading_response
        
        return {
            "is_correct": is_correct
        }

    @tool
    async def answer(self, params: AnswerInput) -> ToolOutput:
        grader_output = await self._grade_sample(params.answer)
        reward = 1.0 if grader_output["is_correct"] else 0.0
        return ToolOutput(
            metadata=grader_output,
            blocks=[TextBlock(text=f"Answer graded. Reward: {reward:.2f}")],
            reward=reward,
            finished=True
        )

    async def get_prompt(self) -> List[TextBlock]:
        return [TextBlock(text=self.validated.question)]

    @classmethod
    def list_tasks(cls, split: str) -> list[JSONObject]:
        if split != "test":
            raise ValueError(f"Unknown split: {split}")
        return examples  # type: ignore[return-value]

    @classmethod
    def list_splits(cls) -> list[str]:
        return AVAILABLE_SPLITS.copy()
