import time

from Public.PageObject.BasePage import BasePage
from Public.PageObject.PlatformAppHomePage import PlatformAppHomePage

from Public.Decorator import teststep
from Public.Decorator import testcase


class WizardPage(BasePage):
    @teststep
    def wait_page(self):
        self.driver \
            .wait_for_element_by_class_name('android.widget.FrameLayout')

    @teststep
    def skip(self):
        rect = self.driver \
            .element_by_class_name('android.widget.FrameLayout') \
            .rect

        y = rect['height']/2
        x = rect['width']/2
        for i in range(3):
            self.driver \
                .touch('drag', {'fromX': x, 'fromY': y, 'toX': 0, 'toY': y, 'steps': 5})

            time.sleep(1)

        self.driver \
            .element_by_class_name('android.widget.FrameLayout').click()


@testcase
def skip_wizard_to_home():
    wizard = WizardPage()
    wizard.wait_page()
    wizard.skip()

    home_page = PlatformAppHomePage()
    if home_page.wait_popup():
        home_page.close_popup()

    if home_page.wait_page():
        return True
    else:
        return False
