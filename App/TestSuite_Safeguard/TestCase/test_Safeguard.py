import unittest

from Public.Decorator import setupclass
from Public.Decorator import teardownclass
from Public.Decorator import setup
from Public.Decorator import teardown
from Public.Decorator import testcase

from App.PageObject.PlatformAppHomePage import PlatformAppHomePage
from App.PageObject.PlatformAppHomePage import back_to_app
from App.PageObject.SafeguardPage import SafeguardPage


class Safeguard(unittest.TestCase):
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.home_page = PlatformAppHomePage()

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        pass

    @setup
    def setUp(self):
        back_to_app()

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_App_Safeguard_Func_010(self):
        """保障"""
        self.home_page.click_safeguard()

        safeguard = SafeguardPage()
        self.assertTrue(safeguard.wait_page())
