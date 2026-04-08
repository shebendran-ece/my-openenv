from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    action: str

state_data = {"task": "email classification"}

@app.get("/")
def home():
    return {"message": "OpenEnv Running"}

@app.post("/reset")
def reset():
    global state_data
    state_data = {"task": "email classification"}
    return state_data

@app.post("/step")
def step(action: Action):
    reward = 1.0 if action.action == "important" else 0.2
    return {
        "observation": "next",
        "reward": reward,
        "done": True,
        "info": {}
    }

@app.get("/state")
def state():
    return state_data
