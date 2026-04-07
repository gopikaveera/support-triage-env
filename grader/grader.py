VALID_ACTIONS = ["monitor", "clarify", "assist", "escalate"]

def grade(action, correct_action):
    # Case 1: Invalid action
    if action not in VALID_ACTIONS:
        return -0.5

    # Case 2: Correct action
    if action == correct_action:
        return 1.0

    # Case 3: Near miss logic
    if correct_action == "assist" and action == "clarify":
        return 0.25
    if correct_action == "clarify" and action == "assist":
        return 0.25
    if correct_action == "monitor" and action == "clarify":
        return 0.25

    # Case 4: Wrong action
    return -1.0