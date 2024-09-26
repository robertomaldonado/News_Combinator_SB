import re
from typing import List
from urllib.request import urlopen
from src.utilities.sorter import *


class WebCrawler:
  raw_news = None

  def __init__(self) -> None:
    self.news_list = None
    self.filtered_list = None

  @staticmethod
  def retrieve_values(pattern: str, news_sections: List[str]) -> List[str]:
    tmp_list = list()
    for i in range(len(news_sections)):
      match_results = re.search(pattern, news_sections[i])
      if match_results == None:
        tmp_list.append("0")
      else:
        tmp = re.sub("<.*?>", "", match_results.group())
        tmp_list.append(tmp)
    return tmp_list

  @staticmethod
  def retrieve_titles(news_sections: List[str]) -> List[str]:
    tmp_list = list()
    any_text_pattern = r">([^<>]*)<"
    for i in range(len(news_sections)):
      tmp = re.findall(any_text_pattern, news_sections[i])
      tmp_list.append(tmp[13])
    return tmp_list

    # Create a partial list with the needed content
  def scrap_partial_data(self) -> List[List[str]]:
      # Retrieve news from the specified website
    url = "https://news.ycombinator.com"
    try:
      page = urlopen(url)
      html = page.read().decode("utf-8")
    except:
      print("Cannot retrieve with url, switching to local file")
      with open("local_file.txt", 'r') as filename:
        html = filename.readlines()
      html = "".join(html)

    news_sections = list()
    for i in range(1, 30):
      news_start = html.find(f'<span class="rank">{i}.</span>')
      news_end = html.find(f'<span class="rank">{i+1}.</span>')
      section = html[news_start:news_end]
      news_sections.append(section)
    else:
      news_start = html.find(f'<span class="rank">{30}.</span>')
      news_end = html.find(f"rel='next'>More</a>")
      section = html[news_start:news_end]
      news_sections.append(section)
    return news_sections

  def set_news_list(self) -> None:
    news_sections = self.scrap_partial_data()
    id_pattern = "[1-9]?[0-9]\\."
    points_pattern = "[0-9]?[0-9]?[0-9]?[0-9] point"
    comments_pattern = "[0-9]?[0-9]?[0-9]\\&nbsp\\;comment"

    id_list = self.retrieve_values(id_pattern, news_sections)
    points_list = self.retrieve_values(points_pattern, news_sections)
    comments_list = self.retrieve_values(comments_pattern, news_sections)
    titles_list = self.retrieve_titles(news_sections)

    news_list = list()
    for i in range(len(news_sections)):
      # Check for empty data, we have seen this issue in the website. Otherwise skip it
      if titles_list[i] == "" or points_list[i] == "" or comments_list[i] == "" or id_list[i] == "":
        continue
      news_list.append([id_list[i][:-1], titles_list[i],
                        points_list[i][:-len(" point")], comments_list[i][:-len("&nbsp;comment")]])
    self.news_list = news_list

  def filter_long_title_sort_by_comments(self) -> List[List[str]]:
    sorted_list = filter_title_by_longitude_and_sort_by_type(
        self.news_list, "long")
    self.filtered_list = sorted_list[:]  # Pass a copy, not the ref

  def filter_short_title_sort_by_points(self) -> List[List[str]]:
    sorted_list = filter_title_by_longitude_and_sort_by_type(
        self.news_list, "short")
    self.filtered_list = sorted_list[:]   # Pass a copy, not the ref
