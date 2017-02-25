from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep


class InsuranceHomePage(BasePage):
    @teststep
    def wait_page(self):
        """以保险首页Title中的“金惠家保险”的ID为依据，并通过ELEMENT的TEXT属性进行辅助验证"""
        try:
            element = self.driver \
                .wait_for_element_by_id('com.platform.jhj:id/title_text')

            if element.text == '金惠家保险':
                return True
            else:
                return False
        except WebDriverException:
            return False
