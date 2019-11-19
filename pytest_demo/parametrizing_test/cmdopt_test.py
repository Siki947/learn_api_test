import pytest
from parametrizing_test.assert_test import minversion

@minversion
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")

    elif cmdopt == "type2":
        print("second")
    assert 0

