import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (if not already downloaded)
nltk.download("vader_lexicon")

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        if not text:
            return 0  # Neutral if no text is available

        score = self.analyzer.polarity_scores(text)
        return score['compound']

    def analyze_articles(self, articles):
        for article in articles:
            article['sentiment_score'] = self.analyze_sentiment(article['content'])
        return articles
