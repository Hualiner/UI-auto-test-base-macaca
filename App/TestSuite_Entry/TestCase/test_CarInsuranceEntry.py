import unittest

from Public.Decorator import setupclass
from Public.Decorator import teardownclass
from Public.Decorator import setup
from Public.Decorator import teardown
from Public.Decorator import testcase

from App.PageObject.PlatformAppHomePage import PlatformAppHomePage
from App.PageObject.PlatformAppHomePage import back_to_home_page
from App.PageObject.LoginPage import LoginPage
from App.PageObject.LoginPage import valid_login
from App.PageObject.PlatformAppMyPage import PlatformAppMyPage

from CarInsurance.PageObject.CarInsuranceHomePage import CarInsuranceHomePage
from CarInsurance.PageObject.MyCarInsurancePage import MyCarInsurancePage

from App.TestData.Account import VALID_ACCOUNT


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
        back_to_home_page()

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_Car_HomeEntry_Func_010(self):
        """车险首页入口验证"""
        self.home_page.click_car_insurance()

        car_insurance_home = CarInsuranceHomePage()
        self.assertTrue(car_insurance_home.wait_page())

    @testcase
    def test_Car_MyCarInsurEntry_Func_010(self):
        """我的车险入口验证"""
        self.home_page.click_my()

        login = LoginPage()
        if login.wait_page():
            valid_login(VALID_ACCOUNT.account(), VALID_ACCOUNT.password())

            if self.home_page.wait_page():
                self.home_page.click_my()

        my_page = PlatformAppMyPage()
        my_page.wait_page()
        my_page.click_my_car_insurance()

        my_car_insurance = MyCarInsurancePage()
        self.assertTrue(my_car_insurance.wait_page())
