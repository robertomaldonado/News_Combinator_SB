![Web Crawler Status](https://github.com/robertomaldonado/News_Combinator_SB/actions/workflows/python-app.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)

# News Combinator

This project aims to solve the given prompt.

Using the application locally:

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

Automated testing added to the application with github-actions

Running tests for the application locally:

> pytest

# Prompt

From there, we want it to be able to perform a couple of filtering operations:

Filter all previous entries with more than five words in the title ordered by the number of comments first.  
Filter all previous entries with less than or equal to five words in the title ordered by points.  
When counting words, consider only the spaced words and exclude any symbols. For instance, the phrase “This is - a self-explained example” should be counted as having 5 words.

The solution should be designed for a web environment. The primary functionality and interaction should be accessible through a web browser.

We will measure the performance of the provided solution and your ability to test the requested operations in the scenarios described above. In addition, we'd love to see the following in your code for extra points:

- Good object-oriented/functional code, avoiding repetition and favoring a consistent organization. You should stick to the semantics of your chosen language and be as consistent as possible.
- Correct usage of version control tools, with a good commit history and incremental software delivery practices.
- Automated testing with any framework or tool of your choice.
- We value candidates who love clean, well-structured code and who can creatively solve problems.
- A ReadMe is always helpful to guide us through your work.
