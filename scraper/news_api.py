import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

class NewsAPI:
    BASE_URL = "https://finnhub.io/api/v1/"

    def __init__(self):
        self.api_key = FINNHUB_API_KEY

    def get_financial_news(self, ticker, days=14):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        from_date = start_date.strftime('%Y-%m-%d')
        to_date = end_date.strftime('%Y-%m-%d')

        endpoint = f"{self.BASE_URL}company-news"
        params = {
            'symbol': ticker.upper(),
            'from': from_date,
            'to': to_date,
            'token': self.api_key
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()

            articles = [
                {
                    'title': article.get('headline', ''),
                    'description': article.get('summary', ''),
                    'content': article.get('summary', ''),
                    'url': article.get('url', ''),
                    'source': article.get('source', ''),
                    'published_at': self._convert_timestamp(article.get('datetime', 0)),
                    'image': article.get('image', ''),
                    'category': article.get('category', ''),
                    'related_symbols': article.get('related', [])
                }
                for article in data if isinstance(data, list)
            ]

            return articles

        except requests.exceptions.RequestException as e:
            print(f"Error fetching news from Finnhub: {e}")
            return []
        except Exception as e:
            print(f"Error processing news data: {e}")
            return []

    def _convert_timestamp(self, timestamp):
        try:
            if timestamp:
                return datetime.fromtimestamp(timestamp).isoformat() + 'Z'
            return ''
        except:
            return ''

    def get_company_profile(self, ticker):
        
        endpoint = f"{self.BASE_URL}stock/profile2"
        params = {
            'symbol': ticker.upper(),
            'token': self.api_key
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching company profile: {e}")
            return {}