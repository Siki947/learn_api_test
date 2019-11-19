import pytest

test_user_data = [{"user":"admin1","psw":"1111"},
                  {"user":"admin1","psw":""}]

@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("登录账户：%s"%user)
    print("登录账户：%s"%psw)
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_login(login):
    a = login
    print("logind的返回值：%s" % a)
    assert a,"失败原因：密码为空"