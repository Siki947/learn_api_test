import pytest
import requests
import json
from common.Log import MyLog as Log
import configparser
import re
import os

log = Log.get_log()
logger = log.get_logger()

config = configparser.ConfigParser()
proDir = os.path.dirname(os.getcwd())
confPath = os.path.join(proDir,"conf","config.ini")
config.read(confPath, encoding="utf-8")
list = []
list = config.sections()
if "HEADERS" not in list:
     config.add_section("HEADERS")

@pytest.fixture(scope="module")
def loginManage():
    """
    后台管理端登录
    :return:
    """
    header = {

        "Accept": "application/json, text/plain, */*",

        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": "zh-CN,zh;q=0.9"
        }
    data = {"userName":"s2b-admin","password":"zs123456"}
    #data_json = json.dumps(payload)
    try:
        respones = requests.post(url='http://192.168.1.232/api/portal/auth/login',json=data,headers=header)
        if respones.cookies:
            manage_cookies = "".join(re.findall(r"<Cookie(.+?)for",str(respones.cookies).replace(' ','')))

            try:
                config.set("HEADERS","cookies",manage_cookies)
                with open(confPath,"w+") as f:
                    config.write(f)
                    logger.info("cookies写入config.ini成功")
            except Exception as e:
                logger.error("cookies写入错误：%s"%e)
            logger.info("登录成功")
            return respones
        else:
            logger.error("登录失败，status_code：%s"%respones.status_code)
    except Exception as e:
        logger.error("登录异常：%s"%e)

loginManage()
