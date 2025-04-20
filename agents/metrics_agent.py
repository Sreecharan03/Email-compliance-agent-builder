def aggregate_metrics(summaries):
    total = len(summaries)
    violations = sum(1 for s in summaries if s['status'] == "Non-Compliant")
    return {
        "total_emails": total,
        "violations": violations,
        "compliance_rate": 100 * (total - violations) / total
    }
