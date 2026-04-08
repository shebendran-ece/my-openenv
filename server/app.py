from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    action: str

@app.get("/")
def home():
    return {"message": "OpenEnv Running"}

@app.post("/reset")
def reset():
    return {"observation": "start"}

@app.post("/step")
def step(action: Action):
    return {
        "observation": "next",
        "reward": 1.0,
        "done": True,
        "info": {}
    }

@app.get("/state")
def state():
    return {"state": "ok"}
