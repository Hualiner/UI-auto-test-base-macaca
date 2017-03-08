from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep


class InviteFriendsPage(BasePage):
    @teststep
    def wait_page(self):
        if self.wait_string_use_and('福利', '活动规则'):
            return True
        else:
            return False

    @teststep
    def wait_back(self, timeout=10000):
        try:
            self.driver.wait_for_element_by_id('com.platform.jhj:id/back_btn', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def back(self):
        self.driver.element_by_id('com.platform.jhj:id/back_btn').click()
