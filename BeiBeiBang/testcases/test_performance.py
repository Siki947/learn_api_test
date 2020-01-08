from common import configDB



localConfigDB = configDB.MyDB()

class TestBDPerformance():
    def test_newUserAmount(self,loginManage,month):
        """
        新用户（三个月内下单）x月订单总额
        :return:
        """
    def test_oldUserAmountr(self,loginManage,month):
        """
        老用户（三个月后）X月订单总额
        :param month:
        :return:
        """
    def test_newUserCommission(self,loginManage,month):
        """
        新用户提成
        :param month:
        :return:
        """
    def test_oldUserCommission(self,loginManage,month):
        """
        老用户提成
        :param month:
        :return:
        """
    def test_firstOrder(self,loginManage,month,first_condition,min_reward,max_reward):
        """
        首单提成
        :param month:
        :param first_condition:
        :param min_reward:
        :param max_reward:
        :return:
        """
    def test_newStoreTotal(self,loginManage,month):
        """
        x月拓店数
        :param month:
        :return:
        """

    def test_firstOrderTotal(self,loginManage,month):
        """
        x月首单数
        :param month:
        :return:
        """
    def test_conversionRate(self,loginManage):
        """
        转化率
        :return:
        """
    def test_orderAmountTotal(self,loginManage,month):
        """
        x月订单总金额（扣除退款）
        :return:
        """

    def test_returnAmountTotal(self,loginManage,month):
        """
        x月退款总金额
        :return:
        """
