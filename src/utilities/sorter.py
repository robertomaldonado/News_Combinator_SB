from typing import List


def filter_title_by_longitude_and_sort_by_type(news_list: List[List[str]], filter_type: str) -> List[List[str]]:
  """Function sorts as specified by the customer"""
  tmp_filtered_list, tmp_count, sorted_list = list(), list(), list()
  indexed_item = 0

  if filter_type == "short":
    indexed_item = 2
  if filter_type == "long":
    indexed_item = 3

  # First filter longitude
  if filter_type == "short":
    for i in range(len(news_list)):
      curr_title = news_list[i][1]
      if len(curr_title.split(" ")) <= 5:
        tmp_filtered_list.append(news_list[i])
        tmp_count.append(int(news_list[i][indexed_item]))
  else:
    for i in range(len(news_list)):
      curr_title = news_list[i][1]
      if len(curr_title.split(" ")) > 5:
        tmp_filtered_list.append(news_list[i])
        tmp_count.append(int(news_list[i][indexed_item]))

  # Sort based on the values defined based on last steps array
  tmp_count = sorted(tmp_count)
  for num in tmp_count:
    for j in range(len(tmp_filtered_list)):
      if num == int(tmp_filtered_list[j][indexed_item]):
        sorted_list.append(tmp_filtered_list[j])
  return sorted_list
