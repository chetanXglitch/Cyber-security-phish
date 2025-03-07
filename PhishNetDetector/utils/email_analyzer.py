import re

def is_fake_gmail(email):
    """
    Check if the Gmail ID is fake or dummy.
    """
    # Common fake Gmail patterns
    fake_patterns = [
        r"security[-_]?team",
        r"support[-_]?team",
        r"admin[-_]?account",
        r"no[-_]?reply",
        r"user\d+",
        r"info[-_]?service",
        r"verify[-_]?account",
        r"prize[-_]?winner",
    ]

    # Check if the email matches any fake pattern
    for pattern in fake_patterns:
        if re.search(pattern, email, re.IGNORECASE):
            return True

    # Check for generic or suspicious usernames
    username = email.split("@")[0]
    if username.lower() in ["user", "admin", "support", "security", "info", "no-reply"]:
        return True

    return False

def analyze_email(email):
    """
    Analyze the email content and sender's email address for phishing attempts.
    """
    # Heuristic rules for phishing detection
    suspicious_keywords = ["urgent", "password", "verify", "account", "suspended", "login", "bank", "paypal"]
    suspicious_links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email)

    # Extract sender's email address (simulated for this example)
    sender_match = re.search(r'From:\s*([\w\.-]+@[\w\.-]+)', email)
    sender = sender_match.group(1) if sender_match else ""

    # Check if the sender's email is a fake or dummy Gmail
    if sender.endswith("@gmail.com") and is_fake_gmail(sender):
        return "Suspicious email (fake or dummy Gmail ID detected)."

    # Check for suspicious keywords
    if any(keyword in email.lower() for keyword in suspicious_keywords):
        return "Suspicious email (contains phishing keywords)."

    # Check for suspicious links
    if suspicious_links:
        return "Suspicious email (contains links)."

    return "Email appears safe."