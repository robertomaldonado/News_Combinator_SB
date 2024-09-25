from flask import Flask
import src.driver
app = Flask(__name__)


@app.route("/")
def home():
  return "<p>App running...</p>"


@app.route("/news_list")
def get_news():
  return src.driver.main()


if __name__ == "__main__":
  app.run(debug=True)
