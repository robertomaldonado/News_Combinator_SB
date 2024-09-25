from src.WebCrawler import WebCrawler


# Test 1. Test the data type returned matches expected type


def test_get_all_simulation_ts():
  test_crawler = WebCrawler()
  test_crawler.set_news_list()
  values = test_crawler.news_list
  assert type(values) is list, "Returned crawled data should be a list"
