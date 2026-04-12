SCENARIOS = [
    {
        "id": 1,
        "text": "User says OTP is not arriving during payment checkout, money is on hold and they are worried the transaction might fail.",
        "correct_action": "assist",
        "reason": "Clear issue that can be resolved with guidance",
        "difficulty": "easy",
        "category": "auth"
    },
    {
        "id": 2,
        "text": "User writes 'it is not working' without giving any details.",
        "correct_action": "clarify",
        "reason": "Request is ambiguous",
        "difficulty": "easy",
        "category": "auth"
    },
    {
        "id": 3,
        "text": "User says they are unable to navigate to the settings page and cannot find required options.",
        "correct_action": "assist",
        "reason": "Usability issue that can be guided",
        "difficulty": "medium",
        "category": "performance"
    },
    {
        "id": 4,
        "text": "User requests a refund immediately after signing up without using the service.",
        "correct_action": "assist",
        "reason": "Standard refund policy can handle this",
        "difficulty": "medium",
        "category": "billing"
    },
    {
        "id": 5,
        "text": "User reports payment was deducted but account still shows inactive, and they mention this has already happened once before.",
        "correct_action": "escalate",
        "reason": "Financial issue affecting trust and service",
        "difficulty": "medium",
        "category": "billing"
    },
    {
        "id": 6,
        "text": "User gets a generic error message 'Something went wrong' after login.",
        "correct_action": "clarify",
        "reason": "Insufficient details to diagnose",
        "difficulty": "medium",
        "category": "auth"
    },
    {
        "id": 7,
        "text": "User account is locked after multiple failed login attempts.",
        "correct_action": "assist",
        "reason": "Can be resolved through account recovery",
        "difficulty": "easy",
        "category": "auth"
    },
    {
        "id": 8,
        "text": "User reports that the app is slightly slow during peak hours but still usable.",
        "correct_action": "monitor",
        "reason": "Low priority performance issue",
        "difficulty": "medium",
        "category": "performance"
    },
    {
        "id": 9,
        "text": "User says the entire website is down, no one in their team can log in, and this is affecting business operations urgently.",
        "correct_action": "escalate",
        "reason": "Critical system-wide outage",
        "difficulty": "hard",
        "category": "performance"
    },
    {
        "id": 10,
        "text": "User is unable to pass the 'I am not a robot' CAPTCHA verification despite multiple attempts.",
        "correct_action": "assist",
        "reason": "Common solvable issue with guidance",
        "difficulty": "medium",
        "category": "auth"
    },
    {
        "id": 11,
        "text": "User reports sensitive account data appears incorrect after login and is concerned about possible data corruption or breach.",
        "correct_action": "escalate",
        "reason": "Potential data integrity or security issue",
        "difficulty": "hard",
        "category": "security"
    },
    {
        "id": 12,
        "text": "User says the app occasionally logs them out randomly.",
        "correct_action": "monitor",
        "reason": "Intermittent issue not immediately critical",
        "difficulty": "medium",
        "category": "auth"
    },
    {
    "id": 13,
    "text": "User reports receiving multiple spam emails from the platform even after unsubscribing.",
    "correct_action": "escalate",
    "reason": "Possible security or system-level issue affecting user trust",
    "difficulty": "hard",
    "category": "security"
    },
    {
    "id": 14,
    "text": "User says their account was accessed from an unknown device, they did not log in, and they are worried about unauthorized access.",
    "correct_action": "escalate",
    "reason": "Potential account breach or unauthorized access",
    "difficulty": "hard",
    "category": "security"
    },
    {
    "id": 15,
    "text": "User reports that their password reset link is expired immediately after receiving it.",
    "correct_action": "assist",
    "reason": "Common issue that can be resolved by guiding user through reset process",
    "difficulty": "medium",
    "category": "auth"
    },
    {
    "id": 16,
    "text": "User complains that the mobile app crashes only when uploading a profile picture.",
    "correct_action": "assist",
    "reason": "Specific reproducible issue that can be guided or troubleshooted",
    "difficulty": "medium",
    "category": "performance"
    },
    {
    "id": 17,
    "text": "User says they are being charged twice for the same subscription and is frustrated as support has not responded yet.",
    "correct_action": "escalate",
    "reason": "Billing error involving financial impact",
    "difficulty": "hard",
    "category": "billing"
    }
]
