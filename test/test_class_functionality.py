from src.WebCrawler import WebCrawler


# Test 1. Test the data type returned matches expected type


def test_list_returned():
  test_crawler = WebCrawler()
  test_crawler.set_news_list()
  values = test_crawler.news_list
  assert type(values) is list, "Returned crawled data should be a list"


# Test 2. Test the number od items in a


def test_items_in_sublist():
  test_crawler = WebCrawler()
  test_crawler.set_news_list()
  values = test_crawler.news_list
  assert len(values[1]) == 4, "Returned sub-list should have 4 items"

# Test 3. Test the data types returned matches expected type


def test_items_data_types_in_sublist():
  test_crawler = WebCrawler()
  test_crawler.set_news_list()
  values = test_crawler.news_list
  assert type(values[1][0]) is str, "First field should be str"
  assert type(values[2][1]) is str, "Second field should be str"
  assert type(values[3][2]) is str, "Third field should be str"
  assert type(values[4][3]) is str, "Fourth field should be str"

#  Test 4. Test the data types returned matches expected type


def test_empty_initial_news_list():
  test_crawler = WebCrawler()
  empty_values = test_crawler.news_list
  assert empty_values is None, "Initial news_list should be None"


#  Test 5. Test data gets filled after calling .set_news_list method


def test_news_list_gets_populated():
  test_crawler = WebCrawler()
  values = test_crawler.news_list
  assert values is None, "Initial news_list should be None"
  test_crawler.set_news_list()
  values = test_crawler.news_list
  assert len(
      values) > 0, "Once a list is created, it should have items in the list"

#  Test 6. Test the data types returned matches expected type


def test_empty_initial_filtered_list():
  test_crawler = WebCrawler()
  empty_values = test_crawler.filtered_list
  assert empty_values is None, "Initial filtered_list should be None"


#  Test 7. Test data gets filled after calling filter_long_title_sort_by_comments method


def test_filtered_long_list_gets_populated():
  test_crawler = WebCrawler()
  values = test_crawler.filtered_list
  assert values is None, "Initial filtered_list should be None"
  test_crawler.set_news_list()
  test_crawler.filter_long_title_sort_by_comments()
  values = test_crawler.filtered_list
  assert len(
      values) > 0, "Once a list is filtered, it should have items in the list"

#  Test 8. Test data gets filled after calling filter_short_title_sort_by_points method


def test_filtered_short_list_gets_populated():
  test_crawler = WebCrawler()
  values = test_crawler.filtered_list
  assert values is None, "Initial filtered_list should be None"
  test_crawler.set_news_list()
  test_crawler.filter_short_title_sort_by_points()
  values = test_crawler.filtered_list
  assert len(
      values) > 0, "Once a list is filtered, it should have items in the list"
