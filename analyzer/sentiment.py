import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import string

#Use BERT model for sentiment analysis
class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Load pre-trained model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
    def preprocess_text(self, text):
        # Convert text to lowercase for uniformity
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        return text
        
    def analyze_sentiment(self, text):
        if not text:
            return 0  # Neutral if no text is available
            
        text = self.preprocess_text(text)
        
        # Tokenize and prepare for model
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(self.device)
        
        # Get prediction
        with torch.no_grad():
            outputs = self.model(**inputs)
            scores = outputs.logits.softmax(dim=1)
            
        # Convert to sentiment score in range [-1, 1] similar to VADER
        # Assuming index 0 is negative and index 1 is positive
        negative_score = scores[0, 0].item()
        positive_score = scores[0, 1].item()
        
        # Calculate compound score similar to VADER's compound
        compound = positive_score - negative_score
        
        return compound
        
    def analyze_articles(self, articles):
        for article in articles:
            article['sentiment_score'] = self.analyze_sentiment(article['content'])
        return articles