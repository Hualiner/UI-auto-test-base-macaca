from macaca import WebDriverException

from Public.BasePage import BasePage

from Public.Decorator import teststep


class GesturePasswordPage(BasePage):
    @teststep
    def wait_page(self):
        """以手势密码绘制页面的文字提示的TEXT为依据"""
        try:
            self.driver\
                .wait_for_element_by_name('请绘制解锁图案')
            return True
        except WebDriverException:
            return False

    @teststep
    def skip(self):
        """以“跳过”Button的TEXT为依据"""
        self.driver\
            .element_by_name('跳过')\
            .click()
