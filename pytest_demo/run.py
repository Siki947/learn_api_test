import pytest

if __name__ == '__main__':
    '''mark标签写入pytest.ini'''
    pytest.main(["-v","./mark_test/test_mark.py","--markers"])
    '''mark标记'''
    #pytest.main(["-v","./mark_test/test_mark.py","-m=hello"])
    '''函数节点id'''
    #pytest.main(["-v","./mark_test/test_server.py::TestClass::test_method"])
    '''不执行标记的测试'''
    #pytest.main(["-s", "./mark_test/test_server.py", "-m='not webtest'"])
    '''执行标记的测试'''
    #pytest.main(["-s","./mark_test/test_server.py","-m=webtest"])
    '''测试结果保存至allure'''
    #pytest.main(["-s","./parametrizing_test/assert_test.py","-q","--alluredir=./parametrizing_test/report"])
    '''断言失败截图'''
    #pytest.main(["-s","html_screenshot/test_01.py","--html=./html_screenshot/report.html", "--self-contained-html"])
    #pytest.main(["-s","./parametrizing_test/cmdopt_test.py","--cmdopt=type2"])