import json
import os
from typing import Any

import pytest
from utils import get_path_to_data_dir
from protocolqa import ProtocolQA, AnswerInput, examples as protocolqa_examples
from seqqa import SeqQA, examples as seqqa_examples
from tableqa import TableQA, examples as tableqa_examples
from suppqa import SuppQA, examples as suppqa_examples
from cloningscenarios import CloningScenarios, examples as cloningscenarios_examples
from figqa import FigQA, examples as figqa_examples
from dbqa import DBQA, examples as dbqa_examples
from litqa2 import LitQA2, examples as litqa2_examples


CHECK_N = 10 # because grader evaluations are expensive
DATA_DIR = get_path_to_data_dir()


# =====PROTOCOLQA=====
all_data = []
with open(DATA_DIR / "protocolqa" / "protocolqa-v1-public.jsonl", "r") as f:
    for line in f:
        all_data.append(json.loads(line.strip()))
all_data = all_data[:CHECK_N]
protocolqa_examples = protocolqa_examples[:CHECK_N]
assert len(all_data) == len(protocolqa_examples)

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(protocolqa_examples, all_data))
async def test_protocolqa_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = ProtocolQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']

    line_split = task['question'].split("\n")
    right_line = [i for i in line_split if data['ideal'] in i][0]
    correct_letter = right_line.split(")")[1].strip()

    result = await env.answer(AnswerInput(answer=correct_letter))
    assert result.reward == 1.0


@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(protocolqa_examples, all_data))
async def test_protocolqa_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = ProtocolQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']

    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0


# =====SEQQA=====
all_data = []
for file_name in [
    "ORF-seq-numlen-v1-public.jsonl",
    "ORF-transeff-v1-public.jsonl", 
    "PCR-gene-enzprimers-v1-public.jsonl",
    "PCR-gene-gibshindprimers-v1-public.jsonl",
    "PCR-gene-gibssmaprimers-v1-public.jsonl",
    "PCR-geneprimers-enz-v1-public.jsonl",
    "PCR-len-primers-v1-public.jsonl",
    "PCR-primers-len-v1-public.jsonl",
    "PCR-seq-enzprimers-v1-public.jsonl",
    "PCR-seq-primers-v1-public.jsonl",
    "Prop-seq-gcpercent-v1-public.jsonl",
    "RE-seq-lenfrags-v1-public.jsonl",
    "RE-seq-numfrags-v1-public.jsonl",
    "ORF-seq-AAid-v1-public.jsonl",
    "ORF-seq-AAseq-v1-public.jsonl"
]:
    with open(DATA_DIR / "seqqa" / file_name, "r") as f:
        for line in f:
            all_data.append(json.loads(line.strip()))
seqqa_examples = seqqa_examples[:CHECK_N]
all_data = all_data[:CHECK_N]
assert len(all_data) == len(seqqa_examples)

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(seqqa_examples, all_data))
async def test_seqqa_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = SeqQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']

    result = await env.answer(AnswerInput(answer=data['ideal']))
    assert result.reward == 1.0


@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(seqqa_examples, all_data))
async def test_seqqa_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = SeqQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']

    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0


# =====TABLEQA=====
tableqa_data = []
with open(DATA_DIR / "tableqa" / "tableqa-v1-public.jsonl", "r") as f:
    for line in f:
        tableqa_data.append(json.loads(line.strip()))

assert len(tableqa_data) == len(tableqa_examples)
tableqa_examples = tableqa_examples[:CHECK_N]
tableqa_data = tableqa_data[:CHECK_N]

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(tableqa_examples, tableqa_data))
async def test_tableqa_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = TableQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer=data['ideal']))
    assert result.reward == 1.0

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(tableqa_examples, tableqa_data))
async def test_tableqa_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = TableQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0


# =====SUPPQA=====
suppqa_data = []
with open(DATA_DIR / "suppqa" / "suppqa-v1-public.jsonl", "r") as f:
    for line in f:
        suppqa_data.append(json.loads(line.strip()))

assert len(suppqa_data) == len(suppqa_examples)
suppqa_examples = suppqa_examples[:CHECK_N]
suppqa_data = suppqa_data[:CHECK_N]

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(suppqa_examples, suppqa_data))
async def test_suppqa_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = SuppQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer=data['ideal']))
    assert result.reward == 1.0

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(suppqa_examples, suppqa_data))
async def test_suppqa_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = SuppQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0


# =====CLONING SCENARIOS=====
cloningscenarios_data = []
with open(DATA_DIR / "cloningscenarios" / "cloningscenarios-v1-public.jsonl", "r") as f:
    for line in f:
        cloningscenarios_data.append(json.loads(line.strip()))

assert len(cloningscenarios_data) == len(cloningscenarios_examples)
cloningscenarios_examples = cloningscenarios_examples[:CHECK_N]
cloningscenarios_data = cloningscenarios_data[:CHECK_N]

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(cloningscenarios_examples, cloningscenarios_data))
async def test_cloningscenarios_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = CloningScenarios(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer=data['ideal']))
    assert result.reward == 1.0

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(cloningscenarios_examples, cloningscenarios_data))
async def test_cloningscenarios_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = CloningScenarios(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0


# =====FIGQA=====
figqa_data = []
with open(DATA_DIR / "figqa" / "figqa-v1-public.jsonl", "r") as f:
    for line in f:
        figqa_data.append(json.loads(line.strip()))

assert len(figqa_data) == len(figqa_examples)
figqa_examples = figqa_examples[:CHECK_N]
figqa_data = figqa_data[:CHECK_N]

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(figqa_examples, figqa_data))
async def test_figqa_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = FigQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer=data['ideal']))
    assert result.reward == 1.0

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(figqa_examples, figqa_data))
async def test_figqa_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = FigQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0


# =====DBQA=====
dbqa_data = []
for file_name in [
    "dga_task-v1-public.jsonl",
    "gene_location_task-v1-public.jsonl", 
    "mirna_targets_task-v1-public.jsonl",
    "mouse_tumor_gene_sets-v1-public.jsonl",
    "oncogenic_signatures_task-v1-public.jsonl",
    "tfbs_GTRD_task-v1-public.jsonl",
    "variant_from_sequence_task-v1-public.jsonl",
    "variant_multi_sequence_task-v1-public.jsonl",
    "vax_response_task-v1-public.jsonl",
    "viral_ppi_task-v1-public.jsonl"
]:
    with open(DATA_DIR / "dbqa" / file_name, "r") as f:
        for line in f:
            dbqa_data.append(json.loads(line.strip()))

assert len(dbqa_data) == len(dbqa_examples)
dbqa_examples = dbqa_examples[:CHECK_N]
dbqa_data = dbqa_data[:CHECK_N]

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(dbqa_examples, dbqa_data))
async def test_dbqa_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = DBQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer=data['ideal']))
    assert result.reward == 1.0

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(dbqa_examples, dbqa_data))
async def test_dbqa_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = DBQA(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    assert task['id'].split("_")[-1] == data['id']
    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0


# =====LITQA2=====
litqa2_data = []
with open(DATA_DIR / "litqa2" / "litqa-v2-public.jsonl", "r") as f:
    for line in f:
        litqa2_data.append(json.loads(line.strip()))

assert len(litqa2_data) == len(litqa2_examples)
litqa2_examples = litqa2_examples[:CHECK_N]
litqa2_data = litqa2_data[:CHECK_N]

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(litqa2_examples, litqa2_data))
async def test_litqa2_golden_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = LitQA2(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    result = await env.answer(AnswerInput(answer=data['ideal']))
    assert result.reward == 1.0

@pytest.mark.asyncio
@pytest.mark.parametrize("task_and_data", zip(litqa2_examples, litqa2_data))
async def test_litqa2_xfail_grading(task_and_data: tuple[dict[str, Any], dict[str, Any]]):
    task, data = task_and_data
    env = LitQA2(task_spec=task, secrets={"openai_api_key": os.getenv("OPENAI_API_KEY")})
    result = await env.answer(AnswerInput(answer="covfefe"))
    assert result.reward == 0.0
