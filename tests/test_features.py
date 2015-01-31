__author__ = 'Artur'

from selenium import webdriver
import unittest
from pages.features import FeaturesPage

class TestFeaturesPage(unittest.TestCase):
    def  setUp(self):
        self.driver = webdriver.Firefox()

    def test_check_page_title(self):
        featurespage = FeaturesPage(self.driver)
        featurespage.go_to_page()
        featurespage.is_page_title_matches()

    def test_check_header_links(self):
        featurespage = FeaturesPage(self.driver)
        featurespage.go_to_page()
        featurespage.check_links(FeaturesPage.header_link_list)

    def test_check_footer_links(self):
        featurespage = FeaturesPage(self.driver)
        featurespage.go_to_page()
        featurespage.check_links(FeaturesPage.footer_link_list)

    def test_check_dropdown_menu_links(self):
        featurespage = FeaturesPage(self.driver)
        featurespage.go_to_page()
        featurespage.mouse_click_element(FeaturesPage._explore_dropdown_menu)
        featurespage.check_links(FeaturesPage.explore_dropdown_link_list)

    def tearDown(self):
        self.driver.close()