# 📧 Email Compliance System (Agentic AI-Powered, Mistral-7B)

A modular, production-grade AI system that monitors and enforces email compliance policies using Large Language Models (LLMs), vector search, and agentic AI architecture. This system utilizes the Mistral-7B model for classification and explanation of email violations.

---

## 🧠 Key Features

- 📥 Intelligent Email Ingestion – Parses email body, subject, sender, and recipient.
- 🧹 Preprocessing Agent – Cleans content, removes signatures, and quoted replies.
- 📛 Policy Violation Classification – Uses `Mistral-7B-Instruct` for zero/few-shot email violation classification.
- 📄 Policy Retrieval – Embeds your policy docs and retrieves them using Weaviate (vector DB).
- 🧾 Explanation Agent – Uses Mistral to explain *why* an email violates a policy with reasoning.
- 📊 Metrics Logging – Tracks violation trends using InfluxDB + Grafana.
- 📣 Alert Agent – Sends notifications (email, Slack, webhook) for high-risk incidents.
- 🔌 Plug & Play Modular Design – Each agent runs independently.

---

## 📁 Project Structure

```
email_compliance_project/
├── main.py
├── config.py
├── agents/
│   ├── ingest_agent.py
│   ├── preprocess_agent.py
│   ├── classify_agent.py
│   ├── explain_agent.py
│   ├── retrieve_agent.py
│   ├── summary_agent.py
│   ├── metrics_agent.py
│   └── notify_agent.py
└── utils/
    └── email_utils.py
```

---

## 🔧 Installation & Setup

### 1. Clone Repo
```bash
git clone https://github.com/your-org/email_compliance_project.git
cd email_compliance_project
```

### 2. Create Environment
```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a `.env` file with:
```
WEAVIATE_URL=https://your-weaviate-url
WEAVIATE_API_KEY=your-key
MISTRAL_MODEL_PATH=path/to/mistral-7b-instruct
GRAFANA_ENDPOINT=your-grafana-url
```

---

## 🧠 Model Setup: Mistral-7B-Instruct

Download or load Mistral-7B using Hugging Face:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", torch_dtype=torch.float16, device_map="auto")
```

---

## ⚙️ How It Works

1. `ingest_agent.py`: Parses and structures incoming emails.
2. `preprocess_agent.py`: Strips replies, greetings, signatures.
3. `classify_agent.py`: Classifies emails (e.g., Confidentiality Breach, Harassment, etc.) using Mistral.
4. `retrieve_agent.py`: Finds matching policy using Weaviate similarity search.
5. `explain_agent.py`: Explains the classification rationale.
6. `summary_agent.py`: Summarizes violations for reporting.
7. `metrics_agent.py`: Pushes metadata to InfluxDB (Grafana).
8. `notify_agent.py`: Triggers alerts for risky messages.

---

## 🖼 Example Violation Output

```json
{
  "email_subject": "Leaked Salary Sheet",
  "violation_type": "Confidentiality Breach",
  "explanation": "The email includes employee salary details and is shared with external recipients, violating HR Policy Section 4.3.",
  "matched_policy": "HR Policy 4.3 – Salary Confidentiality",
  "severity": "High"
}
```

---

## 📊 Grafana Dashboard

Tracks:
- Violation counts by day
- Top senders with violations
- Policy sections most violated
- Severity distribution

---

## 🛡 Security Considerations

- All embeddings are stored locally or in encrypted cloud DBs.
- The personally Identifiable Information (PII) redaction is supported.
- Logs do not store the full email body by default (configurable).
- The original code wasn't disclosed due to organizational privacy issues. 
---
