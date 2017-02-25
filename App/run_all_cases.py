import sys

sys.path.append('..')
from Public.CaseStrategy import CaseStrategy
from Public.Drivers import Drivers


if __name__ == '__main__':
    cs = CaseStrategy()
    cases = cs.collect_cases(suite=True)

    # in future, cases_list may be used for testing strategy in multi devices
    Drivers().run(cases)
