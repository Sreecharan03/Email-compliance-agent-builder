from transformers import pipeline

classifier = pipeline("text-classification", model="bert-base-uncased")

def classify_email(text):
    result = classifier(text[:512])[0]
    label = result['label']
    score = result['score']
    if label == "LABEL_0":
        return "Compliant", score
    elif score > 0.9:
        return "Non-Compliant", score
    else:
        return "Needs Review", score
