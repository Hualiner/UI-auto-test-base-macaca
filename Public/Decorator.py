import sys
import time

from functools import wraps

from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.ReportPath import ReportPath
from Public.Log import Log


flag = 'IMAGE:'
log = Log()


def _screenshot(name):
    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screenshot = name + '-' + date_time + '.PNG'
    path = ReportPath().get_path() + '\\' + screenshot

    driver = BasePage().get_driver()
    driver.save_screenshot(path)

    return screenshot


def teststep(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('\t--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            return ret
        except WebDriverException:
            log.e('\t<-- %s, %s', func.__qualname__, 'Error')
            raise WebDriverException(message=flag + _screenshot(func.__qualname__))

    return wrapper


def teststeps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('  --> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.i('  <-- %s, %s', func.__qualname__, 'Success')
            return ret
        except WebDriverException:
            log.e('  <-- %s, %s', func.__qualname__, 'Error')
            raise WebDriverException

    return wrapper


def testcase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.i('<-- %s, %s\n', func.__qualname__, 'Success')
            return ret
        except WebDriverException:
            log.e('<-- %s, %s\n', func.__qualname__, 'Error')
            raise WebDriverException
        except AssertionError:
            log.e('<-- %s, %s\n', func.__qualname__, 'Fail')
            raise AssertionError(flag + _screenshot(func.__qualname__))

    return wrapper


def setup(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.i('--> %s', func.__qualname__)
        func(*args, **kwargs)
        log.i('<-- %s, %s\n', func.__qualname__, 'Success')

    return wrapper


def teardown(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.i('--> %s', func.__qualname__)
        func(*args, **kwargs)
        log.i('<-- %s, %s\n', func.__qualname__, 'Success')

    return wrapper


def setupclass(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.i('--> %s', func.__qualname__)
        func(*args, **kwargs)
        log.i('<-- %s, %s\n', func.__qualname__, 'Success')

    return wrapper


def teardownclass(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.i('--> %s', func.__qualname__)
        func(*args, **kwargs)
        log.i('<-- %s, %s\n', func.__qualname__, 'Success')

    return wrapper
