from macaca import WebDriverException

from Public.PageObject.BasePage import BasePage

from Public.Decorator import teststep


class PlatformAppHomePage(BasePage):
    @teststep
    def wait_page(self):
        """以首页底部“金惠家”Tab的中文名为依据"""
        try:
            self.driver\
                .wait_for_element_by_name('金惠家')
            return True
        except WebDriverException:
            return False

    @teststep
    def wait_popup(self):
        """以关闭popup的button的ID为依据"""
        try:
            self.driver \
                .wait_for_element_by_id('com.platform.jhj:id/main_popup_close_adimg')
            return True
        except WebDriverException:
            return False

    @teststep
    def close_popup(self):
        """以关闭popup的button的ID为依据"""
        self.driver\
            .element_by_id('com.platform.jhj:id/main_popup_close_adimg')\
            .click()

    @teststep
    def click_car_insurance(self):
        """以“车险”Icon图片的XPATH为依据"""
        self.driver \
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]'
                              '/android.widget.ImageView[1]') \
            .click()

    @teststep
    def click_insurance(self):
        """以“保险”Icon图片的XPATH为依据"""
        self.driver\
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.support.v4.view.ViewPager[1]/android.view.ViewGroup[1]'
                              '/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]'
                              '/android.widget.HorizontalScrollView[1]/android.widget.FrameLayout[1]'
                              '/android.widget.LinearLayout[3]/android.widget.ImageView[1]')\
            .click()

    @teststep
    def click_jhj(self):
        """以“金惠家”Tab的中文名称的XPATH为依据"""
        self.driver \
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]'
                              '/android.widget.TextView[1]')\
            .click()

    @teststep
    def click_discover(self):
        """以“发现”Tab的中文名称的XPATH为依据"""
        self.driver \
            .elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]'
                               '/android.widget.TextView[1]') \
            .click()

    @teststep
    def click_safeguard(self):
        """以“保障”Tab的中文名称的XPATH为依据"""
        self.driver \
            .elements_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                               '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]'
                               '/android.widget.TextView[1]') \
            .click()

    @teststep
    def click_my(self):
        """以“我的”Tab的中文名称的XPATH为依据"""
        self.driver\
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                              '/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]'
                              '/android.widget.TextView[1]')\
            .click()
