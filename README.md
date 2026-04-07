---
title: Support Triage Environment
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 🤖 Support Triage Environment

## 🚀 Overview
The **Support Triage Environment** simulates a real-world customer support system where an AI agent must intelligently decide how to respond to incoming user issues.

The agent must classify each scenario into one of four actions:
- 🛠️ **assist** — provide direct help  
- ❓ **clarify** — request more information  
- 🚨 **escalate** — forward critical issues  
- 👀 **monitor** — track low-priority issues  

This environment evaluates:
- Decision-making accuracy  
- Handling ambiguity  
- Prioritization under uncertainty  

---

## 🌍 Real-World Motivation
Customer support teams constantly triage issues based on urgency, clarity, and business impact.

This environment replicates that workflow in a structured, testable format for AI agents.

> ⚠️ **Note:** Scenarios are synthetically generated based on real-world customer support patterns.

---

## 🧠 Problem Design

### 🔹 Action Space
| Action     | Description |
|------------|------------|
| assist     | Provide direct resolution |
| clarify    | Ask for missing details |
| escalate   | Handle critical/high-risk issues |
| monitor    | Observe low-priority situations |

---

### 🔹 Observation Space
Each step returns:

```json
{
  "scenario": "User issue description",
  "step": 0
}
```

---

## 🎯 Task Difficulty Levels

| Level  | Description | Example |
|--------|------------|--------|
| Easy   | Clear, direct issues | OTP not received → assist |
| Medium | Ambiguous scenarios | Requires reasoning |
| Hard   | Critical / edge cases | May require escalation |

---

## 🏆 Reward System

| Outcome   | Reward |
|----------|--------|
| Correct   | +1.0 |
| Partial   | +0.25 |
| Incorrect | -1.0 |

### 📈 Difficulty Scaling
- Medium → ×1.1  
- Hard → ×1.2  

✔ Continuous reward feedback ensures stable evaluation.

---

## ⚙️ Environment Design
- 🎲 Random scenario generation  
- ⏱️ Fixed episode length  
- 📏 Deterministic grading  
- 🔌 Fully OpenEnv compatible  

---

## 🤖 Inference Pipeline

Baseline agent:
- Uses an OpenAI-compatible client  
- Reads environment variables  

### Output Format
```
[START]
[STEP]
[END]
```

---

## 🛠️ Setup Guide

### ▶️ Run Locally
```bash
docker build -t support-triage-env .
docker run support-triage-env
```

---

## ☁️ Deployment
- Hosted on Hugging Face Spaces  
- Docker-based execution  
- OpenEnv compatible  

---

## 📊 Baseline Performance
- Moderate performance across tasks  
- Higher variance on medium and hard scenarios  
- Reflects realistic ambiguity challenges  

---

## ✨ Key Features
- 🧩 Real-world decision simulation  
- 📊 Multi-level difficulty  
- 🎯 Deterministic evaluation  
- 📈 Continuous reward scoring  
- ⚡ Lightweight and fast  

---

## 🧪 Example Scenario

**Input:**
```
User: "My payment was deducted but order not confirmed"
```

**Expected Action:**
```
escalate
```

---

## 🏁 Conclusion
This environment provides a **practical and scalable benchmark** for evaluating AI agents in customer support triage tasks.

It bridges the gap between:
- Academic RL environments  
- Real-world decision-making systems  
