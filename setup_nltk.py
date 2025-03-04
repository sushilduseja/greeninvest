import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def setup_nltk():
    """Download required NLTK data"""
    try:
        nltk.download('vader_lexicon', quiet=True)
        print("Successfully downloaded VADER lexicon")
    except Exception as e:
        print(f"Error downloading VADER lexicon: {e}")

if __name__ == "__main__":
    setup_nltk()
