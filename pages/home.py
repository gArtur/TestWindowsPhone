from selenium.webdriver.common.by import By

__author__ = 'Artur'

from pages.base import BasePage

class HomePage(BasePage):
    url = "http://www.windowsphone.com/pl-pl/"
    page_title = "Smartfon wynaleziony na nowo z myślą o Tobie | Windows Phone (Polska)"
    home_page_link_list = [
        {
            'locator': (By.LINK_TEXT, 'Znajdź telefon dla siebie'),
            'url_suffix': '/phones',
            'link_text': 'Znajdź telefon dla siebie',
        },
        {
            'locator': (By.LINK_TEXT, 'Dowiedz się, jak'),
            'url_suffix': 'how-to/wp8/moving-to-windows-phone',
            'link_text': 'Dowiedz się, jak',
        },
        {
            'locator': (By.LINK_TEXT, 'Zacznij poszukiwania'),
            'url_suffix': '/Store',
            'link_text': 'Zacznij poszukiwania',
        },
        {
            'locator': (By.LINK_TEXT, 'Więcej informacji'),
            'url_suffix': 'how-to/wp8/start/add-ringtones-to-my-phone',
            'link_text': 'Więcej informacji',
        },
        {
            'locator': (By.LINK_TEXT, 'Zobacz, jakie nowości będą dostępne w wersji Windows Phone 8.1'),
            'url_suffix': '',
            'link_text': 'Zobacz, jakie nowości będą dostępne w wersji Windows Phone 8.1',
        },
    ]