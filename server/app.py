from fastapi import FastAPI
import random
import subprocess

app = FastAPI()

# Sample scenarios
scenarios = [
    "OTP not received",
    "Payment deducted but order not confirmed",
    "App crashes randomly",
    "Need help but not clear"
]

current_step = 0


# Health check (optional but good)
@app.get("/")
def read_root():
    return {"status": "running"}


# ✅ REQUIRED: RESET ENDPOINT
@app.post("/reset")
def reset():
    global current_step, current_scenario
    current_step = 0

    current_scenario = random.choice(scenarios)

    return {
        "scenario": current_scenario,
        "step": current_step
    }

# ✅ REQUIRED: STEP ENDPOINT
@app.post("/step")
def step(action: str):
    global current_step
    current_step += 1

    # Use LAST scenario from reset (important)
    global current_scenario

    scenario = current_scenario.lower()

    # Rule-based mapping (deterministic)
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

    # Reward logic
    if action == correct_action:
        reward = 0.9
    elif action in ["assist", "clarify", "escalate", "monitor"]:
        reward = 0.5
    else:
        reward = 0.1

    done = current_step >= 5

    return {
        "reward": reward,
        "done": done
    }

# (Optional) Run inference at startup — keep if needed
@app.on_event("startup")
def run_inference():
    subprocess.run(["python", "inference.py"])

def main():
    return app


if __name__ == "__main__":
    main()

