from Public.BasePage import BasePage
from Public.Decorator import teststep


class SafeguardPage(BasePage):
    @teststep
    def wait_page(self):
        if self.wait_string_use_and('三泰控股', '金投金融'):
            return True
        else:
            return False
