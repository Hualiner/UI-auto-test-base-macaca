import time
import unittest

from Public.Decorator import setupclass
from Public.Decorator import teardownclass
from Public.Decorator import setup
from Public.Decorator import teardown
from Public.Decorator import testcase

from Public.PageObject.PlatformAppHomePage import PlatformAppHomePage
from Public.PageObject.WebViewPage import WebViewPage
from Public.PageObject.LoginPage import LoginPage
from Public.PageObject.GesturePasswordPage import GesturePasswordPage
from Public.PageObject.PlatformAppMyPage import PlatformAppMyPage

from CarInsurance.PageObject.CarInsuranceHomePage import CarInsuranceHomePage
from CarInsurance.PageObject.MyCarInsurancePage import MyCarInsurancePage

from CarInsurance.TestData.Account import VALID_ACCOUNT


class CarInsuranceEntry(unittest.TestCase):
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
        if not self.home_page.wait_page():
            web_view = WebViewPage()
            if web_view.wait_page():
                web_view.back()
                self.home_page.wait_page()

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_Car_HomeEntry_Func_010(self):
        """车险首页入口验证"""
        self.home_page.click_jhj()      # in order to ensure on the jhj page
        time.sleep(0.5)     # this sleep is necessary, if not, something wrong will happen
        self.home_page.click_car_insurance()

        car_insurance_home = CarInsuranceHomePage()
        self.assertTrue(car_insurance_home.wait_page())

    @testcase
    def test_Car_MyCarInsurEntry_Func_010(self):
        """我的车险入口验证"""
        self.home_page.click_my()

        login = LoginPage()
        if login.wait_page():
            login.input_account(VALID_ACCOUNT.account())
            login.input_password(VALID_ACCOUNT.password())
            login.login()

            gesture = GesturePasswordPage()
            if gesture.wait_page():
                gesture.skip()

            if self.home_page.wait_page():
                self.home_page.click_my()

        my_page = PlatformAppMyPage()
        my_page.wait_page()
        my_page.click_my_car_insurance()

        my_car_insurance = MyCarInsurancePage()
        self.assertTrue(my_car_insurance.wait_page())

    # def test_case1(self):
    #     x = 1
    #     print('x:', x)
    #     self.assertEqual(x, 1)
    #
    # def test_case2(self):
    #     x = 2
    #     print('x:', x)
    #     self.assertEqual(x, 1)
    #
    # def test_case3(self):
    #     x = 2/0
    #     print('x:', x)
    #     self.assertEqual(x, 1)
