
title: Support Triage Environment
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
Support Triage Environment
Overview
This project simulates a real-world customer support triage system where an AI agent must decide the most appropriate action for incoming user issues.

The agent must classify each scenario into one of the following actions:

assist
clarify
escalate
monitor
This environment is designed to evaluate decision-making, ambiguity handling, and prioritization skills of AI systems. The scenarios reflect common customer support workflows such as authentication issues, payment failures, system outages, and user ambiguity handling.

Real-World Motivation
Customer support teams constantly triage user issues based on urgency, clarity, and impact. This environment models that workflow for training and evaluating intelligent agents.

Note: Scenarios are synthetically generated based on real-world customer support patterns.

Action Space
The agent can choose one of the following actions:

assist → Provide direct help for solvable issues
clarify → Ask for more information when the issue is unclear
escalate → Forward critical or system-level issues
monitor → Track low-priority or intermittent issues
Observation Space
Each step provides: { "scenario": "User issue description", "step": 0 }

Tasks
The environment includes three levels of tasks based on scenario difficulty:

Easy Tasks
Clear and well-defined user issues
Direct mapping to a single correct action
Example: OTP not received → assist
Medium Tasks
Partially ambiguous scenarios
Requires reasoning between multiple possible actions
Example: vague error message → clarify
Hard Tasks
Critical, high-risk, or edge-case scenarios
Requires correct prioritization and escalation
Example: system outage or security issue → escalate
Each task is evaluated using a deterministic grader that compares the agent’s action with the expected correct action.

Reward Design
Correct action → +1.0
Partially correct → +0.25
Incorrect → -1.0
Difficulty scaling:

Medium → ×1.1
Hard → ×1.2
This ensures meaningful reward shaping across trajectories.

Environment Design
Randomized scenario selection
Fixed episode length
Deterministic grading
Supports OpenEnv interface
OpenEnv Compliance
This environment follows the OpenEnv specification:

Implements reset(), step(), and state()
Uses structured observation, action, and reward formats
Includes deterministic grading
Provides openenv.yaml metadata
Validated using OpenEnv validation tools.

Inference
The baseline inference script:

Uses OpenAI client
Reads environment variables
Produces standardized logs: [START] [STEP] [END]
Setup
Run Locally
Clone the repository

Build the Docker image:

docker build -t support-triage-env
Run the container: docker run support-triage-env

Deployment
Deployed as a Hugging Face Space
Docker-based execution
Compatible with OpenEnv validation
Baseline Performance
The Baseline inference script produces reproducible scores across tasks, demonstrating the environment's ability to evaluate agent performance under varying difficulty levels.

Key Features
Real-world task simulation
Multi-level difficulty
Deterministic grading
Continuous reward feedback
Lightweight and deployable
Conclusion
This environment provides a practical benchmark for evaluating AI agents in customer support decision-making scenarios.
