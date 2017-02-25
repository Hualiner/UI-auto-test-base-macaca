import os
import sys

sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
from Public.CaseStrategy import CaseStrategy
from Public.Drivers import Drivers


if __name__ == '__main__':
    cs = CaseStrategy()
    cases = cs.collect_cases(suite=False)

    # in future, cases_list may be used for testing strategy in multi devices
    Drivers().run(cases)
