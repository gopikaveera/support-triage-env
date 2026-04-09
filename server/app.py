from fastapi import FastAPI
import random

app = FastAPI()
current_step = 0
current_scenario = ""

scenarios = [
    "OTP not received",
    "Payment deducted but order not confirmed",
    "App crashes randomly",
    "Need help but not clear"
]


@app.get("/")
def read_root():
    return {"status": "running"}



@app.post("/reset")
def reset():
    global current_step, current_scenario
    current_step = 0
    current_scenario = random.choice(scenarios)

    return {
        "scenario": current_scenario,
        "step": current_step
    }



@app.post("/step")
def step(action: str):
    global current_step, current_scenario
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

    # HARD SAFETY (fixes your failure)
    reward = max(0.01, min(0.99, float(reward)))

    done = current_step >= 5

    return {
        "reward": reward,
        "done": done
    }


#  Required entry point
def main():
    return app


if __name__ == "__main__":
    main()
