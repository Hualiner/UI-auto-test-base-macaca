import time

from multiprocessing import Pool

from macaca import WebDriver

from Public.Ports import Ports
from Public.Devices import Devices
from Public.MacacaServer import MacacaServer
from Public.RunCases import RunCases
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage
from Public.Log import Log

from App.PageObject.WizardPage import skip_wizard_to_home


class Drivers:
    @staticmethod
    def _run_cases(server_url, run, cases):
        log = Log()
        log.set_logger(run.get_device()['udid'], run.get_path() + '\\' + 'client.log')

        log.i('platformName: %s', run.get_device()['platformName'])
        log.i('udid: %s', run.get_device()['udid'])
        log.i('package: %s\n', run.get_device()['package'])

        log.i('macaca server port: %d\n', run.get_port())

        # init driver
        driver = WebDriver(run.get_device(), server_url)
        driver.init()

        # set cls.path, it must be call before operate on any page
        path = ReportPath()
        path.set_path(run.get_path())

        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        base_page.set_driver(driver)

        # skip wizard
        if skip_wizard_to_home():
            # run cases
            run.run(cases)

        # quit driver
        driver.quit()

    def run(self, cases):
        # read all devices on this PC
        devices = Devices().get_devices()

        # read free ports on this PC
        ports = Ports().get_ports(len(devices))

        if not len(devices):
            print('there is no device connected this PC')
            return

        runs = []
        for i in range(len(devices)):
            runs.append(RunCases(devices[i], ports[i]))

        # start macaca server
        macaca_server = MacacaServer(runs)
        macaca_server.start_server()
        for port in ports:
            while not macaca_server.is_running(port):
                print('wait macaca server all ready...')
                time.sleep(1)
        print('macaca server all ready')

        # run on every device
        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(self._run_cases,
                             args=(macaca_server.server_url(run.get_port()), run, cases,))

            # fix bug of macaca, android driver can not init in the same time
            time.sleep(2)

        pool.close()
        pool.join()
