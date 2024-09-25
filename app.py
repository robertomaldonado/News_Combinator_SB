from flask import Flask
from src.WebCrawler import WebCrawler

app = Flask(__name__)


@app.route("/")
def home():
  return "<p>App running...</p>"


@app.route("/news_list")
def get_news():
  my_crawler.set_news_list()
  return my_crawler.news_list


if __name__ == "__main__":
  my_crawler = WebCrawler()
  app.run(debug=True)
