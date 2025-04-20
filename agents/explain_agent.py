def explain_decision(text):
    if "confidential" in text.lower():
        return "Mentions confidential information"
    elif "salary" in text.lower():
        return "Sensitive financial details"
    return "Language may need further review"
