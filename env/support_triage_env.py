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

        # Reward shaping
        reward = float(base_reward)

        # Bonus for correct action on first step
        if action == correct_action and self.step_count == 1:
            reward += 0.1

        # Penalty for repeating same action
        if len(self.history) >= 1 and action == self.history[-1]:
            reward -= 0.05

        # Clamp reward
        reward = max(0.01, min(0.99, reward))

        self.history.append(action)

        difficulty = self.current.get("difficulty", "easy")

       
        if action == correct_action:
            # Hard tasks require at least 2 steps
            if difficulty == "hard" and self.step_count < 2:
                done = False
            else:
                done = True
        else:
            done = self.step_count >= self.max_steps

        return self.state(), reward, done, {}
