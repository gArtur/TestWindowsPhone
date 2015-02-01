from selenium.webdriver.common.by import By

__author__ = 'Artur'

from pages.base import BasePage

class FeaturesPage(BasePage):
    url = "http://www.windowsphone.com/pl-pl/features"
    page_title = "Funkcje systemu Windows Phone (Polska)"
    explore_dropdown_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'a#signin'),
            'url_suffix': 'ffeatures',
            'link_text': 'Zaloguj się',
        },
        {
            'locator': (By.CSS_SELECTOR, 'a#myPhone'),
            'url_suffix': '/my',
            'link_text': 'Mój telefon',
        },
        {
            'locator': (By.CSS_SELECTOR, 'a#findMyPhone'),
            'url_suffix': '/my/find',
            'link_text': 'Znajdź mój telefon',
        },
        {
            'locator': (By.CSS_SELECTOR, 'a#purchases'),
            'url_suffix': '/my/purchase-history',
            'link_text': 'Historia zakupów',
        },
        {
            'locator': (By.CSS_SELECTOR, 'a#myFamily'),
            'url_suffix': '/family',
            'link_text': 'Moja rodzina',
        },
    ]
