import pytest

test_login_data = [("admin","111111"),("admin","")]

def login(user,psw):
    print("用户名：%s"%user)
    print("密码：%s"%psw)
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("user,psw",test_login_data)
def test_login(user,psw):
    result = login(user,psw)
    assert result == True,"失败原因：密码为空"


