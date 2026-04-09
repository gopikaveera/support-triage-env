def clamp_score(score):
    return max(0.01, min(0.99, score))

def grade(action, correct_action):
    # Perfect match
    if action == correct_action:
        return clamp_score(0.9)

    # Close / reasonable actions
    if correct_action == "assist" and action == "clarify":
        return clamp_score(0.6)

    if correct_action == "clarify" and action == "assist":
        return clamp_score(0.6)

    if correct_action == "monitor" and action == "assist":
        return clamp_score(0.5)

    if correct_action == "assist" and action == "monitor":
        return clamp_score(0.5)

    # Moderate mistake
    if action in ["assist", "clarify"] and correct_action in ["assist", "clarify"]:
        return clamp_score(0.4)

    # Escalation mistakes (more serious)
    if action == "escalate" and correct_action != "escalate":
        return clamp_score(0.2)

    # Default wrong but still valid range
    return clamp_score(0.1)
