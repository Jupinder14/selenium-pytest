import pytest
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.calorie_calc import CarbCalcPage

@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.calculator = CarbCalcPage()

    yield
    driver.close()
    driver.quit()

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        attach(driver.get_screenshot_as_png(),name="Screenshot",attachment_type=AttachmentType.PNG)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep