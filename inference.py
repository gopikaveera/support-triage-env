import os
from openai import OpenAI
from env.support_triage_env import SupportTriageEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Missing HF_TOKEN or API_KEY")
if not API_BASE_URL:
    raise ValueError("API_BASE_URL is missing in environment variables")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

if API_KEY is None:
    raise ValueError("API_KEY environment variable is required")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)


def warmup_llm():
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": "Say OK"}
            ]
        )
        print("[WARMUP]", response.choices[0].message.content)
    except Exception as e:
        print("[WARMUP ERROR]", str(e))


warmup_llm()


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
            text = state.get("scenario", "No scenario provided")

            try:
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

            except Exception as llm_error:
                print(f"[LLM ERROR] {str(llm_error)}")
                action = "assist"  # fallback

            if action not in ["monitor", "clarify", "assist", "escalate"]:
                action = "assist"

            state, reward, done, _ = env.step(action)
            rewards.append(reward)

            print(f"[STEP] step={step+1} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

            if done:
                success = True
                break

    except Exception as e:
        success = False
        print(f"[ERROR] {str(e)}")

    finally:
        score = sum(rewards) / len(rewards) if rewards else 0.0

        print(
        f"[END] success={str(success).lower()} "
        f"steps={len(rewards)} "
        f"score={score:.2f} "
        f"rewards={','.join(f'{r:.2f}' for r in rewards)}"
    )
