import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

class NewsAPI:
    BASE_URL = "https://newsapi.org/v2/"

    def __init__(self):
        self.api_key = NEWS_API_KEY

    def get_financial_news(self, ticker, days=14):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        from_date = start_date.strftime('%Y-%m-%d')
        to_date = end_date.strftime('%Y-%m-%d')

        endpoint = f"{self.BASE_URL}everything"
        params = {
            'q': f"{ticker} OR {self._get_company_name(ticker)}",
            'from': from_date,
            'to': to_date,
            'language': 'en',
            'sortBy': 'publishedAt',
            'apiKey': self.api_key
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()

            articles = [
                {
                    'title': article.get('title', ''),
                    'description': article.get('description', ''),
                    'content': article.get('content', ''),
                    'url': article.get('url', ''),
                    'source': article.get('source', {}).get('name', ''),
                    'published_at': article.get('publishedAt', '')
                }
                for article in data.get('articles', [])
            ]

            return articles

        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return []

    def _get_company_name(self, ticker):
        company_map = {
            'AAPL': 'Apple',
            'MSFT': 'Microsoft',
            'GOOGL': 'Google',
            'AMZN': 'Amazon',
            'META': 'Facebook',
            'TSLA': 'Tesla',
            'NFLX': 'Netflix',
            'NVDA': 'NVIDIA',
            'JPM': 'JPMorgan'
        }
        return company_map.get(ticker.upper(), ticker)
