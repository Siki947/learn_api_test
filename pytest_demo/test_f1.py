import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并打开百度首页")
    yield
    print("执行teardown")
    print("最后关闭浏览器")
def test_s1(open):
    print("用例1")

def test_s2(open):
    print("用例2")

def test_s3(open):
    print("用例3")

if __name__ == '__main__':
    pytest.main(["-s","test_f1.py"])