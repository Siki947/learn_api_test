from common import configDB
from common import Log
from common import configDB
from common import readSQL
import pytest

log = Log.MyLog.get_log()
logger = log.get_logger()


def effective_bds(month):
    """
    查询有效BD,有配置bd提成，且状态正常的bd
    :return:
    """
    db = configDB.MyDB()
    db.connectDB()
    sql = readSQL.ReadSQL().get_sql("prd", "wechat_commission", "select_effective_BD")
    sql = sql % month
    cur = db.executeSQL(sql)
    effective_bds = db.get_all(cur)
    db.closeDB()
    return effective_bds


def b_orders(month):
    """
    查询sale_order表中bd下小b某月订单支付总金额
    :param month:
    :return:(store_id,total_final_amount)
    """
    effective_bds_commission = effective_bds(month)
    effective_bds_id = str(tuple([i[0] for i in effective_bds_commission]))
    db = configDB.MyDB()
    db.connectDB()
    read_sql = readSQL.ReadSQL()
    b_order_sum_sql = read_sql.get_sql("prd", "sale_order", "select_b_order_sum") % (month, effective_bds_id)
    cur_b_order = db.executeSQL(b_order_sum_sql)
    b_order_sum = list(db.get_all(cur_b_order))
    logger.info(b_order_sum)
    db.closeDB()
    if b_order_sum:
        return b_order_sum
    else:
        return None


def b_estimate_orders(month):
    """
    查询bds_order_estimate表中bd下小b某月订单支付总金额
    :param month:
    """
    effective_bds_commission = effective_bds(month)
    effective_bds_id = str(tuple([i[0] for i in effective_bds_commission]))
    db = configDB.MyDB()
    db.connectDB()
    read_sql = readSQL.ReadSQL()
    # my_redis = configRedis.MyRedis()
    # my_redis.connect_redis()
    b_estimate_order_sum_sql = read_sql.get_sql("prd", "bds_order_estimate", "select_b_estimate_order_sum") % (
    month, effective_bds_id)
    cur_b_estimate_order = db.executeSQL(b_estimate_order_sum_sql)
    b_estimate_order = db.get_all(cur_b_estimate_order)
    logger.info(b_estimate_order)
    db.closeDB()
    if b_estimate_order:
        # for store_estimate_order in b_estimate_order_sum:
        #     my_redis.insert_value(store_estimate_order[0], store_estimate_order[1])
        # my_redis.execute_pipe()
        b_estimate_order_dict = {}
        for key, value in b_estimate_order:
            b_estimate_order_dict[key] = value
        return b_estimate_order_dict
    else:
        return None


b_estimate_order_dict = b_estimate_orders("2021-04")
b_order_list = b_orders("2021-04")


@pytest.mark.parametrize("month", ["2021-04"])
class TestBdTool():

    @pytest.mark.parametrize("store_id,total_final_amount", b_order_list)
    def test_amount_b_order_equal_b_estimate(self, month, store_id, total_final_amount):
        """
        1.sale_order表中bd下的小b某月订单支付总金额与bds_order_estimate表中该bd总金额是否相等
        2.bds_order_estimate表中某月产生订单数据的小b数量是否与sale_order表中的小b数量一致
        :param month:
        :return:
        """
        if store_id and total_final_amount:
            b_estimate_sum = b_estimate_order_dict.get(store_id)
            if b_estimate_sum:
                assert total_final_amount == b_estimate_sum, "sale_order表中store_id = %s 的用户商品支付总金额为：%s,bds_order_estimate 表中该用户商品支付总金额为：%s" % (
                store_id, total_final_amount, b_estimate_sum)
            else:
                assert False, "bds_order_estimate表中无bd_id=%s 的订单数据" % store_id
        else:
            logger.info("当前有效BD中，sale_order表中%s没有订单数据" % month)

    def test_len_b_order_equal_b_estimate(self, month):
        if b_order_list:
            b_orders_len = len(b_order_list)
            if b_estimate_order_dict:
                b_estimate_len = len(b_estimate_order_dict)
                if b_orders_len == b_estimate_len:
                    assert True, "sale_order表中下单小b数量为：%s与bds_order_estimate中小b数量：%s ，一致" % (
                    b_orders_len, b_estimate_len)
                else:
                    assert False, "sale_order表中下单小b数量为：%s与bds_order_estimate中小b数量：%s，不一致" % (
                    b_orders_len, b_estimate_len)
            else:
                assert False, "bds_order_estimate 表中 %s 无订单数据" % month
        else:
            assert True, "当前有效BD中，sale_order表中%s没有订单数据" % month


if __name__ == '__main__':
    pytest.main(["-s", "test_bd_tool.py", '--html = D:/learn_api_test/BeiBeiBang/report/report.html'],
                ['--self-contained-html'])
