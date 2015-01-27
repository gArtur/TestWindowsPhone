from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

__author__ = 'Artur'

class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    _search_box_locator = (By.ID, 'searchInput')
    _search_button_locator = (By.ID, 'searchButton')
    header_link_list = [
        {
            'locator': (By.CSS_SELECTOR, '#header a.phones'),
            'url_suffix': 'phones',
            'link_text': 'Telefony',
        },
        {
            'locator': (By.CSS_SELECTOR, '#header a.design'),
            'url_suffix': 'features',
            'link_text': 'Funkcje',
        },
        {
            'locator': (By.CSS_SELECTOR, '#header a.marketplace'),
            'url_suffix': 'store',
            'link_text': 'Aplikacje+Gry',
        },
        {
            'locator': (By.CSS_SELECTOR, '#header a.support'),
            'url_suffix': 'how-to/wp8',
            'link_text': 'Porady',
        },
    ]

    #Navigate to selected adress
    def go_to_page(self):
        self.driver.get(self.url)

    def link_url(self, locator):
        url = self.driver.find_element(*locator)
        return url.get_attribute('href')

    def link_title(self, locator):
        title = self.driver.find_element(*locator)
        return title.text

    def check_header_links(self):
        for link in self.header_link_list:
            url = self.link_url(link.get('locator'))
            title = self.link_title(link.get('locator'))
            assert (link.get('link_text')) in title
            assert (link.get('url_suffix')) in url

    #Searching with search box
    def search_in_page(self, text):
        search_box = self.driver.find_element(*self._search_box_locator)
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)
        assert 'Nie znaleziono odpowiednich aplikacji.' not in self.driver.page_source
        assert 'Nie znaleziono odpowiednich artykułów z poradami.' not in self.driver.page_source

    #Check page title
    def is_page_title_matches(self):
        assert self.page_title in self.driver.title