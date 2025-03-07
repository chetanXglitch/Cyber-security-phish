from utils.email_analyzer import analyze_email

def test_email_analyzer():
    # Test 1: Suspicious email with phishing keywords
    email1 = "URGENT: Your account has been suspended. Verify your password now!"
    assert analyze_email(email1) == "Suspicious email (contains phishing keywords)."

    # Test 2: Suspicious email with links
    email2 = "Please click this link to verify your account: http://phishingsite.com"
    assert analyze_email(email2) == "Suspicious email (contains links)."

    # Test 3: Safe email
    email3 = "Hello, just checking in to see how you're doing."
    assert analyze_email(email3) == "Email appears safe."

    print("All email analyzer tests passed!")

if __name__ == "__main__":
    test_email_analyzer()