from config import *
from agents.ingest_agent import fetch_emails
from agents.preprocess_agent import clean_email_body
from agents.classify_agent import classify_email
from agents.explain_agent import explain_decision
from agents.summary_agent import generate_summary
from agents.metrics_agent import aggregate_metrics
from agents.notify_agent import alert_on_violation
from utils.rag_weaviate import retrieve_policy_context

def run_pipeline():
    emails = fetch_emails(EMAIL_API, USERNAME, PASSWORD)
    summaries = []
    for email in emails:
        clean_body = clean_email_body(email["body"])
        status, confidence = classify_email(clean_body)
        explanation = explain_decision(clean_body)
        policy = retrieve_policy_context(clean_body)
        summary = generate_summary(email, status, explanation, policy)
        alert_on_violation(summary)
        summaries.append(summary)
    metrics = aggregate_metrics(summaries)
    print("\n📊 Compliance Metrics:", metrics)

if __name__ == "__main__":
    run_pipeline()
