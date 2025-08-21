import numpy as np
import requests
import os
from dotenv import load_dotenv
import string
import time

#vercel-sentiment-app
load_dotenv()

# Use BERT model for sentiment analysis via HuggingFace API
class SentimentAnalyzer:
    def __init__(self, model_name="distilbert/distilbert-base-uncased-finetuned-sst-2-english"):
        # Store model name and setup API
        self.model_name = model_name
        self.api_token = os.getenv('HF_API_TOKEN')
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        
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
        
        # Call HuggingFace API
        payload = {"inputs": text}
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            
            if response.status_code == 503:
                # Model is loading, wait and retry once
                time.sleep(20)
                response = requests.post(self.api_url, headers=self.headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                
                # Process the result to match your original output format
                if result and isinstance(result, list) and len(result) > 0:
                    scores = result[0]
                    
                    negative_score = 0
                    positive_score = 0
                    
                    # Extract scores based on labels
                    for score_item in scores:
                        if score_item['label'] == 'NEGATIVE':
                            negative_score = score_item['score']
                        elif score_item['label'] == 'POSITIVE':
                            positive_score = score_item['score']
                    
                    # Calculate compound score similar to your original method
                    compound = positive_score - negative_score
                    return compound
                else:
                    return 0  # Neutral if no valid result
            else:
                print(f"API Error: {response.status_code} - {response.text}")
                return 0  # Return neutral on error
                
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return 0  # Return neutral on error
        
    def analyze_articles(self, articles):
        for article in articles:
            article['sentiment_score'] = self.analyze_sentiment(article['content'])
            # Small delay to respect API rate limits
            time.sleep(0.1)
        return articles