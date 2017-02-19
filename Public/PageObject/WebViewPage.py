from macaca import WebDriverException

from Public.PageObject.BasePage import BasePage

from Public.Decorator import teststep


class WebViewPage(BasePage):
    @teststep
    def wait_page(self):
        """以WebView中“返回”Button的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id('com.platform.jhj:id/title_button_text')
            return True
        except WebDriverException:
            return False

    @teststep
    def back(self):
        """以WebView中“返回”Button的ID为依据"""
        self.driver\
            .wait_for_element_by_id('com.platform.jhj:id/title_button_text')\
            .click()
