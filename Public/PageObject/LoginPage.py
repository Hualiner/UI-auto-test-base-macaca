from macaca import WebDriverException

from Public.PageObject.BasePage import BasePage

from Public.Decorator import teststep


class LoginPage(BasePage):
    @teststep
    def wait_page(self):
        """以登录页面的“登录”Button的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id('com.platform.jhj:id/login_btn')
            return True
        except WebDriverException:
            return False

    @teststep
    def input_account(self, account):
        """以“请输入手机号码”的TEXT为依据"""
        self.driver\
            .element_by_name('请输入手机号码')\
            .clear()\
            .send_keys(account)

    @teststep
    def input_password(self, pwd):
        """以“输入登录密码”的XPATH为依据"""
        self.driver\
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]'
                              '/android.widget.RelativeLayout[2]/android.widget.EditText[1]')\
            .clear()\
            .send_keys(pwd)

    @teststep
    def login(self):
        """以“登录”Button的ID为依据"""
        self.driver\
            .element_by_id('com.platform.jhj:id/login_btn')\
            .click()
