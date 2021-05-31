import pytest
import requests
import json
from common.Log import MyLog as Log
import configparser
import re
import os
from common import readInterfaceURL


@pytest.fixture()
def loginManage():
    """
    后台管理端登录cd
    :return:
    """
    log = Log.get_log()
    logger = log.get_logger()

    config = configparser.ConfigParser()
    proDir = os.path.dirname(os.getcwd())
    confPath = os.path.join(proDir, "conf", "config.ini")
    config.read(confPath, encoding="utf-8")
    # list = []
    list = config.sections()

    if "WEBHEADERS" not in list:
        config.add_section("WEBHEADERS")

    header = {

        "Accept": config.get("WEBHEADERS","Accept"),
        "User-Agent":config.get("WEBHEADERS","User-Agent"),
        "Content-Type": config.get("WEBHEADERS","Content-Type"),
        "Accept-Encoding": config.get("WEBHEADERS","Accept-Encoding"),
        "Accept-Language": config.get("WEBHEADERS","Accept-Language")
        }
    data = {"userName":"s2b-admin","password":"zs123456"}
    #data_json = json.dumps(payload)
    host = config.get("HTTP","scheme")+"://"+config.get("HTTP","baseurl")+"/"
    uri = readInterfaceURL.get_url_from_xml("webLogin")
    try:
        respones = requests.post(url=host+uri,json=data,headers=header)
        if respones.cookies:
            manage_cookies = "".join(re.findall(r"<Cookie(.+?)for",str(respones.cookies).replace(' ','')))
            try:
                config.set("WEBHEADERS","cookies",manage_cookies)
                with open(confPath,"w+") as f:
                    config.write(f)
                    logger.info("cookies写入config.ini[WEBHANDERS]成功")
            except Exception as e:
                logger.error("cookies写入错误：%s"%e)
            logger.info("登录成功")
            return respones
        else:
            logger.error("登录失败，status_code：%s"%respones.status_code)
    except Exception as e:
        logger.error("登录异常：%s"%e)

@pytest.fixture()
def loginMini():
    """
    童E时代小程序登录
    :return:
    """
    log = Log.get_log()
    logger = log.get_logger()

    config = configparser.ConfigParser()
    proDir = os.path.dirname(os.getcwd())
    confPath = os.path.join(proDir, "conf", "config.ini")
    config.read(confPath, encoding="utf-8")
    # list = []
    list = config.sections()

    if "MINIHEADERS" not in list:
        config.add_section("MINIHEADERS")

    header = {

        "Accept": config.get("MINIHEADERS", "Accept"),
        "User-Agent": config.get("MINIHEADERS", "User-Agent"),
        "Content-Type": config.get("MINIHEADERS", "Content-Type"),
        "Accept-Encoding": config.get("MINIHEADERS", "Accept-Encoding"),
        "Accept-Language": config.get("MINIHEADERS", "Accept-Language"),
        "host": config.get("MINIHEADERS", "host")
    }
    data = {"userName": "18800000001", "password": "123456"}
    # data_json = json.dumps(payload)
    host = config.get("HTTP", "scheme") + "://" + config.get("HTTP", "baseurl") + "/"
    uri = readInterfaceURL.get_url_from_xml("miniLogin")
    try:
        respones = requests.post(url=host + uri, json=data, headers=header)
        if respones.cookies:
            mini_cookies = respones.headers['Set-Cookie'].split(";")[0].strip()[8:]
            try:
                config.set("MINIHEADERS", "x-token", mini_cookies)
                with open(confPath, "w+") as f:
                    config.write(f)
                    logger.info("cookies写入config.ini[MINIHANDERS]成功")
            except Exception as e:
                logger.error("cookies写入错误：%s" % e)
            logger.info("登录成功")
            return respones
        else:
            logger.error("登录失败，status_code：%s" % respones.status_code)
    except Exception as e:
        logger.error("登录异常：%s" % e)


