import re
import ssl
from urllib.error import URLError

# Initialize sentiment analysis with fallback
HAVE_NLTK = False
try:
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    
    # Handle SSL certificate issues
    try:
        _create_unverified_https_context = ssl._create_unverified_context
        ssl._create_default_https_context = _create_unverified_https_context
    except AttributeError:
        pass

    # Try to initialize VADER
    try:
        nltk.data.find('sentiment/vader_lexicon')
        sentiment_analyzer = SentimentIntensityAnalyzer()
        HAVE_NLTK = True
    except (LookupError, URLError):
        try:
            nltk.download('vader_lexicon', quiet=True)
            sentiment_analyzer = SentimentIntensityAnalyzer()
            HAVE_NLTK = True
        except Exception:
            print("Warning: NLTK VADER lexicon not available. Using fallback sentiment analysis.")
except ImportError:
    print("Warning: NLTK not available. Using fallback sentiment analysis.")

def simple_sentiment_analysis(text):
    """Fallback sentiment analysis using simple keyword matching"""
    if not text:
        return 0.5
        
    # Simple positive and negative word lists
    positive_words = {'good', 'great', 'positive', 'excellent', 'sustainable', 'ethical', 
                     'responsible', 'green', 'efficient', 'improvement', 'innovative'}
    negative_words = {'bad', 'poor', 'negative', 'unethical', 'unsustainable', 'violation', 
                     'risk', 'penalty', 'scandal', 'inefficient'}
    
    words = set(re.findall(r'\w+', text.lower()))
    pos_count = len(words.intersection(positive_words))
    neg_count = len(words.intersection(negative_words))
    total = pos_count + neg_count
    
    if total == 0:
        return 0.5
    
    return pos_count / total

def analyze_esg(text):
    """
    Analyze ESG-related text using available sentiment analysis methods.
    
    Parameters:
        text (str): Text from a corporate ESG report.
    
    Returns:
        tuple: ESG score (float) and the sentiment analysis result (dict).
    """
    if not text or len(text.strip()) == 0:
        return 0.5, {"compound": 0.5, "pos": 0.0, "neu": 1.0, "neg": 0.0}

    try:
        if HAVE_NLTK:
            # Use VADER if available
            sentiment_scores = sentiment_analyzer.polarity_scores(text)
            esg_score = (sentiment_scores['compound'] + 1) / 2
        else:
            # Use fallback sentiment analysis
            score = simple_sentiment_analysis(text)
            sentiment_scores = {
                "compound": (score * 2) - 1,  # Convert [0,1] to [-1,1]
                "pos": score,
                "neu": 0.0,
                "neg": 1 - score
            }
            esg_score = score

        return esg_score, sentiment_scores

    except Exception as e:
        print(f"Error during sentiment analysis: {str(e)}")
        return 0.5, {"compound": 0.5, "pos": 0.0, "neu": 1.0, "neg": 0.0}
