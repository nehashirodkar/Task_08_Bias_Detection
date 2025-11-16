# Task 08 – Bias Detection in LLM Data Narratives  
Syracuse University | MSIS Research Requirement  

This repository contains my implementation of **Task 08: Bias Detection in LLM Data Narratives**, where the objective is to test whether large language models (LLMs) produce biased interpretations when given *minimally varied prompts* on the same dataset.

The project evaluates framing bias, demographic bias, confirmation bias, and selection bias using a **synthetic sports performance dataset** and prompt-pair experiments.

---


No real individuals or PII were used.

---

## 🧪 Hypotheses Tested

1. **Framing Bias (H1)**  
   Positive framing (growth potential) vs negative framing (underperformance) will change model recommendations.

2. **Demographic Bias (H2)**  
   Mentioning class year (senior/junior/sophomore) changes which player the LLM selects.

3. **Confirmation Bias (H3)**  
   If primed with a claim, the LLM will tend to agree even when unsupported.

4. **Selection Bias (H4)**  
   LLMs may emphasize high-impact stats (goals) and ignore others (turnovers).

---

## ⚙️ Scripts Overview

### `experiment_design.py`  
Generates all prompt files programmatically.

### `run_experiment.py`  
Runs each prompt 3× through one or more LLMs and logs outputs.

### `analyze_bias.py`  
Performs basic sentiment analysis and creates summary plots.

### `validate_claims.py`  
Checks whether model responses contradict the dataset.

---

## ▶️ How to Reproduce

### 1. Install dependencies  
```bash
pip install -r requirements.txt


