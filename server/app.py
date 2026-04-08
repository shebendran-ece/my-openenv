from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------- Models --------
class Observation(BaseModel):
    state: str

class Action(BaseModel):
    action: str

class StepResponse(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict

# -------- State --------
current_state = "start"

# -------- Routes --------
@app.get("/")
def home():
    return {"message": "OpenEnv Running"}

@app.post("/reset")
def reset():
    global current_state
    current_state = "start"
    return Observation(state=current_state)

@app.post("/step")
def step(action: Action):
    global current_state

    if action.action == "next":
        current_state = "progress"
        return StepResponse(
            observation=Observation(state=current_state),
            reward=1.0,
            done=False,
            info={}
        )
    else:
        return StepResponse(
            observation=Observation(state=current_state),
            reward=0.0,
            done=True,
            info={}
        )

@app.get("/state")
def state():
    return {"state": current_state}
