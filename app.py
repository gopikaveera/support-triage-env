from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "running"}

# Run inference once at startup
@app.on_event("startup")
def run_inference():
    subprocess.run(["python", "inference.py"])