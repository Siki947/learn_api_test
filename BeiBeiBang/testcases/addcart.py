import requests
from  common import Log
from conf import  readConfig
from common import readSQL
from common import configDB

log = Log.MyLog.get_log()
logger = log.get_logger()

def add_goods_to_cart():
    mini_header = readConfig.ReadConfig()
    header = {
        "User-Agent": mini_header.get_headers("MINIHEADERS","user-agent"),
        "Accept": mini_header.get_headers("MINIHEADERS","accept"),
        "Accept-Language": mini_header.get_headers("MINIHEADERS","accept-language"),
        "Accept-Encoding": mini_header.get_headers("MINIHEADERS","accept-encoding"),
        "x-token":mini_header.get_headers("MINIHEADERS","x-token"),
        "Host": mini_header.get_headers("MINIHEADERS","host"),
        "Connection":mini_header.get_headers("MINIHEADERS","connection"),
        "Content-Type": mini_header.get_headers("MINIHEADERS","content-type"),
        "X-Requested-With": mini_header.get_headers("MINIHEADERS","x-requested-with")
    }
    add_cart = "http://192.168.1.232/api/sloop/cart"
    my_sql = readSQL.ReadSQL()
    sql = my_sql.get_sql("prd","store_goods_sku","select_goods_id_and_sku_id")
    my_bd = configDB.MyDB()
    my_bd.connectDB()
    my_cursor =my_bd.executeSQL(sql)
    goods_id_and_sku_id =my_bd.get_all(my_cursor)
    my_bd.closeDB()
    # logger.info("goods_id_and_sku_id = %s"%str(goods_id_and_sku_id))
    if goods_id_and_sku_id:
        body = []
        for datas in goods_id_and_sku_id:
            goods_id,goods_sku_id,real_stock = datas
            goods_sku = {}
            goods_sku["sourceId"]=1
            goods_sku["goodsId"]=str(goods_id)
            goods_sku["skuId"]=goods_sku_id
            goods_sku["quantity"]=1
            goods_sku["realStock"]=real_stock
            body.append(goods_sku)
        try:
            result=requests.post(add_cart,json=body,headers=header)
            if result.status_code==200:
                logger.info("加入商品至购物车，请求成功")
            else:
                logger.info("加入商品至购物车，请求成功 状态码：%s"%result.text)
        except Exception as e:
            logger.error("请求加入购物车报错：%s"%e)
    else:
        logger.info("加入商品至购物车，查询goods_id和sku_id没有值")


if __name__ == '__main__':

    add_goods_to_cart()