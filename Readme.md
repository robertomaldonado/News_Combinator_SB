![Web Crawler Status](https://github.com/robertomaldonado/News_Combinator_SB/actions/workflows/python-app.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)

# News Combinator - Web Scrapper

## Using the application locally:

1. Create venv and install packages:

> python3 -m venv venv
> source venv/bin/activate
> pip3 install -r requirements.txt

2. To run the application locally please use:

> flask run --host 0.0.0.0 --port 8000

3. To read the news summary, open your favorite browser and navigate to:

> http://127.0.0.1:8000

4. Add the endpoints to the address:

- /all-news: To see them ordered by default, as the website has them.

- /filter-long-titles: Filter all entries with more than five words in the title ordered by the number of comments first.

- /filter-short-titles: Filter all entries with less than or equal to five words in the title ordered by points.

---

## Testing:

Automated testing added to the application with github-actions

Running tests for the application locally:

> pytest

---

## Documentation:

This project has been documented with Swagger for flask
To access please visit:

> http://127.0.0.1:8000/apidocs

---

## Deployed runnning app:

A copy of an earlier stage of the project was uploaded to Pythonanywhere

To see this app, please navigate to: http://robmaldo.pythonanywhere.com

---

## Technology stack used:

- Flask to generate the API
- Github actions to run tests on Github
- Pytest to run tests locally
- Swagger to document the endpoints
- Pythonanywhere to host an app working with a local file

---

### Solved prompt

Using the language that you feel most proficient in, create a web crawler using scraping techniques to extract the first 30 entries from https://news.ycombinator.com/. You'll only care about the number, the title, the points, and the number of comments for each entry.

From there, we want it to be able to perform a couple of filtering operations:

- Filter all previous entries with more than five words in the title ordered by the number of comments first.
- Filter all previous entries with less than or equal to five words in the title ordered by points.  
  When counting words, consider only the spaced words and exclude any symbols. For instance, the phrase “This is - a self-explained example” should be counted as having 5 words.

The solution should be designed for a web environment. The primary functionality and interaction should be accessible through a web browser.
