import pytest

def test_sl(login):
    print("用例1：登录之后其它动作1")

def test_s2():
    print("用例2：不需要登录，操作")

def test_s3(login):
    print("用例3：登录之后其它动作3")

# if __name__ == '__main__':
#     pytest.main(["-s","test_fix1.py"])