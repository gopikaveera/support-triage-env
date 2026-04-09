import random
from tasks.scenarios import SCENARIOS
from grader.grader import grade

class SupportTriageEnv:
    def __init__(self, max_steps=5):
        self.max_steps = max_steps
        self.step_count = 0
        self.current = None
        self.history = []

    def reset(self):
        self.step_count = 0
        self.current = random.choice(SCENARIOS)
        self.history = []
        return self.state()

    def state(self):
        return {
            "scenario": self.current["text"],
            "step": self.step_count,
            "history": self.history,
            "progress": f"Step {self.step_count} of {self.max_steps}"
        }

    def step(self, action):
        self.step_count += 1

        correct_action = self.current["correct_action"]
        base_reward = grade(action, correct_action)

        # Difficulty-aware reward
        difficulty = self.current["difficulty"]

        if difficulty == "medium":
            reward = base_reward * 1.1
        elif difficulty == "hard":
            reward = base_reward * 1.2
        else:
            reward = base_reward

        # Keep reward strictly within (0, 1)
        reward = max(0.01, min(0.99, reward))

        # Track action history
        self.history.append(action)

        # Termination logic
        if action == correct_action:
            done = True
        else:
            done = self.step_count >= self.max_steps

        return self.state(), reward, done, {}
