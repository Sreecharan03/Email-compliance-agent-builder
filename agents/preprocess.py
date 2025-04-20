import re

def clean_email_body(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'Sent from.*', '', text)
    return text.strip()
