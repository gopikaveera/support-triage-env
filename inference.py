import os
from openai import OpenAI
from env.support_triage_env import SupportTriageEnv

# Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY environment variable is required")

# Initialize OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

# Task setup
TASKS = ["easy", "medium", "hard"]
BENCHMARK = "support_triage_env"

for TASK_NAME in TASKS:
    env = SupportTriageEnv()

    print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}")

    rewards = []
    success = False

    try:
        state = env.reset()

        for step in range(5):
            text = state["scenario"]

            # REQUIRED API CALL
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a support triage agent. Choose ONLY one action: monitor, clarify, assist, escalate."
                    },
                    {
                        "role": "user",
                        "content": f"Scenario: {text}\nAnswer with one word."
                    }
                ]
            )

            action = response.choices[0].message.content.strip().lower()

            # Safety fallback
            if action not in ["monitor", "clarify", "assist", "escalate"]:
                action = "assist"

            state, reward, done, _ = env.step(action)
            rewards.append(reward)

            print(f"[STEP] step={step+1} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

            if done:
                success = True
                break

    except Exception:
        success = False

    finally:
        print(f"[END] success={str(success).lower()} steps={len(rewards)} rewards={','.join(f'{r:.2f}' for r in rewards)}")
