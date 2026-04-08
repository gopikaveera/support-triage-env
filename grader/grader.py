def grade(action, correct_action):
    """
    Returns a score strictly between (0, 1)
    """

    # Perfect match
    if action == correct_action:
        return 0.9

    # Close / reasonable actions
    if correct_action == "assist" and action == "clarify":
        return 0.6

    if correct_action == "clarify" and action == "assist":
        return 0.6

    if correct_action == "monitor" and action == "assist":
        return 0.5

    if correct_action == "assist" and action == "monitor":
        return 0.5

    # Moderate mistake
    if action in ["assist", "clarify"] and correct_action in ["assist", "clarify"]:
        return 0.4

    # Escalation mistakes (more serious)
    if action == "escalate" and correct_action != "escalate":
        return 0.2

    # Default wrong but still valid range
    return 0.1
