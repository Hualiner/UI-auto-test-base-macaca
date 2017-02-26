import time

from Public.BasePage import BasePage


class WaitString(BasePage):
    def wait_all(self, *args, max_time=10):
        """
        wait all strings between the gaven time
        :param args: strings
        :param max_time: time that wait the gaven strings
        :return: True or False
        """
        times = max_time

        for i in range(10):
            source = self.driver.source

            previous = False
            for j in range(len(args)):
                if args[j] in source:
                    if j != 0 and not previous:
                        return False

                    previous = True

                    if j == len(args) - 1:
                        return True
                else:
                    if previous:
                        return False

            if i == times - 1:
                return False
            else:
                time.sleep(1)

    def wait_anyone(self, *args, max_time=10):
        """
        wait anyone string between the gaven time
        :param args: strings
        :param max_time: time that wait the gaven strings
        :return: True or False
        """
        times = max_time

        for i in range(10):
            source = self.driver.source

            for string in args:
                if string in source:
                    return True

            if i == times - 1:
                return False
            else:
                time.sleep(1)
