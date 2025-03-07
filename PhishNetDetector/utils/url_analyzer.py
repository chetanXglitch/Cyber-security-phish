import re
from urllib.parse import urlparse

def analyze_url(url):
    # Heuristic rules for phishing detection
    suspicious_keywords = ["login", "verify", "account", "bank", "paypal", "secure"]
    suspicious_domains = ["freegiftcards.com", "phishingsite.com"]

    # Check for suspicious keywords in the URL
    if any(keyword in url for keyword in suspicious_keywords):
        return "Suspicious URL (contains phishing keywords)."

    # Check for suspicious domains
    domain = urlparse(url).netloc
    if domain in suspicious_domains:
        return "Suspicious URL (known phishing domain)."

    # Check for URL shortening services
    if re.match(r"bit\.ly|goo\.gl|tinyurl\.com", domain):
        return "Suspicious URL (uses URL shortening service)."

    return "URL appears safe."