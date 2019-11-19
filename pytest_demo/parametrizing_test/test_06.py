import pytest

@pytest.fixture(scope="function")
def start(request):
    print("\n---开始执行function---")

@pytest.mark.usefixtures("start")
def test_a():
    print("----用例a执行---")

@pytest.mark.usefixtures("start")
class Test_aaa():
    def test_01(self):
        print('------用例01------')

    def test_02(self):
        print('-----用例02-----')
        