"""
Create a web crawler using scraping techniques to extract the first 30 entries from https://news.ycombinator.com/.
Store: Number, the title, the points, and the number of comments for each entry.
"""
from typing import List
import re


def main():
  # Retrieve news from the specified website
  # url = "https://news.ycombinator.com"
  # page = urlopen(url)
  # html = page.read().decode("utf-8")

  # Code to test locally (limited access to internet)
  with open("local_file.txt", 'r') as filename:
    html = filename.readlines()
  html = "".join(html)

  # Create a partial list with the needed content
  sections = list()
  for i in range(1, 30):
    news_start = html.find(f'<span class="rank">{i}.</span>')
    news_end = html.find(f'<span class="rank">{i+1}.</span>')
    section = html[news_start:news_end]
    sections.append(section)
  else:
    news_start = html.find(f'<span class="rank">{30}.</span>')
    news_end = html.find(f"rel='next'>More</a>")
    section = html[news_start:news_end]
    sections.append(section)

  def retrieve_values(pattern: str, sections: List[str]) -> List[str]:
    tmp_list = list()
    for i in range(len(sections)):
      match_results = None
      match_results = re.search(pattern, sections[i])
      t = match_results.group()
      t = re.sub("<.*?>", "", t)
      tmp_list.append(t)
    return tmp_list

  def retrieve_titles(sections: List[str]) -> List[str]:
    tmp_list = list()
    any_text_pattern = r">([^<>]*)<"
    for i in range(len(sections)):
      t = re.findall(any_text_pattern, sections[i])
      tmp_list.append(t[13])
    return tmp_list

  def get_news_list():
    """ In this section we use both approaches:
    - Using the pattern
    - Titles retrieves from the position after using regex findall
    """
    # Define patterns to be used
    id_pattern = "[1-9]?[0-9]\\."
    points_pattern = "[0-9]?[0-9]?[0-9]?[0-9] point"
    comments_pattern = "[0-9]?[0-9]?[0-9]\\&nbsp\\;comment"
    # Use patterns to retrieve the values we seek
    id_list = retrieve_values(id_pattern, sections)
    points_list = retrieve_values(points_pattern, sections)
    comments_list = retrieve_values(comments_pattern, sections)
    # Find titles in the html section
    titles_list = retrieve_titles(sections)

    # Build the resulting list
    news_list = list()
    for i in range(len(sections)):
      news_list.append([id_list[i][:-1], titles_list[i],
                        points_list[i][:-len(" point")], comments_list[i][:-len("&nbsp;comment")]])
    return news_list

  return get_news_list()


if __name__ == '__main__':
  main()
