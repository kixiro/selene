import atexit

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import selene
from selene.browsers import Browser


def is_driver_initialized(name):
    try:
        return selene.selene_driver._shared_web_driver_source.driver.name == name
    except AttributeError:
        return False


def ensure_browser_started(name):
    if is_driver_initialized(name):
        return

    atexit._run_exitfuncs()
    if name == Browser.CHROME:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif name == Browser.MARIONETTE:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Firefox()
    atexit.register(driver.quit)
    selene.tools.set_driver(driver)
