def check_domain_similarity(filename):
    suspicious_domains = ["secure-login.com", "account-verify.net", "fake-bank.org"]
    for domain in suspicious_domains:
        if domain in filename.lower():
            return f"Suspicious domain detected in filename: {domain}"
    return "No suspicious domain patterns detected."
