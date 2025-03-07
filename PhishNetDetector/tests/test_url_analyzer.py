from utils.url_analyzer import analyze_url

def test_url_analyzer():
    assert analyze_url("http://freegiftcards.com") == "Suspicious URL (known phishing domain)."
    assert analyze_url("http://google.com") == "URL appears safe."
    print("All URL analyzer tests passed!")

if __name__ == "__main__":
    test_url_analyzer()