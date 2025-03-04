from flask import Flask, render_template, request
from scraper.news_api import NewsAPI
from analyzer.sentiment import SentimentAnalyzer

'''
We are going to use news.org's API for this project, maybe in the future we 
can use other APIs that are more accurate and tailored towards just financial news
'''

app = Flask(__name__)

news_api = NewsAPI()
sentiment_analyzer = SentimentAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        articles = news_api.get_financial_news(ticker)
        analyzed_articles = sentiment_analyzer.analyze_articles(articles)

        return render_template("results.html", articles=analyzed_articles, ticker=ticker)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
