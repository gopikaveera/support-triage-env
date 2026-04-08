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
    global current_step
    current_step = 0

    return {
        "scenario": random.choice(scenarios),
        "step": current_step
    }


# ✅ REQUIRED: STEP ENDPOINT
@app.post("/step")
def step(action: str):
    global current_step
    current_step += 1

    # Simple reward logic
    if action == "assist":
        reward = 1.0
    elif action == "clarify":
        reward = 0.25
    elif action == "escalate":
        reward = 1.0
    else:
        reward = -1.0

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
