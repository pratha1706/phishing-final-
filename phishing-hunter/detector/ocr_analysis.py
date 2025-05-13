import pytesseract
from PIL import Image
import re

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def analyze_text(text):
    suspicious_keywords = ["password", "verify", "account", "urgent", "login", "click here", "update", "bank", "credentials"]
    score = 0
    findings = []

    for keyword in suspicious_keywords:
        matches = re.findall(keyword, text, re.IGNORECASE)
        if matches:
            findings.append(f"Found keyword: {keyword} ({len(matches)} times)")
            score += len(matches) * 5

    if len(text.split()) < 5:
        findings.append("Text is too short. Could be suspicious.")
        score += 10

    return {
        "score": min(score, 100),
        "findings": findings
    }
