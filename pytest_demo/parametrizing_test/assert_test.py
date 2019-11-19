import pytest
import sys
import parametrizing_test.mymodule
from parametrizing_test import mymodule

'''def f():
    return 3

def test_function():
    a = f()
    assert a % 2 == 0,"判断a为偶数，当前a的值为：%s"%a'''

'''def test_zero_division():
    with pytest.raises(ZeroDivisionError,message ="Expecting ZeroDivisionError") as excinfo:
        1 / 0

    assert excinfo.type == ZeroDivisionError
    assert "division by zero" in str(excinfo.value)'''
'''
if not pytest.config.getoption("--custom-flag"):
    pytest.skip("--custom-flag is missing, skipping tests",allow_module_level=True)'''
minversion = pytest.mark.skipif(mymodule.__versioninfo__ < '1.1',
                                reason="at least mymodule-1.1 required")
def is_true(a):
    if a>0:
        return True
    else:
        return False

@pytest.mark.skip(reason="no way of currently testing this")
def test_01():
    a = 5
    b = -1
    assert is_true(a)
    assert not is_true(b)

@pytest.mark.skipif(sys.version_info < (3,0),reason="requires python3.6 or higher")
def test_02():
    a = "hello"
    b = "hello world"
    assert a in b

@minversion
def test_03():
    a = "yoyo"
    b = "yoyo"
    assert a == b

def test_04():
    a = 5
    b = 6
    assert a != b


def valid_config():
    pass


def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")

