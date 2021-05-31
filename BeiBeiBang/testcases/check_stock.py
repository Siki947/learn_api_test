import requests
from  common import Log
from  common import configDB
from  lxml import etree
import pytest
from common import readSQL

log = Log.MyLog.get_log()
logger = log.get_logger()




class CheckStock():
    def check_goodsStockCount(self):

        db = configDB.MyDB()
        sql = readSQL.ReadSQL().get_sql("prd", "store_goods", "select_goods_stock")
        cur = db.executeSQL(sql)
        results = db.get_all(cur)
        db.closeDB()
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            "Accept": "application/json, text/javascript, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": "_ati=3209090711565; wph_device_id=1618889787847_2b05a6e890ab25334edd540a2b88d49f; fastappsid=hjsa0io6bvv9m8umr1rtq4mc04",
            "Host": "39.100.102.31",
            "Proxy-Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "X - Requested - With": "XMLHttpRequest"
        }
        url = "http://39.100.102.31/e3test/webdrp/web/?app_act=kc_manage/report/kc_sscx_stock"
        # url = "http://39.100.102.31/e3/webdrp/web/?app_act=kc_manage/report/kc_sscx_stock"

        for i in results:
            goods_code_result = i[0]
            real_stock_result = i[1]
            real_lock_stock = i[2]
            param = {
                "ctl_reqid: webdrp":"kc_manage / report / kc_sscx",
                "ctl_uid": "DataTable:DataTable1",
                "ctl_table_id": "DataTable1",
                "ctl_conf": "ImtjX21hbmFnZVwvc3NrYyI =",
                "ctl_dataset": "ImtjX21hbmFnZVwvcmVwb3J0X21vZGVsOjpnZXRfc3NrY19ieV9wYWdlIg ==",
                "ctl_count": "true",
                "ctl_pager": "true",
                "ctl_style":"",
                "ctl_script": "true",
                "ctl_type": "view",
                "ctl_table":"",
                "ctl_params": "eyJmaWx0ZXIiOltdfQ ==",
                "ctl_field_set": "sskc_field_set",
                "record_count": 1,
                "page_size": 20,
                "page_count": 1,
                "page": 1,
                "total_money": 0.00,
                "goods_sn_id": 0,
                "goods_sn": goods_code_result,
                "sku_ids": 0,
                "sku":"",
                "goods_ids": 0,
                "goods_id_name":"",
                "category_name":"",
                "color_id_name":"",
                "size_id_name":"",
                "brand_id":"",
                "year_id":"",
                "season_id":"",
                "series_id":"",
                "qd_id":"",
                "ck_id": "1, 22",
                "kw_id":"",
                "sl": 0,
                "six_nine_code": 0,
                "six_nine_code_name":"",
                "wllx":"",
                "sp":"",
                "zjf":"",
                "order_by_field":"",
                "order_by_value": 1,
                "compare_kc": 0,
                "goods_s_ids": 0,
                "goods_id_sname":"",
                "ky_kc":"",
                "category": 0,
                "isparent": 0,
                # "ck_id_view": "线上中心仓, 童e时代总仓",
                "ck_id_view": "天猫平台仓,总仓",
                "sl_op": 1,
                "csrf_token": "873c7fafdc527aa1fe2b10dfc8e84800",
                "wph_device_id": "1618889787847_2b05a6e890ab25334edd540a2b88d49f",
                "csrf_token": "5c4c89e8162e127983df7985e9230600",


            }
            r = requests.post(url,data=param,headers=header)
            logger.info(r)
            d = r.json()
            logger.info(d)
            # print("re:",d)
            date = d['data']
            dateList1 = date.split(";")
            dateList2 = dateList1[3]
            e3_goodsStock = int(dateList2[5:-5])
            # print(type(e3_goodsStock))
            if (real_stock_result-real_lock_stock) == e3_goodsStock:
                logger.info("goods_code : %s 商品库存数为：%s 。与E3可用库存一致"%(goods_code_result,real_stock_result))
            else:
                logger.info("goods_code : %s 童E时代商品库存数为：%s ；E3总可用库存为：%s 。与E3可用库存不一致"%(goods_code_result,real_stock_result-real_lock_stock,e3_goodsStock))




    def check_skuStockCount(self):

        db = configDB.MyDB()
        sql = "SELECT goods_code,real_stock FROM `store_goods` WHERE store_id=1 AND deleted=0 AND shelves=\"ON_SHELVES\" AND stock_type=\"REAL_STOCK\";"
        cur = db.executeSQL(sql)
        results = db.get_all(cur)
        # print(results)
        db.closeDB()
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": "_ati=3209090711565; fastappsid=7d2ltibu5q7jja20n25epj76o0",
            "Host": "39.100.102.31",
            "Proxy-Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "X - Requested - With": "XMLHttpRequest"
        }
        url = "http://39.100.102.31/e3/webdrp/web/?app_act=ctl/index/do_index&app_ctl=DataTable/do_get_data&ajax=1&type=1"
        for i in results:
            goods_code_result = i[0]
            param = {
                "ajax": 1,
                "type": 1 ,
                "ctl_reqid": "webdrp:kc_manage / report / kc_sscx",
                "ctl_uid": "DataTable:DataTable1",
                "ctl_table_id": "DataTable1",
                "ctl_conf": "ImtjX21hbmFnZVwvc3NrYyI =",
                "ctl_dataset": "ImtjX21hbmFnZVwvcmVwb3J0X21vZGVsOjpnZXRfc3NrY19ieV9wYWdlIg ==",
                "ctl_count": "true",
                "ctl_pager": "true",
                "ctl_script": "true",
                "ctl_type": "view",
                "ctl_params": "eyJmaWx0ZXIiOltdfQ ==",
                "ctl_field_set": "sskc_field_set",
                "record_count": 2,
                "page_size": 20,
                "page_count": 1,
                "page": 1,
                "total_money": 0.00,
                "goods_sn_id": 0,
                "goods_sn": goods_code_result,
                "sku_ids": 0,
                "goods_ids": 0,
                "ck_id": "1, 22",
                "sl": 0,
                "six_nine_code": 0,
                "order_by_value": 1,
                "compare_kc": 0,
                "goods_s_ids": 0,
                "category": 0,
                "isparent": 0,
                "ck_id_view": "线上中心仓, 童e时代总仓",
                "sl_op": 1,

            }
            r = requests.post(url,data=param,headers=header)
            e3_results = r.content



        html = etree.HTML()

if __name__ == '__main__':
    # TestStock().test_goodsStockCount()
    # pytest.mian(["-s", "test_goodsStockCount.py"]) #-s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程
    CheckStock().check_goodsStockCount()