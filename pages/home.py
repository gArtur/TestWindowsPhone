__author__ = 'Artur'

from pages.base import BasePage

class HomePage(BasePage):
    url = "http://www.windowsphone.com/pl-pl/"
    page_title = "Smartfon wynaleziony na nowo z myślą o Tobie | Windows Phone (Polska)"
    header_link_list = BasePage.header_link_list
    footer_link_list = BasePage.footer_link_list