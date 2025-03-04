# Financial News Sentiment Analyzer

## Description
A Python-based web application that performs sentiment analysis on financial news articles using the NewsAPI and NLTK's VADER sentiment analysis tool. The application scrapes recent financial news, analyzes the sentiment, and provides insights into the emotional tone of financial reporting.

## Features
- Fetch latest financial news using NewsAPI
- Perform sentiment analysis using NLTK VADER
- Web interface to display news sentiment results
- Categorize news articles by sentiment (positive, negative, neutral)

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Installation

### Clone the Repository
```bash
git clone https://github.com/wesleymeredith/financial-news-sentiment-analyzer.git
cd financial-news-sentiment-analyzer
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
1. Create a `.env` file in the project root
2. Add your NewsAPI key:
```
NEWS_API_KEY=your_newsapi_key_here
```

## Running the Application
```bash
flask run
```

## Project Structure
```
financial-news-sentiment-analyzer/
│
├── scraper/               # News scraping module
│   ├── __init__.py
│   └── news_api.py        # NewsAPI integration
│
├── analyzer/              # Sentiment analysis module
│   ├── __init__.py
│   └── sentiment.py       # NLTK VADER sentiment logic
│
├── templates/             # HTML templates
│   ├── index.html         # Home page
│   └── results.html       # Sentiment results page
│
├── requirements.txt       # Project dependencies
└── app.py                 # Main Flask application
```

## Dependencies
- Flask 2.3.3
- Requests 2.31.0
- NLTK 3.8.1
- NewsAPI Python 0.2.7
- Scikit-learn 1.3.0
- Pandas 2.0.3

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/SentimentAnalysisTool`)
3. Commit your changes (`git commit -m 'Add advanced sentiment scoring'`)
4. Push to the branch (`git push origin feature/SentimentAnalysisTool`)
5. Open a Pull Request

## Potential Improvements
- Add visualizations of sentiment trends
- Use a much better news api, since the News.org API is very general
- Create more detailed sentiment breakdowns
]

## Contact
Wesley Meredith - wmeredith777@gmail.com

Project Link: [https://github.com/wesleymeredith/financial-news-sentiment-analyzer]