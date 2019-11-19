import pytest

@pytest.mark.parametrize("y",[0,1])
@pytest.mark.parametrize("x",[2,3])
def test_foo(x,y):
    print("x->%s,y->%s" % (x,y))