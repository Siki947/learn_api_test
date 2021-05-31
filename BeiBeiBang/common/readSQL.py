import xml.etree.ElementTree as ET
import os
from common import Log


proDir = os.path.dirname(os.getcwd())

# ****************************** read SQL xml ********************************

class ReadSQL():

    def __init__(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

        self.database = {}
        self.table = {}
        self.sql = {}

    def set_xml(self):
        """
        set sql xml
        :return:
        """

        if len(self.database) == 0:
            sql_path = os.path.join(proDir, "testFile", "SQL.xml")
            tree = ET.parse(sql_path)
            root = tree.getroot()
            # self.logger.info("root.tag : %s,root.attrib= %s"% (root.tag,root.attrib))  # 打印根元素的tag和属性
            # for child in root:
            #     self.logger.info("child = %s " % child)
            #     child.find('database')

            for db in root.findall("database"):
                db_name = db.get("name")
                # self.logger.info('bd_name : %s'% db_name)


                for tb in db.findall("table"):
                    table_name = tb.get("name")
                    # print(table_name)

                    for data in tb.findall("sql"):
                        sql_id = data.get("id")
                        # print(sql_id)
                        self.sql[sql_id] = data.text
                    self.table[table_name] = self.sql
                self.database[db_name] = self.table


    def get_xml_dict(self,database_name, table_name):
        """
        get db dict by given name
        :param database_name:
        :param table_name:
        :return:
        """
        self.set_xml()
        try:
            database_dict = self.database.get(database_name).get(table_name)
        except AttributeError as e:
            self.logger.error("SQL.xml中没有database_name为%s 或 table_name为 %s的数据" %(database_name,table_name))
            self.logger.error(e)
        return database_dict


    def get_sql(self,database_name, table_name, sql_id):
        """
        get sql by given name and sql_id
        :param database_name:
        :param table_name:
        :param sql_id:
        :return:
        """
        db = self.get_xml_dict(database_name, table_name)
        sql = db.get(sql_id)
        sql = sql.strip()
        return sql

# if __name__ == '__main__':
#     ReadSQL().get_sql("prd", "sale_order", "select_sale_order_in_day")