from flask import Flask
from flasgger import Swagger
from src.WebCrawler import WebCrawler

app = Flask(__name__)
swagger = Swagger(app)
my_crawler = WebCrawler()


@app.route("/")
def home():
  """
  ---
  responses:
    200:
      description: A short menu, displaying the three available endpoints
  """
  my_crawler.set_news_list()
  return "<h2>Welcome to News Web Scrapper</h2>Usable endpoints:<p>/all-news</p><p>/filter-long-titles</p><p>/filter-short-titles</p>"


@app.route("/all-news")
def all_news():
  """
  ---
  responses:
    200:
      description: A complete list for the first 30 news in the website https://news.ycombinator.com
  """
  return my_crawler.news_list


@app.route("/filter-long-titles")
def filter_long():
  """
  ---
  responses:
    200:
      description: Filter all entries with more than five words in the title ordered by the number of comments first
  """
  my_crawler.filter_long_title_sort_by_comments()
  return my_crawler.filtered_list


@app.route("/filter-short-titles")
def filter_short():
  """
  ---
  responses:
    200:
      description: Filter all entries with less than or equal to five words in the title ordered by points
      schema:
      examples:
        sorted_filtered_list = [["10","Title","12","10"],["4","Title","15","9"]]
  """
  my_crawler.filter_short_title_sort_by_points()
  return my_crawler.filtered_list


if __name__ == "__main__":
  app.run(debug=True)
