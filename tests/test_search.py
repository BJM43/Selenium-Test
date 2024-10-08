# coding=utf-8
import pytest
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = SearchPage(self.driver, self.wait)
        self.page.go_to_search_page()

    def test_login_fail(self, load_pages):
        self.page.make_a_login_fail("fakeuser@itla.edu.do", "20186927")

    def test_login_pass(self, load_pages):
        self.page.make_a_login_pass("20060211@itla.edu.do", "123456")
