import os
import sys

from macaca import WebDriver

sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
from Public.Devices import Devices
from Public.Ports import Ports
from Public.MacacaServer import MacacaServer
from Public.RunCases import RunCases
from Public.Log import Log
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage


def drive(server_url, run):
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

    while True:
        cmd = input("Please input run or exit:").lower()
        if cmd == 'run':
            print('Run run.py')
            print(os.system('python run.py %s %s %s %s'
                            % (run.get_port(),
                               run.get_device()['udid'],
                               run.get_path(),
                               driver.session_id
                               )
                            )
                  )
        elif cmd == 'exit':
            print('Good Bye')
            break

    # quit driver
    driver.quit()


def main():
    # read all devices on this PC
    devices = Devices().get_devices()

    # read free ports on this PC
    ports = Ports().get_ports(len(devices))

    if not len(devices):
        print('there is no device connected this PC')
        return

    runs = []
    runs.append(RunCases(devices[0], ports[0]))

    # start macaca server
    macaca_server = MacacaServer(runs)
    macaca_server.start_server()

    drive(macaca_server.server_url(runs[0].get_port()), runs[0])

    macaca_server.kill_macaca_server()


if __name__ == '__main__':
    main()
