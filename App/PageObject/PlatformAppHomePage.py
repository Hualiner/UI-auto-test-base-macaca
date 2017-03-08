from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps

from App.PageObject.WebViewPage import WebViewPage
from App.PageObject.InviteFriendsPage import InviteFriendsPage
from App.PageObject.LoginPage import LoginPage
# from App.PageObject.MsgCenterPage import MsgCenterPage


class PlatformAppHomePage(BasePage):
    @teststep
    def wait_page(self, timeout=10000):
        """以“消息图标”的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id('com.platform.jhj:id/home_msg_btn', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def click_msg(self):
        """以“消息图标”的ID为依据"""
        self.driver\
            .element_by_id('com.platform.jhj:id/home_msg_btn')\
            .click()

    @teststep
    def wait_business(self, timeout=10000):
        """以“保险”业务NAME为依据"""
        try:
            self.driver.wait_for_element_by_name('保险', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def click_insurance(self):
        """点击“保险”Icon的中文字体上方（高出中文字体上边界2倍中文字体的高度）"""
        element = self.driver.element_by_name('保险')
        self.click_above_of_element(element, rate=2)

    @teststep
    def click_mutual_help(self):
        e = self.driver.element_by_name('保险')

        element = self.find_element_by_swipe_left('name', '互助', element=e)
        self.click_above_of_element(element, rate=2)

    @teststep
    def click_jhj(self):
        element = self.driver.element_by_name('金惠家')
        self.click_above_of_element(element, rate=0.5)

    @teststep
    def wait_jhj(self, timeout=10000):
        try:
            self.driver.wait_for_element_by_name('金惠家', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def click_safeguard(self):
        element = self.driver.element_by_name('保障')
        self.click_above_of_element(element, rate=0.5)

    @teststep
    def click_hot_insurance_more(self):
        """以“热卖保险”对应的“更多”的ID为依据"""
        self.find_element_on_vertical('id', 'com.platform.jhj:id/home_fm_insurance_more_tv').click()

    @teststep
    def click_invite_friends(self):
        self.find_element_by_swipe_up('id', 'com.platform.jhj:id/invite_Friends_img').click()


new_page_timeout = 0
old_page_timeout = 0


@teststeps
def close_web_view():
    web_view = WebViewPage()
    invite = InviteFriendsPage()
    # msg = MsgCenterPage()
    login = LoginPage()

    if login.wait_page(timeout=old_page_timeout):
        login.back()

    if web_view.wait_page(timeout=old_page_timeout):
        web_view.back()
        return True
    elif invite.wait_back(timeout=old_page_timeout):
        invite.back()
        return True
    # in the home page, this element is always displayed. so, this process can not work correctly
    # elif msg.wait_back(timeout=old_page_timeout):
    #     msg.back()
    #     return True
    else:
        return False


@teststeps
def back_to_home_page():
    """返回App首页，以“消息图标”的ID为依据"""
    home_page = PlatformAppHomePage()
    if not home_page.wait_page(timeout=new_page_timeout):
        if close_web_view():
            timeout = new_page_timeout
        else:
            timeout = old_page_timeout

        if not home_page.wait_page(timeout=timeout):
            flag = False
            if home_page.wait_jhj(timeout=old_page_timeout):
                home_page.click_jhj()
                flag = True

            if flag:
                timeout = new_page_timeout
            else:
                timeout = old_page_timeout

            if not home_page.wait_page(timeout=timeout):
                home_page.find_element_by_swipe_down('id', 'com.platform.jhj:id/home_msg_btn')

    assert home_page.wait_page(timeout=old_page_timeout)


@teststeps
def back_to_business_entry():
    """返回App首页，以“保险”的NAME为依据"""
    home_page = PlatformAppHomePage()
    if not home_page.wait_business(timeout=new_page_timeout):
        if close_web_view():
            timeout = new_page_timeout
        else:
            timeout = old_page_timeout

        if not home_page.wait_business(timeout=timeout):
            flag = False
            if home_page.wait_jhj(timeout=old_page_timeout):
                home_page.click_jhj()
                flag = True

            if flag:
                timeout = new_page_timeout
            else:
                timeout = old_page_timeout

            if not home_page.wait_business(timeout=timeout):
                home_page.find_element_by_swipe_down('name', '保险')

    assert home_page.wait_business(timeout=old_page_timeout)


@teststeps
def back_to_app():
    """返回至App，以“金惠家”bottom tab为依据"""
    timeout = new_page_timeout
    home_page = PlatformAppHomePage()
    if not home_page.wait_jhj(timeout=new_page_timeout):
        if close_web_view():
            timeout = new_page_timeout
        else:
            timeout = old_page_timeout

    assert home_page.wait_jhj(timeout=timeout)


@teststeps
def back_to_jhj_tab():
    """返回值“金惠家”tab页"""
    home = PlatformAppHomePage()

    back_to_app()
    home.click_jhj()
