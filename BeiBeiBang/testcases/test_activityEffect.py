import requests
from  common import Log
from  common import configDB
from collections import Counter




log = Log.MyLog.get_log()
logger = log.get_logger()


class TestActivityEffect():
    def test_goodsStock(self):

        db = configDB.MyDB()
        sql = r"""SELECT
	s.goods_count,
	s.sent_count,
	s.sale_order_no
FROM
	(
		SELECT
			SUM(goods_count) goods_count,
			SUM(sent_count) sent_count,
			sale_order_no
		FROM
			`sale_order_item`
		GROUP BY
			sale_order_id
	) s
LEFT JOIN sale_order o ON s.sale_order_no = o.sale_order_no
WHERE
	s.goods_count > s.sent_count
AND s.sent_count >= 1
AND o.sale_order_type = "A"
AND o.sale_order_status = "PRE_ACCEPT";"""
        cur = db.executeSQL(sql)
        results = db.get_all(cur)
        db.closeDB()
        url = "http://101.132.173.21/api/admin/admins/saleOrder/?limit=50&page=1&offset=0&saleOrderStatus=PART_DELIVER"
        r = requests.get(url)
        d = r.json()
        data = d["items"]
        print(data)
        lists = []
        orderNos = []
        for list in data:
            lists.append(list["saleOrderNo"])
        print(lists)
        # print(lists.__len__())
        for i in results:
            orderNo = i[2]
            orderNos.append(orderNo)
            # print(orderNo)
            if orderNo in lists :
                pass
            else:
                print(orderNo,"不在返回数据中")
        print(orderNos.__len__()) #list元素的个数
        print(Counter(orderNos)) #元素在list中的个数





if __name__ == '__main__':
    TestActivityEffect().test_goodsStock()