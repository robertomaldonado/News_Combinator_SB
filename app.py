from flask import Flask
import src.web_crawler
app = Flask(__name__)


@app.route("/")
def home():
  return "<p>App running...</p>"


@app.route("/news_list")
def get_news():
  return src.web_crawler.do_basic_crawl()


if __name__ == "__main__":
  app.run(debug=True)
