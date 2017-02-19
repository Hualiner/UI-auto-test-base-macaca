from macaca import WebDriverException

from Public.PageObject.BasePage import BasePage

from Public.Decorator import teststep


class PlatformAppMyPage(BasePage):
    @teststep
    def wait_page(self):
        """以用户信息中心SETTINGS的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id('com.platform.jhj:id/iv_settings')
            return True
        except WebDriverException:
            return False

    @teststep
    def click_my_car_insurance(self):
        """以“我的车险”的TEXT为依据"""
        self.driver\
            .element_by_name('我的车险')\
            .click()

    @teststep
    def click_my_insurance(self):
        """以“我的保险”的TEXT为依据"""
        self.driver\
            .element_by_name('我的保险')\
            .click()

    @teststep
    def click_settings(self):
        """以用户信息中心SETTINGS的ID为依据"""
        self.driver\
            .element_by_id('com.platform.jhj:id/iv_settings')\
            .click()


