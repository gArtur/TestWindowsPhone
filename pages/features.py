__author__ = 'Artur'

from pages.base import BasePage

class FeaturesPage(BasePage):
    url = "http://www.windowsphone.com/pl-pl/features"
    page_title = "Funkcje systemu Windows Phone (Polska)"
    header_link_list = BasePage.header_link_list
    footer_link_list = BasePage.footer_link_list