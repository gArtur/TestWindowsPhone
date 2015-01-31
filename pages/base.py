from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unittestzero import Assert

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
            'url_suffix': '/phones',
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

    footer_link_list = [
        {
            'locator': (By.LINK_TEXT, 'Dla deweloperów'),
            'url_suffix': 'developer.windowsphone.com/',
            'link_text': 'Dla deweloperów',
        },
        {
            'locator': (By.LINK_TEXT, 'Dla firm'),
            'url_suffix': 'fwlink/?linkId=260887&clcid=0x415',
            'link_text': 'Dla firm',
        },
        {
            'locator': (By.LINK_TEXT, 'Praca'),
            'url_suffix': 'windowsphonecareers.com/',
            'link_text': 'Praca',
        },
        {
            'locator': (By.LINK_TEXT, 'Mapa witryny'),
            'url_suffix': 'sitemap',
            'link_text': 'Mapa witryny',
        },
        {
            'locator': (By.LINK_TEXT, 'Kontakt z nami'),
            'url_suffix': 'contact-us',
            'link_text': 'Kontakt z nami',
        },
        {
            'locator': (By.LINK_TEXT, 'Opinie'),
            'url_suffix': '#',
            'link_text': 'Opinie',
        },
        {
            'locator': (By.LINK_TEXT, 'Prywatność i pliki cookie'),
            'url_suffix': 'fwlink/?linkId=248681&clcid=0x415',
            'link_text': 'Prywatność i pliki cookie',
        },
        {
            'locator': (By.LINK_TEXT, 'Warunki korzystania'),
            'url_suffix': 'fwlink/?linkId=123158&clcid=0x415',
            'link_text': 'Warunki korzystania',
        },
        {
            'locator': (By.LINK_TEXT, 'Znaki towarowe'),
            'url_suffix': '?linkId=4412893&clcid=0x415',
            'link_text': 'Znaki towarowe',
        },
        {
            'locator': (By.LINK_TEXT, 'Polska (polski)'),
            'url_suffix': 'markets',
            'link_text': 'Polska (polski)',
        },
    ]

    _explore_dropdown_menu = (By.ID, 'exploreTitle')

    #Navigate to selected adress
    def go_to_page(self):
        self.driver.get(self.url)

    def link_url(self, locator):
        url = self.driver.find_element(*locator)
        return url.get_attribute('href')

    def link_title(self, locator):
        title = self.driver.find_element(*locator)
        return title.text

    def mouse_click_element(self, element):
        self.driver.find_element(*element).click()

    #Check if links url and title are corect
    def check_links(self, link_list):
        bad_urls = []
        bad_titles = []
        for link in link_list:
            url = self.link_url(link.get('locator'))
            title = self.link_title(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_urls.append('%s don\'t end with %s' % (url, link.get('url_suffix')))
            if not title == link.get('link_text'):
                bad_titles.append('%s don\'t equal %s' % (title, link.get('link_text')))
        Assert.equal(0, len(bad_urls), '%s bad url\'s found: ' % len(bad_urls) + ', '.join(bad_urls))
        Assert.equal(0, len(bad_titles), '%s bad title\'s found: ' % len(bad_titles) + ', '.join(bad_titles))

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