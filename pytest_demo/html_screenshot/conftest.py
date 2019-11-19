import pytest
from selenium import webdriver


driver = None



@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report,'extra',[])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::","_")+".png"
            print("driver2",driver)
            screen_img = _capture_screenshot()

            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_results_table_header(cells):



def _capture_screenshot():
    '''截图保存为base64,展示到html'''
    return driver.get_screenshot_as_base64()





