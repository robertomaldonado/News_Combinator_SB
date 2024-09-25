"""
Create a web crawler using scraping techniques to extract the first 30 entries from https://news.ycombinator.com/.
Store: Number, the title, the points, and the number of comments for each entry.
"""
from typing import List
from urllib.request import urlopen
import re


def main():
  # url = "https://news.ycombinator.com"
  # page = urlopen(url)
  # html = page.read().decode("utf-8")

  sections = []
  with open("testfile.txt", 'r') as filename:
    html = filename.readlines()
  html = "".join(html)

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

  id_pattern = "[1-9]?[0-9]\\."
  points_pattern = "[0-9]?[0-9]?[0-9]?[0-9] point"
  comments_pattern = "[0-9]?[0-9]?[0-9]\\&nbsp\\;comment"
  id_list = retrieve_values(id_pattern, sections)
  points_list = retrieve_values(points_pattern, sections)
  comments_list = retrieve_values(comments_pattern, sections)
  titles_list = retrieve_titles(sections)

  news_list = list()
  for i in range(len(sections)):
    news_list.append([id_list[i], titles_list[i],
                      points_list[i], comments_list[i]])
  print(news_list)


if __name__ == '__main__':
  main()
