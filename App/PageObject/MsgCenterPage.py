from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep


class MsgCenterPage(BasePage):
    @teststep
    def wait_page(self):
        """以“消息中心”Title的中文名为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('消息中心')
            return True
        except WebDriverException:
            return False
