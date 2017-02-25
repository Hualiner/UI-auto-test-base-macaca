import time

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import testcase

from App.PageObject.PlatformAppHomePage import PlatformAppHomePage
from App.PageObject.PlatformAppHomePopupPage import PlatformAppHomePopupPage


class WizardPage(BasePage):
    @teststep
    def wait_page(self):
        """以Wizard中图片的class name为依据"""
        self.driver \
            .wait_for_element_by_class_name('android.widget.FrameLayout')

    @teststep
    def skip(self):
        """以Wizard中图片的class name为依据"""
        for i in range(3):
            self.swipe_left(steps=5)

            time.sleep(1)

        self.driver \
            .element_by_class_name('android.widget.FrameLayout').click()


@testcase
def skip_wizard_to_home():
    """在App启动页面，跳过Wizard进入到App首页"""
    wizard = WizardPage()
    wizard.wait_page()
    wizard.skip()

    popup = PlatformAppHomePopupPage()
    if popup.wait_page():
        popup.close()

    home_page = PlatformAppHomePage()
    if home_page.wait_page():
        return True
    else:
        return False
