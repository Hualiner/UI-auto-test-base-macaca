from macaca import WebDriverException

from Public.PageObject.BasePage import BasePage

from Public.Decorator import teststep


class PlatformAppHomePopupPage(BasePage):
    @teststep
    def wait_page(self):
        """以首页POPUP的关闭按钮的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id('com.platform.jhj:id/main_popup_close_adimg')
            return True
        except WebDriverException:
            return False

    @teststep
    def close(self):
        """以首页POPUP的关闭按钮的ID为依据"""
        self.driver\
            .element_by_id('com.platform.jhj:id/main_popup_close_adimg')\
            .click()
