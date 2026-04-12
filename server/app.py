from fastapi import FastAPI
import random
import subprocess


app = FastAPI()

current_step = 0
current_scenario = ""
current_task = ""

# Task-specific scenario pools
TASK_POOLS = {
    "easy": [
        "OTP not received",
        "Login issue"
    ],
    "medium": [
        "App crashes randomly",
        "Feature not working properly"
    ],
    "hard": [
        "Payment deducted but order not confirmed",
        "Charged twice for same order"
    ]
}

@app.on_event("startup")
def run_inference():
    subprocess.Popen(["python", "inference.py"])


@app.get("/")
def read_root():
    return {"status": "running"}



@app.post("/reset")
def reset(task: str = "easy"):
    global current_step, current_scenario, current_task

    current_step = 0
    current_task = task

    # fallback safety
    pool = TASK_POOLS.get(task, ["General issue"])

    current_scenario = random.choice(pool)

    return {
        "scenario": current_scenario,
        "step": current_step,
        "task": current_task   
    }



@app.post("/step")
def step(action: str):
    global current_step, current_scenario, current_task
    current_step += 1

    scenario = current_scenario.lower()

    # Determine correct action
    if "otp" in scenario or "login" in scenario:
        correct_action = "assist"
    elif "payment" in scenario or "charged" in scenario:
        correct_action = "escalate"
    elif "crash" in scenario or "bug" in scenario:
        correct_action = "assist"
    elif "not clear" in scenario or "help" in scenario:
        correct_action = "clarify"
    else:
        correct_action = "monitor"

    # SAFE reward logic
    if action == correct_action:
        reward = 0.85
    elif action in ["assist", "clarify", "escalate", "monitor"]:
        reward = 0.55
    else:
        reward = 0.15


    reward = max(0.01, min(0.99, float(reward)))

    done = current_step >= 5

    return {
        "reward": reward,
        "done": done,
        "task": current_task   
    }


def main():
    return app


if __name__ == "__main__":
    main()
