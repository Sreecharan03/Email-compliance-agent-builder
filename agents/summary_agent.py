def generate_summary(email, compliance, explanation, policy_context):
    return {
        "sender": email["from"],
        "subject": email["subject"],
        "status": compliance,
        "reason": explanation,
        "policy_reference": policy_context
    }
