from flask import Flask
from src.WebCrawler import WebCrawler

app = Flask(__name__)
my_crawler = WebCrawler()


@app.route("/")
def home():
  my_crawler.set_news_list()
  return "<p>App running...</p>"


@app.route("/all-news")
def all_news():
  return my_crawler.news_list


@app.route("/filter-long-titles")
def filter_long():
  my_crawler.filter_long_title_sort_by_comments()
  return my_crawler.filtered_list


@app.route("/filter-short-titles")
def filter_short():
  my_crawler.filter_short_title_sort_by_points()
  return my_crawler.filtered_list


if __name__ == "__main__":
  app.run(debug=True)
