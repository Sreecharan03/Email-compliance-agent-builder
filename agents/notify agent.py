def alert_on_violation(summary):
    if summary["status"] == "Non-Compliant":
        print(f"🚨 Alert: Violation from {summary['sender']}")
