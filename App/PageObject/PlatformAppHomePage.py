import time

from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps

from App.PageObject.WebViewPage import WebViewPage


class PlatformAppHomePage(BasePage):
    @teststep
    def wait_page(self):
        """以“消息图标”的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id('com.platform.jhj:id/home_msg_btn')
            return True
        except WebDriverException:
            return False

    @teststep
    def click_msg(self):
        """以“消息图标”的ID为依据"""
        self.driver\
            .element_by_id('com.platform.jhj:id/home_msg_btn')\
            .click()

    @teststep
    def click_car_insurance(self):
        """点击“车险”Icon的中文字体上方（高出中文字体上边界2倍中文字体的高度）"""
        element = self.driver.element_by_name('车险')
        self.click_above_of_element(element, rate=2)

    @teststep
    def click_insurance(self):
        """点击“保险”Icon的中文字体上方（高出中文字体上边界2倍中文字体的高度）"""
        element = self.driver.element_by_name('保险')
        self.click_above_of_element(element, rate=2)

    @teststep
    def click_jhj(self):
        """以“金惠家”Tab的中文名称的XPATH为依据"""
        self.driver \
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]'
                              '/android.widget.TextView[1]')\
            .click()

    @teststep
    def click_discover(self):
        """以“发现”Tab的中文名称的XPATH为依据"""
        self.driver \
            .elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]'
                               '/android.widget.TextView[1]') \
            .click()

    @teststep
    def click_safeguard(self):
        """以“保障”Tab的中文名称的XPATH为依据"""
        self.driver \
            .elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]'
                               '/android.widget.TextView[1]') \
            .click()

    @teststep
    def click_my(self):
        """以“我的”Tab的中文名称的XPATH为依据"""
        self.driver\
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]'
                              '/android.widget.TextView[1]')\
            .click()

    @teststep
    def click_finance_choiceness_more(self):
        """以“理财精选”对应的“更多”的ID为依据"""
        self.find_element_on_vertical('id', 'com.platform.jhj:id/home_welfare_more_tv').click()

    @teststep
    def click_hot_insurance_more(self):
        """以“热卖保险”对应的“更多”的ID为依据"""
        self.find_element_on_vertical('id', 'com.platform.jhj:id/home_fm_insurance_more_tv').click()

    @teststep
    def for_test(self):
        """仅用于测试"""
        pass


@teststeps
def back_to_home_page():
    """返回App首页，以“消息图标”的ID为依据"""
    home_page = PlatformAppHomePage()
    if not home_page.wait_page():
        web_view = WebViewPage()
        if web_view.wait_page():
            web_view.back()
        if not home_page.wait_page():
            home_page.click_jhj()
            if not home_page.wait_page():
                home_page.find_element_by_swipe_down('id', 'com.platform.jhj:id/home_msg_btn')
