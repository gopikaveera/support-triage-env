# Support Triage Environment

## Overview

The Support Triage Environment simulates a real-world customer support workflow in which an AI agent must determine the most appropriate action for incoming user issues.

At each step, the agent analyzes a scenario and selects one of the following actions:

* assist — provide direct help for resolvable issues
* clarify — request additional information when the issue is ambiguous
* escalate — forward critical or system-level issues
* monitor — track low-priority or intermittent issues

This environment evaluates decision-making under uncertainty, prioritization, and the ability to handle real-world ambiguity.

---

## Real-World Motivation

Customer support systems must triage large volumes of user issues efficiently. Decisions depend on:

* urgency and impact
* clarity of the request
* risk (financial, security, or system-wide)
* user sentiment

This environment models those dynamics to provide a meaningful benchmark for evaluating intelligent agents.

Scenarios are synthetically generated based on real-world customer support patterns.

---

## Action Space

The agent selects one of four discrete actions:

* assist — resolve the issue directly
* clarify — gather missing or unclear information
* escalate — handle high-risk or critical issues
* monitor — observe non-critical or intermittent issues

---

## Observation Space

Each step returns a structured observation:

```json
{
  "scenario": "User issue description",
  "step": 0,
  "history": [],
  "progress": "Step 0 of N"
}
```

* scenario: the current user issue
* step: current step index
* history: list of past actions
* progress: human-readable step tracking

---

## Task Design

The environment includes three levels of difficulty:

### Easy

* Clearly defined issues
* Direct mapping to a single action

Example: OTP not received → assist

---

### Medium

* Partially ambiguous scenarios
* Requires interpretation and decision-making

Example: vague error message → clarify

---

### Hard

* Critical, high-impact, or sensitive issues
* Requires prioritization and multi-step reasoning

Example: system outage or security concern → escalate

---

## Multi-Step Behavior

* Easy and medium tasks may complete quickly
* Hard tasks require at least two steps before completion
* Encourages realistic workflows such as:

  * clarify → assist
  * detect severity → escalate

---

## Reward Design

The environment provides a shaped reward signal:

* Base reward is computed using a deterministic grader
* Additional shaping includes:

  * bonus for correct action on the first step
  * penalty for repeating the same action
* Rewards are constrained to the range (0.01, 0.99)

This design encourages:

* efficient decision-making
* non-repetitive behavior
* correct prioritization across steps

---

## Environment Design

* Randomized scenario selection
* Multi-step interaction support
* Action history tracking
* Difficulty-aware termination logic
* Deterministic grading for reproducibility

---

## OpenEnv Compliance

The environment adheres to the OpenEnv specification:

* Implements reset(), step(), and state()
* Uses structured observation, action, and reward formats
* Includes deterministic grading logic
* Provides openenv.yaml metadata
* Validated using OpenEnv validation tools

---

## Inference

The baseline inference script:

* Uses an OpenAI-compatible client
* Reads configuration from environment variables:

  * API_BASE_URL
  * MODEL_NAME
  * HF_TOKEN
* Produces structured logs in the required format:

```
[START]
[STEP]
[END]
```

The script demonstrates reproducible behavior across all task levels.

---

## Setup

### Local Execution

```
git clone <repository-url>
cd support-triage-env

docker build -t support-triage-env .
docker run support-triage-env
```

---

## Deployment

* Deployed as a Docker-based Hugging Face Space
* Compatible with OpenEnv validation pipeline
* Designed to run within constrained compute environments

---

## Key Features

* Real-world task simulation
* Multi-level difficulty progression
* Reward shaping with intermediate signals
* Multi-step decision-making
* Deterministic evaluation
* Lightweight and deployable

---

## Conclusion

The Support Triage Environment provides a practical benchmark for evaluating AI agents in customer support workflows. It captures key challenges such as ambiguity handling, prioritization, and efficient decision-making, making it suitable for both training and evaluation of intelligent systems.
