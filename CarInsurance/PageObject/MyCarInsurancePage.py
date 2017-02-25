from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep


class MyCarInsurancePage(BasePage):
    @teststep
    def wait_page(self):
        """以“我的车辆”的XPATH为依据"""
        try:
            self.driver\
                .wait_for_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                                           '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                                           '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                                           '/android.view.ViewGroup[1]/android.webkit.WebView[1]'
                                           '/android.webkit.WebView[1]/android.view.View[12]')
            return True
        except WebDriverException:
            return False
