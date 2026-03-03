# LAB-Bench

[![OpenReward Environment](https://img.shields.io/badge/%E2%AD%90%20OpenReward-Environment-f7e6cc)](https://openreward.ai/EnvCommons/LAB-Bench) [![Hugging Face Dataset](https://img.shields.io/badge/Hugging%20Face-Dataset-orange)](https://huggingface.co/datasets/futurehouse/lab-bench)

## Description

LAB-Bench (Language Agent Biology Benchmark) is an environment for evaluating language agents on practical scientific research tasks. It contains over 2,400 multiple-choice questions across 8 sub-environments designed to assess capabilities including literature search, protocol planning, data analysis, figure interpretation, database navigation, and sequence manipulation. Unlike traditional science benchmarks focused on textbook knowledge, LAB-Bench measures performance on real-world research tasks that would make an AI system useful as a scientific assistant.

## Capabilities

- Scientific literature retrieval and RAG
- Supplementary material interpretation
- Scientific figure and table comprehension
- Biological database query and navigation
- Protocol analysis and troubleshooting
- DNA/RNA sequence analysis and manipulation
- Molecular cloning workflow planning

## Compute Requirements

Agents are given a standard environment with no sandbox or file system access.

## License

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Tasks

LAB-Bench contains 8 sub-environments:

| Sub-Environment | Description |
|----------------|-------------|
| **LitQA2** | Scientific literature RAG questions |
| **SuppQA** | Supplementary material interpretation |
| **FigQA** | Scientific figure comprehension |
| **TableQA** | Scientific table interpretation |
| **DbQA** | Biological database queries (10 subtasks) |
| **ProtocolQA** | Protocol analysis and troubleshooting |
| **SeqQA** | Sequence analysis (15 subtasks) |
| **CloningScenarios** | Molecular cloning workflows |

Each sub-environment has a **test** split.

## Reward Structure

This is a single-turn environment. The agent submits an answer via the `answer` tool. An LLM grader evaluates correctness against the reference answer. Reward is binary: 1.0 if correct, 0.0 if incorrect.

## Data

Data consists of JSONL files sourced from [HuggingFace futurehouse/lab-bench](https://huggingface.co/datasets/futurehouse/lab-bench). Each task includes a multiple-choice question with randomized options. Data is stored on the OpenReward platform.

## Tools

| Tool | Description |
|------|-------------|
| `answer` | Submit your multiple-choice answer (A, B, C, or D). Ends the episode. |

## Time Horizon

Single-turn. The agent reads the scientific question and submits one answer.

## Environment Difficulty

LAB-Bench evaluates practical scientific research capabilities with tasks designed to require real scientific knowledge. Results from the original paper:

| Sub-Environment | Human | Claude-3.5-Sonnet | GPT-4o |
|-----------------|-------|-------------------|--------|
| LitQA2 (Precision) | 73.8% | 37.7% | 44.6% |
| SuppQA | 86% | 75% | 47% |
| FigQA | 82% | 54% | 30% |
| TableQA | 87% | 90% | 75% |
| ProtocolQA | 87% | 66% | 56% |
| CloningScenarios | 73% | 54% | 37% |

## Other Environment Requirements

OpenAI API key required for LLM-based grading. Pass via `secrets={"openai_api_key": "..."}`.

## Safety

Agents in LAB-Bench answer scientific research questions in a standard environment. The environment does not present direct safety risks.

## Citation

```bibtex
@article{laurent2024lab,
  title={LAB-Bench: Measuring Capabilities of Language Models for Biology Research},
  author={Laurent, Jon M. and Janizek, Joseph D. and Ruzo, Michael and Hinks, Michaela M. and Hammerling, Michael J. and Narayanan, Siddharth and Ponnapati, Manvitha and White, Andrew D. and Rodriques, Samuel G.},
  journal={arXiv preprint arXiv:2407.10362},
  year={2024}
}
```
