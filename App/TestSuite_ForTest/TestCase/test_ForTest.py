import unittest

from Public.Decorator import setupclass
from Public.Decorator import teardownclass
from Public.Decorator import setup
from Public.Decorator import teardown
from Public.Decorator import testcase

from App.PageObject.PlatformAppHomePage import PlatformAppHomePage
from App.PageObject.PlatformAppHomePage import back_to_home_page


class ForTest(unittest.TestCase):
    @classmethod
    @setupclass
    def setUpClass(cls):
        """public variable in every case"""
        cls.home_page = PlatformAppHomePage()

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        pass

    @setup
    def setUp(self):
        """in order to ensure on the home page for every case"""
        back_to_home_page()

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_For_Test(self):
        """For Test"""
        self.home_page.for_test()

