import random
from tasks.scenarios import SCENARIOS
from grader.grader import grade

class SupportTriageEnv:
    def __init__(self, max_steps=5):
        self.max_steps = max_steps
        self.step_count = 0
        self.current = None

    def reset(self):
        self.step_count = 0
        self.current = random.choice(SCENARIOS)
        return self.state()

    def state(self):
        return {
            "scenario": self.current["text"],
            "step": self.step_count
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

        done = self.step_count >= self.max_steps

        # Move to next scenario
        self.current = random.choice(SCENARIOS)

        return self.state(), reward, done, {}