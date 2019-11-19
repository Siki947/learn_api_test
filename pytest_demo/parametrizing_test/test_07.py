import pytest

@pytest.fixture(scope="module",autouse=True)
def start(request):
    print('\n---开始执行moule-----')
    print('module：%s' % request.module.__name__)
    print('------启动浏览器------')
    yield
    print("-------结束测试end-----")

class Test_aaa():
    @pytest.fixture(scope="function",autouse=True)
    def open_home(self,request):
        print("function:%s \n------回到首页-----" % request.function.__name__)

    def test_01(self):
        print('-----------用例01--------------')

    def test_02(self):
        print('-----------用例02------------')
