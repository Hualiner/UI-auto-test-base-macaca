import os
import sys

from macaca import WebDriver

sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
from Public.Log import Log
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage

from App.PageObject.PlatformAppHomePage import PlatformAppHomePage


class Run(BasePage):
    def run(self):
        # self.click_element_by_accessibility_id('为爱车投保')

        home = PlatformAppHomePage()
        home.click_insurance()


def init():
    port = int(sys.argv[1])
    udid = sys.argv[2]
    report_path = str(sys.argv[3])
    session = sys.argv[4]

    server_url = {
                'hostname': '127.0.0.1',
                'port': port,
    }

    log = Log()
    log.set_logger(udid, report_path + '\\' + 'client.log')

    driver = WebDriver('', server_url)
    driver.attach(session)

    # set cls.path, it must be call before operate on any page
    path = ReportPath()
    path.set_path(report_path)

    # set cls.driver, it must be call before operate on any page
    base_page = BasePage()
    base_page.set_driver(driver)


if __name__ == '__main__':
    init()

    Run().run()


