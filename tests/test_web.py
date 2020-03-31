import pytest
from selenium.webdriver import Chrome

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_basic_duckduckgo_search(browser):
    PHRASE = 'panda'

    search_input = DuckDuckGoSearchPage(browser)
    search_input.load()
    search_input.search(PHRASE)

    search_result = DuckDuckGoResultPage(browser)

    assert search_result.link_div_count() > 0
    assert search_result.search_input_value() == PHRASE
    assert search_result.phrase_result_count(PHRASE) > 0


def test_duckduckgo_search_tiger(browser):
    PHRASE = 'tiger'

    search_input = DuckDuckGoSearchPage(browser)
    search_input.load()
    search_input.search(PHRASE)

    search_result = DuckDuckGoResultPage(browser)

    assert search_result.link_div_count() > 0
    assert search_result.search_input_value() == PHRASE
    assert search_result.phrase_result_count(PHRASE) > 0


def test_duckduckgo_search_click_link(browser):
    PHRASE = 'panda'

    search_input = DuckDuckGoSearchPage(browser)
    search_input.load()
    search_input.search(PHRASE)

    search_result = DuckDuckGoResultPage(browser)

    assert search_result.link_div_count() > 0
    assert search_result.search_input_value() == PHRASE
    assert search_result.phrase_result_count(PHRASE) > 0

    search_input.click_link()

    assert search_result.get_page_title('Panda Chinese Restaurant')
