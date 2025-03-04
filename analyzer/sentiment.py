import nltk
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download("vader_lexicon")

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def preprocess_text(self, text):
        # Convert text to lowercase for uniformity
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        return text

    def analyze_sentiment(self, text):
        if not text:
            return 0  # Neutral if no text is available
        
        text = self.preprocess_text(text) # Preprocess the text before analyzing sentiment
        score = self.analyzer.polarity_scores(text)
        return score['compound']

    def analyze_articles(self, articles):
        for article in articles:
            article['sentiment_score'] = self.analyze_sentiment(article['content'])
        return articles
