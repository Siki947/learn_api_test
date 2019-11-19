import pytest
test_user_data = ["admin1","admin2"]

@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("登录账户：%s"%user)
    return user

'''添加indirect=True参数是为了把login当成一个函数去执行，而不是一个参数

'''
@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_login(login):
    a = login
    print("测试用例中login的返回值：%s"% a)
    assert a !=""


