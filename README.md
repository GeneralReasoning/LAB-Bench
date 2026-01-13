GR TODO:
- `get_table` often leads to the error "Error executing action 'get_table': sent 1009 (message too big) frame exceeds limit of 1048576 bytes; no close frame received"

# LAB-Bench

LAB-Bench is a benchmark for evaluating language agents on practical scientific research tasks. The benchmark consists of over 2,400 multiple-choice questions designed to assess capabilities including literature search, protocol planning, data analysis, figure interpretation, database navigation, and sequence manipulation. Unlike traditional science benchmarks focused on textbook knowledge, LAB-Bench aims to measure performance on real-world research tasks that would make an AI system useful as a scientific assistant. The benchmark is based on the paper "Language Agent Biology Benchmark: Evaluating AI Systems on Practical Scientific Research Tasks" and is available at https://huggingface.co/datasets/futurehouse/lab-bench.

## LitQA2

LitQA2 is a benchmark for evaluating scientific RAG (Retrieval-Augmented Generation) systems. The benchmark consists of 248 multiple-choice questions with 100% human coverage.

### Overview

LitQA2 measures a system's ability to retrieve information from scientific literature. The questions are designed to:

- Have unambiguous answers
- Be attested to only once in scientific literature
- Not be answerable from abstracts alone
- Require access to highly esoteric findings from recent scientific papers
- Not be answerable through training data recall
- Require literature access and reasoning capabilities

### Key Features

- Multiple-choice format
- 248 questions total
- 100% human coverage
- Focus on scientific RAG capabilities
- Questions derived from recent scientific papers
- Requires literature access and reasoning

### Leaderboard

| Model                              | Precision (%) |
|------------------------------------|--------------:|
| PaperQA2                           |          85.2 |
| Human (baseline)                   |          73.8 |
| Perplexity Pro                     |          69.7 |
| Gemini-Pro-1.5                     |          51.7 |
| GPT-4o                             |          44.6 |
| GPT-4-Turbo                        |          43.6 |
| Elicit                             |          40.9 |
| Claude-Sonnet-3.5                  |          37.7 |
| Claude-Opus                        |          23.6 |

## SuppQA

SuppQA is a benchmark for evaluating AI systems on their ability to find and interpret information in scientific paper supplements. The benchmark consists of multiple-choice questions that require accessing and understanding information contained in supplemental materials.

### Overview

The questions are designed to test practical knowledge of scientific supplements through scenarios that:

- Require accessing specific supplemental materials
- Cannot be answered using abstracts or main paper text
- Focus on information in supplemental text and tables
- Provide paper title and DOI but not specific supplement details
- Benefit from effective retrieval tool usage

### Key Features

- Multiple-choice format
- Focus on supplemental material interpretation
- Questions based on real scientific papers
- Requires effective information retrieval
- Tests ability to navigate scientific supplements

### Leaderboard

| Model                          | SuppQA |
|--------------------------------|-------:|
| **Human**                      |   0.86 |
| **claude-3-5-sonnet-20240620** |   0.75 |
| **claude-3-opus-20240229**     |   0.59 |
| **gemini-1.5-pro-001**         |   0.32 |
| **gpt-4o**                     |   0.47 |
| **gpt-4-turbo**                |   0.39 |
| **claude-3-haiku-20240307**    |   0.35 |
| **Meta-Llama-3-7B-Instruct**   |   0.27 |

## FigQA

FigQA is a benchmark for evaluating AI systems on their ability to comprehend and reason about scientific figures. The benchmark consists of multiple-choice questions that require analyzing and interpreting information from scientific figures without any additional context.

### Overview

The questions are designed to test visual comprehension and reasoning through scenarios that:

- Present only the figure image without captions or paper text
- Require integration of information from multiple elements
- Test multi-hop reasoning similar to text-based benchmarks
- Focus on scientific figure interpretation
- Require multi-modal capabilities

### Key Features

- Multiple-choice format
- Visual-only questions (no text context)
- Multi-hop reasoning requirements
- Scientific figure interpretation
- Multi-modal capabilities needed

### Leaderboard

| Model                          | FigQA |
|--------------------------------|------:|
| **Human**                      | 0.82  |
| **claude-3-5-sonnet-20240620** | 0.54  |
| **claude-3-opus-20240229**     | 0.31  |
| **gemini-1.5-pro-001**         | 0.34  |
| **gpt-4o**                     | 0.30  |
| **gpt-4-turbo**                | 0.28  |
| **claude-3-haiku-20240307**    | 0.24  |
| **Meta-Llama-3-7B-Instruct**   | 0.00  |

## TableQA

TableQA is a benchmark for evaluating AI systems on their ability to interpret and reason about data in scientific tables. The benchmark consists of multiple-choice questions that require analyzing and interpreting information from scientific tables without any additional context.

### Overview

The questions are designed to test data interpretation and reasoning through scenarios that:

- Present only the table image without captions or paper text
- Require both simple lookup and complex reasoning
- Test ability to perform operations on tabular data
- Focus on scientific table interpretation
- Require multi-modal capabilities

### Key Features

- Multiple-choice format
- Visual-only questions (no text context)
- Data lookup and reasoning requirements
- Scientific table interpretation
- Multi-modal capabilities needed

### Leaderboard

| Model                          | TableQA |
|--------------------------------|--------:|
| **Human**                      |    0.87 |
| **claude-3-5-sonnet-20240620** |    0.90 |
| **claude-3-opus-20240229**     |    0.74 |
| **gemini-1.5-pro-001**         |    0.71 |
| **gpt-4o**                     |    0.75 |
| **gpt-4-turbo**                |    0.58 |
| **claude-3-haiku-20240307**    |    0.51 |
| **Meta-Llama-3-7B-Instruct**   |    0.00 |


## DbQA

DbQA is a benchmark for evaluating AI systems on database query tasks in biology research. The benchmark consists of multiple-choice questions that require accessing and retrieving information from specific biological databases.

### Overview

The questions are designed to test practical knowledge of biological databases through scenarios that:

- Require accessing specific biological databases
- Test information retrieval capabilities
- Cover diverse biological domains
- Focus on database-specific knowledge
- Require accurate data attribution

### Key Features

- Multiple-choice format
- Database-specific questions
- Diverse biological domains
- Information retrieval focus
- Data attribution requirements

### Leaderboard

| Model                          | DbQA_dga_task-v1 | DbQA_gene_location_task-v1 | DbQA_mirna_targets_task-v1 | DbQA_mouse_tumor_gene_sets-v1 | DbQA_oncogenic_signatures_task-v1 | DbQA_tfbs_GTRD_task-v1 | DbQA_variant_from_sequence_task-v1 | DbQA_variant_multi_sequence_task-v1 | DbQA_vax_response_task-v1 | DbQA_viral_ppi_task-v1 |
|--------------------------------|-----------------:|---------------------------:|---------------------------:|-------------------------------:|-----------------------------------:|-----------------------:|------------------------------------:|-------------------------------------:|--------------------------:|-----------------------:|
| **Human**                      | 0.71             | 0.93                       | 1.00                       | 1.00                           | 1.00                               | 1.00                   | 0.75                                | 0.38                                 | 1.00                      | 0.90                   |
| **claude-3-5-sonnet-20240620** | 0.00             | 0.00                       | 0.00                       | 0.73                           | 0.59                               | 0.00                   | 0.75                                | 0.16                                 | 0.57                      | 0.00                   |
| **claude-3-opus-20240229**     | 0.00             | 0.00                       | 0.00                       | 0.71                           | 0.57                               | 0.00                   | 0.11                                | 0.18                                 | 0.65                      | 0.00                   |
| **gemini-1.5-pro-001**         | 0.00             | 0.22                       | 0.00                       | 0.76                           | 0.75                               | 0.00                   | 0.17                                | 0.33                                 | 0.61                      | 0.00                   |
| **gpt-4o**                     | 0.17             | 0.38                       | 0.30                       | 0.59                           | 0.32                               | 0.33                   | 0.44                                | 0.12                                 | 0.45                      | 0.69                   |
| **gpt-4-turbo**                | 0.17             | 0.22                       | 0.03                       | 0.58                           | 0.61                               | 0.00                   | 0.00                                | 0.00                                 | 0.65                      | 0.28                   |
| **claude-3-haiku-20240307**    | 0.17             | 0.22                       | 0.26                       | 0.55                           | 0.30                               | 0.31                   | 0.36                                | 0.16                                 | 0.38                      | 0.49                   |
| **Meta-Llama-3-7B-Instruct**   | 0.25             | 0.21                       | 0.29                       | 0.58                           | 0.47                               | 0.19                   | 0.35                                | 0.12                                 | 0.54                      | 0.40                   |

DbQA questions are intended to require the access and retrieval of information from specific common databases used in biology research. In contrast to related prior benchmarks that aimed to assess the general biological factuality of LLM generations, our DbQA questions focus on the ability to return information attributable to specific databases. DbQA questions were designed to cover a wide array of data sources, such that a model or agent would not be able to answer them all with the use of a single API.

## ProtocolQA

ProtocolQA is a benchmark for evaluating AI systems on protocol analysis and troubleshooting tasks. The benchmark consists of multiple-choice questions based on modified scientific protocols that require understanding of:

- Protocol design and execution
- Error identification and correction
- Step sequence and dependencies
- Experimental outcomes
- Troubleshooting strategies

### Overview

The questions are designed to test practical knowledge of scientific protocols through scenarios that:

- Present modified or incomplete protocols
- Describe unexpected experimental outcomes
- Require error identification
- Need protocol correction
- Test troubleshooting abilities

### Key Features

- Multiple-choice format
- Real-world protocol scenarios
- Error identification focus
- Protocol correction requirements
- Outcome-based questions

### Leaderboard

| Model                          | ProtocolQA |
|--------------------------------|-----------:|
| **Human**                      |       0.87 |
| **gemini 2.5 pro**             |       0.74 |
| **claude-3-5-sonnet-20240620** |       0.66 |
| **claude-3-opus-20240229**     |       0.62 |
| **gemini-1.5-pro-001**         |       0.58 |
| **gpt-4o**                     |       0.56 |
| **gpt-4-turbo**                |       0.59 |
| **claude-3-haiku-20240307**    |       0.51 |
| **Meta-Llama-3-7B-Instruct**   |       0.49 |

ProtocolQA questions are crafted from published protocols that have been manipulated to introduce errors either by modification or omission of steps. Questions then present hypothetical outcomes of the modified protocol, and ask what step(s) might need to be modified or added to "fix" the protocol to produce the intended output.

## SeqQA

SeqQA is a benchmark for evaluating AI systems on sequence analysis and manipulation tasks. The benchmark consists of multiple-choice questions across 15 subtasks that test understanding of:

- DNA/RNA sequence properties
- PCR primer design and analysis
- Restriction enzyme analysis
- Open reading frame (ORF) analysis
- Sequence translation and effects
- GC content analysis

### Overview

The questions are designed to test practical knowledge of sequence analysis through scenarios that:

- Analyze sequence properties
- Design and evaluate PCR primers
- Predict restriction digest outcomes
- Identify and analyze ORFs
- Calculate sequence characteristics
- Test sequence manipulation abilities

### Key Features

- Multiple-choice format
- 15 specialized subtasks
- Real-world sequence analysis scenarios
- Tool-dependent questions
- Sequence manipulation focus

### Leaderboard

| Model                          | SeqQA_ORF-seq-AAid-v1 | SeqQA_ORF-seq-Aseq-v1 | SeqQA_ORF-seq-numlen-v1 | SeqQA_ORF-transeff-v1 | SeqQA_PCR-gene-enzprimers-v1 | SeqQA_PCR-gene-gibshindprimers-v1 | SeqQA_PCR-gene-gibssmaprimers-v1 | SeqQA_PCR-geneprimers-enz-v1 | SeqQA_PCR-len-primers-v1 | SeqQA_PCR-primers-len-v1 | SeqQA_PCR-seq-enzprimers-v1 | SeqQA_PCR-seq-primers-v1 | SeqQA_Prop-seq-gcpercent-v1 | SeqQA_RE-seq-lenfrags-v1 | SeqQA_RE-seq-numfrags-v1 |
|--------------------------------|-----------------------:|----------------------:|-------------------------:|-----------------------:|------------------------------:|---------------------------------:|--------------------------------:|-----------------------------:|--------------------------:|--------------------------:|------------------------------:|---------------------------:|----------------------------:|---------------------------:|---------------------------:|
| **Human**                      | 0.91                   | 0.88                  | 0.43                     | 0.75                   | 0.88                          | 0.79                             | 0.78                          | 0.98                         | 0.90                      | 0.90                      | 0.83                          | 1.00                       | 1.00                        | 0.86                       | 0.74                       |
| **claude-3-5-sonnet-20240620** | 0.13                   | 0.89                  | 0.00                     | 0.92                   | 0.78                          | 0.71                             | 0.70                          | 0.91                         | 0.29                      | 0.37                      | 0.95                          | 0.98                       | 0.59                        | 0.33                       | 0.28                       |
| **claude-3-opus-20240229**     | 0.13                   | 0.70                  | 0.28                     | 0.71                   | 0.87                          | 0.75                             | 0.40                          | 0.84                         | 0.45                      | 0.38                      | 0.83                          | 0.91                       | 0.50                        | 0.26                       | 0.18                       |
| **gemini-1.5-pro-001**         | 0.09                   | 0.26                  | 0.18                     | 0.67                   | 0.80                          | 0.71                             | 0.54                          | 0.69                         | 0.07                      | 0.19                      | 0.73                          | 0.64                       | 0.41                        | 0.17                       | 0.22                       |
| **gpt-4o**                     | 0.23                   | 0.50                  | 0.14                     | 0.66                   | 0.64                          | 0.75                             | 0.47                          | 0.77                         | 0.14                      | 0.15                      | 0.86                          | 0.76                       | 0.32                        | 0.25                       | 0.11                       |
| **gpt-4-turbo**                | 0.15                   | 0.50                  | 0.27                     | 0.49                   | 0.60                          | 0.67                             | 0.72                          | 0.75                         | 0.13                      | 0.26                      | 0.78                          | 0.56                       | 0.23                        | 0.27                       | 0.22                       |
| **claude-3-haiku-20240307**    | 0.19                   | 0.57                  | 0.26                     | 0.52                   | 0.61                          | 0.57                             | 0.51                          | 0.83                         | 0.14                      | 0.26                      | 0.86                          | 0.82                       | 0.40                        | 0.22                       | 0.12                       |
| **Meta-Llama-3-7B-Instruct**   | 0.19                   | 0.49                  | 0.29                     | 0.46                   | 0.58                          | 0.45                             | 0.58                          | 0.39                         | 0.06                      | 0.22                      | 0.73                          | 0.47                       | 0.36                        | 0.19                       | 0.16                       |

SeqQA questions are designed to test a model's ability to analyze and manipulate biological sequences, with a focus on practical tasks common in molecular biology workflows. The benchmark includes tasks that require understanding of sequence properties, PCR primer design, restriction enzyme analysis, and ORF analysis. Each subtask focuses on a specific aspect of sequence analysis, allowing for detailed evaluation of a model's capabilities in different areas of sequence manipulation and analysis.


## CloningScenarios

CloningScenarios is a benchmark for evaluating AI systems on complex molecular cloning tasks. The benchmark consists of multiple-choice questions based on real-world cloning scenarios that require understanding of:

- Plasmid design and manipulation
- DNA fragment assembly
- Multi-step cloning workflows
- Tool selection and usage
- Protocol planning

### Overview

The questions are designed to test practical knowledge of molecular cloning through scenarios that:

- Involve multiple plasmids and DNA fragments
- Require multi-step workflows
- Need tool selection and usage
- Test protocol planning abilities
- Are based on real-world cloning scenarios

### Key Features

- Multiple-choice format
- Real-world cloning scenarios
- Complex multi-step workflows
- Tool-dependent questions
- Related question groups testing different aspects of the same scenario

### Leaderboard

| Model                          | CloningScenarios |
|--------------------------------|-----------------:|
| **Human**                      | 0.73             |
| **claude-3-5-sonnet-20240620** | 0.54             |
| **gemini 2.5 pro**             | 0.53             |
| **claude-3-opus-20240229**     | 0.41             |
| **gemini-1.5-pro-001**         | 0.33             |
| **gpt-4o**                     | 0.37             |
| **gpt-4-turbo**                | 0.36             |
| **claude-3-haiku-20240307**    | 0.29             |
| **Meta-Llama-3-7B-Instruct**   | 0.34             |
