import pytest
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then


@scenario('search.feature', 'Doing a google search')
def test_search(browser):
    pass

@scenario('search.feature', 'Doing a google calculator search')
def test_calculator_search(browser):
    pass

@given('I opened google')
def open_page(browser, query):
    """
    Enter data into the google search box
    """
    browser.visit('https://www.google.com/')

@given('I search for <query>')
def enter_data(browser, query):
    """
    Enter data into the google search box
    """

    search_box_xpath = '//form//input[@type="text"]'
    browser.find_by_xpath(search_box_xpath).type(query)

@given('I hit enter')
def submit_data(browser):
    """
    Submits the google search query
    """

    search_box_xpath = '//form//input[@type="text"]'
    browser.find_by_xpath(search_box_xpath).type(Keys.RETURN)

@then('The query <query> appears in the url')
def assert_query_in_url(browser, query):
    """
    Assert the query is in the current url
    """

    assert ('q=' + query) in browser.url

@then('The answer <answer> appears in the url')
def assert_answer_in_page(browser, answer):
    """
    Assert the answer is in the current page
    """

    assert answer == browser.find_by_xpath('//span[@class="cwcot"]').value
