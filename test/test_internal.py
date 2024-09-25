import src.web_crawler


# Test 1. Test the data type returned matches expected type


def test_get_all_simulation_ts():
  single_crawl = src.web_crawler.do_basic_crawl()
  assert type(single_crawl) is list, "Returned crawled data should be a list"
