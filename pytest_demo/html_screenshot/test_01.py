import time
import pytest
from selenium import webdriver

def test_jsq_01(browser):
    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t = browser.title
    assert t =="上海-悠悠"



# if __name__ == '__main__':
#     pytest.main(["--html=report.html","--self-contained-html"])
