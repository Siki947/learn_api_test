from  common import configDB
from  common import Log
from  common import configDB
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
    sql = readSQL.ReadSQL().get_sql("prd", "wechat_commission", "select_effective_BD")
    sql = sql%month
    cur = db.executeSQL(sql)
    effective_bds = db.get_all(cur)
    logger.info("有效BD : %s"  %effective_bds)
    db.closeDB()
    return effective_bds
    # for bds_id in effective_bds:



def test_totalPackageAmount(month):
    """
    某月有效BD下小B的包裹总金额与commission_estimate_amount，finance_trade_info总金额是否相同
    :return:
    """
    pass
def test_totalCStoreSaleOrderAmount(month):
    """
    某月有效BD下小B的云店总金额与commission_estimate_amount，finance_trade_info总金额是否相同
    :param month:
    :return:
    """
    pass

def test_commissionPoint(month):
    """
    1.某月有效BD下小B的包裹和云店的提成点是否与commission_estimate_amount，finance_trade_info相同
    2.排除首单
    :param month:
    :return:
    """
    pass
def test_firstOrder(month):
    """
    某月有效BD下小B的首单金额是否与commission_estimate_amount，finance_trade_info相同
    :param month:
    :return:
    """
    pass
def test_totalPackageReturnAmount(month):
    """
    某月有效BD下小B的包裹退款总金额与commission_estimate_amount，finance_trade_info总金额是否相同
    :param month:
    :return:
    """
    pass

def test_totalCStoreReturnAmount(self, month):
    """
    某月有效BD下小B的云店退款总金额与commission_estimate_amount，finance_trade_info总金额是否相同
    :param month:
    :return:
    """
    pass

if __name__ == '__main__':
    print(inquire_effective_bd("2021-04"))
    # pytest.main(["-s", "test_bdPerformance.py"])