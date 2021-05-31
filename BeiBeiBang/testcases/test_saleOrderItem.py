from common import configDB
from common import Log
from common import readSQL
import pytest


def select_create_order():
    my_bd = configDB.MyDB()
    my_bd.connectDB()
    my_sql = readSQL.ReadSQL()
    sql = my_sql.get_sql("prd", "sale_order", "select_sale_order_in_day")
    my_cursor = my_bd.executeSQL(sql)
    sale_order_amount_detail = my_bd.get_all(my_cursor)
    my_bd.closeDB()
    return sale_order_amount_detail

def get_sale_order_id():
   return [ i[0] for i in select_create_order()]

class TestSaleOrderItem():

    log = Log.MyLog.get_log()
    logger = log.get_logger()
    my_bd = configDB.MyDB()
    my_bd.connectDB()
    my_sql = readSQL.ReadSQL()

    def teardown_class(self):
        self.my_bd.closeDB()


    def select_sale_order_item(self,sale_order_id):

        sql = self.my_sql.get_sql("prd","sale_order_item","select_sale_order_item_sum")%sale_order_id
        my_cursor = self.my_bd.executeSQL(sql)
        sale_order_item_sum =[int(i) for i in self.my_bd.get_all(my_cursor)[0]]
        return sale_order_item_sum

    def select_sale_order_item_compare(self,sale_order_id):

        sql = self.my_sql.get_sql("prd", "sale_order_item", "select_sale_order_item_compare") % sale_order_id
        my_cursor = self.my_bd.executeSQL(sql)
        sale_order_item_compare = self.my_bd.get_all(my_cursor)
        return sale_order_item_compare

    def select_sale_order_item_detail(self,sale_order_id):

        sql = self.my_sql.get_sql("prd", "sale_order_item", "select_sale_order_item_detail") % sale_order_id
        my_cursor =self.my_bd.executeSQL(sql)
        sale_order_item_detail = self.my_bd.get_all(my_cursor)
        return sale_order_item_detail


    @pytest.mark.parametrize("sale_order_id",get_sale_order_id())
    def test_item_distribution(self,sale_order_id):
        """
        检查sale_order_item中一个item的红包+余额+现金+vip+优惠券的金额是否与商品价格*item数量一致
        :param sale_order_id:
        :return:
        """
        for i in self.select_sale_order_item_compare(sale_order_id):
            _, sale_order_item_id,item_price,total_amount=i
            if item_price == total_amount:
                assert True,"订单id为：%s的订单，sale_order_item_id的红包余额+折扣总价与商品金额*item的数量一致"%sale_order_item_id
            else:
                assert False,"订单id为：%s的订单，sale_order_item_id的红包余额+折扣总价与商品金额*item的数量不一致"%sale_order_item_id

    @pytest.mark.parametrize("sale_order_id,vip_discount_amount,discount_amount,final_total_amount,balance_use,redpacket_use",list(select_create_order()))
    def test_item_total_amount_and_discount(self,sale_order_id,vip_discount_amount,discount_amount,final_total_amount,balance_use,redpacket_use):
        """
        检查订单的sale_order_item的现金、红包、余额、vip折扣、优惠券折扣总金额是否与该订单sale_order表中一致
        :param sale_order_id:
        :param vip_discount_amount:
        :param discount_amount:
        :param final_total_amount:
        :param balance_use:
        :param redpacket_use:
        :return:
        """
        _,item_vip_discount_amount,item_discount_amount,item_final_amount,item_redpacket_amount,item_balance_amount=self.select_sale_order_item(sale_order_id)
        if vip_discount_amount == item_vip_discount_amount and discount_amount==item_discount_amount and final_total_amount==item_final_amount and balance_use==item_balance_amount and redpacket_use == item_redpacket_amount:
            assert True ,"订单id为：%s 的订单，item金额总数与sale_order金额一致"%sale_order_id
        else:
            assert False,"订单id为：%s 的订单，item金额总数与sale_order金额不一致"%sale_order_id

    @pytest.mark.parametrize("sale_order_id",get_sale_order_id())
    def test_discount_negative(self,sale_order_id):
        """
        检查sale_order_item中会员折扣和优惠券分配有没有负数
        :param sale_order_id:
        :return:
        """
        sale_order_item =self.select_sale_order_item_detail(sale_order_id)
        for i in sale_order_item:
            _,vip_discount_amount,discount_amount,_,_,_=i
            if vip_discount_amount >= 0 and discount_amount >= 0:
                assert True,"订单id为：%s的订单，会员折扣和优惠折扣金额没有负数"%sale_order_id
            else:
                assert False,"订单id为：%s的订单，会员折扣和优惠折扣金额有负数"%sale_order_id



# if __name__ == '__main__':
#     pytest.main(["-s", "test_bd_tool.py",'--html=D:/learn_api_test/BeiBeiBang/report/report.html'],
#                 ['--self-contained-html'],["--maxfail=5"])