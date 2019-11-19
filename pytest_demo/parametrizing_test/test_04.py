import pytest

test_user = ["admin1","admin2"]
test_psw = ["111111","222222"]

@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user

@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw

@pytest.mark.parametrize("input_user",test_user,indirect=True)
@pytest.mark.parametrize("input_psw",test_psw,indirect=True)
def test_login(input_user,input_psw):
    a = input_user
    b = input_psw
    print("测试数据a-> %s,b-> %s" % (a,b))
    assert b
