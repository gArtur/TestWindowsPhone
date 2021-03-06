__author__ = 'Artur'

from selenium import webdriver
import unittest
from pages.home import HomePage
from pages.base import BasePage

class TestHomePage(unittest.TestCase):
    def  setUp(self):
        self.driver = webdriver.Firefox()

    def test_check_page_title(self):
        homepage = HomePage(self.driver)
        homepage.go_to_page()
        homepage.is_page_title_matches()

    def test_check_home_page_links(self):
        homepage = HomePage(self.driver)
        homepage.go_to_page()
        homepage.check_links(HomePage.home_page_link_list)

    def test_check_header_links(self):
        homepage = HomePage(self.driver)
        homepage.go_to_page()
        homepage.check_links(BasePage.header_link_list)

    def test_check_footer_links(self):
        homepage = HomePage(self.driver)
        homepage.go_to_page()
        homepage.check_links(BasePage.footer_link_list)

    def test_search(self):
        homepage = HomePage(self.driver)
        homepage.go_to_page()
        homepage.search_in_page('Lumia')

    def tearDown(self):
        self.driver.close()