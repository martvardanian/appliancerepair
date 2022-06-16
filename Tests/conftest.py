import pytest
from selenium import webdriver
from Configs.configs import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init_driver(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
#         print("Launching Chrome browser..........")
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
#         print("Launching Firefox browser..........")
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()

@pytest.fixture()
def setup(browser):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--window-size=1280,800")
    s = Service(ChromeDriverManager().install())
    if browser == 'chrome':
        driver = webdriver.Chrome(service=s, options=options)
        # driver = webdriver.Chrome(executable_path=DriverPath.CHROME_EXECUTABLE_PATH)
        print("Launching Chrome browser..........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=DriverPath.FIREFOX_EXECUTABLE_PATH)
        print("Launching Firefox browser..........")
    else:
        driver = webdriver.Chrome(service=s, options=options)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")







# jenkins shell
# export PYTHONPATH="${PYTHONPATH}:/home/erida-employee/Desktop/Mart/ApplianceRepairAuto"
# python3 --version
# python3 -m venv venv
# source venv/bin/activate
# python --version
# pip3 install pytest
# pip3 install selenium
# pip3 install webdriver-manager
# pytest /home/erida-employee/Desktop/Mart/ApplianceRepairAuto/Tests/Positive