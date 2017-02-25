from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps

from App.PageObject.GesturePasswordPage import GesturePasswordPage


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
        """以“请输入登录密码”的XPATH为依据"""
        self.driver\
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]'
                              '/android.support.v7.widget.LinearLayoutCompat[2]/android.widget.EditText[1]')\
            .clear()\
            .send_keys(pwd)

    @teststep
    def login(self):
        """以“登录”Button的ID为依据"""
        self.driver\
            .element_by_id('com.platform.jhj:id/login_btn')\
            .click()


@teststeps
def valid_login(account, password):
    """用给定的account与password进行登录，登录后返回登录前的页面"""
    login = LoginPage()
    login.input_account(account)
    login.input_password(password)
    login.login()

    gesture = GesturePasswordPage()
    if gesture.wait_page():
        gesture.skip()
