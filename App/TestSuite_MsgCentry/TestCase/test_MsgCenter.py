import unittest

from Public.Decorator import setupclass
from Public.Decorator import teardownclass
from Public.Decorator import setup
from Public.Decorator import teardown
from Public.Decorator import testcase

from App.PageObject.PlatformAppHomePage import PlatformAppHomePage
from App.PageObject.PlatformAppHomePage import back_to_home_page
from App.PageObject.MsgCenterPage import MsgCenterPage
from App.PageObject.LoginPage import LoginPage
from App.PageObject.LoginPage import valid_login

from App.TestData.Account import VALID_ACCOUNT


class MsgCenter(unittest.TestCase):
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
        back_to_home_page()

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_App_MsgCenterEntry_Func_010(self):
        """消息中心入口验证"""
        self.home_page.click_msg()

        login = LoginPage()
        if login.wait_page():
            valid_login(VALID_ACCOUNT.account(), VALID_ACCOUNT.password())

            if self.home_page.wait_page():
                self.home_page.click_msg()

        msg = MsgCenterPage()
        self.assertTrue(msg.wait_page())



