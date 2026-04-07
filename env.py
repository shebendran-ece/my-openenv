class OpenEnv:
    def __init__(self):
        self.current_task = 0

    def reset(self):
        self.current_task = 1
        return {"task": "email classification"}

    def step(self, action):
        reward = 0.0

        if self.current_task == 1:
            if action == "important":
                reward = 1.0
            else:
                reward = 0.2

        done = True
        return {"next": None}, reward, done, {}

    def state(self):
        return {"task_id": self.current_task}