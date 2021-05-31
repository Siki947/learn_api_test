import redis
import conf.readConfig as readConfig
from common.Log import MyLog as Log



class MyRedis():

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.my_redis = None


    def connect_redis(self):
        localReadConfig = readConfig.ReadConfig()
        my_host = localReadConfig.get_redis("host")
        my_port = localReadConfig.get_redis("port")
        try:
            pool = redis.ConnectionPool(host=my_host,port= my_port,max_connections=100)
            self.my_redis = redis.Redis(connection_pool=pool)
            self.logger.info("Connect Redis successfully!")
            return self.my_redis
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def execute_pipe(self):
        pipe = self.my_redis.pipeline(transaction=True)
        pipe.execute()

    def insert_value(self,key,value):
        arr = {"int": "整数", "float": "浮点", "str": "字符串", "list": "列表", "tuple": "元组", "dict": "字典", "set": "集合"}
        vartype = self.typeof(value)
        if not (vartype in arr):
            self.my_redis.set(str(key), str(value), nx=True)
        else:
            self.my_redis.set(key,value,nx=True)

    def modify_value(self,key,value):
           self.my_redis.set(str(key),str(value), nx=True)

    def typeof(self,variate):
        type = None
        if isinstance(variate, int):
            type = "int"
        elif isinstance(variate, str):
            type = "str"
        elif isinstance(variate, float):
            type = "float"
        elif isinstance(variate, list):
            type = "list"
        elif isinstance(variate, tuple):
            type = "tuple"
        elif isinstance(variate, dict):
            type = "dict"
        elif isinstance(variate, set):
            type = "set"
        return type

    def get_value(self,key):
        value = self.my_redis.get(key)
        return value


if __name__ == '__main__':
    my_redis = MyRedis()
    my_redis.connect_redis()
    my_redis.insert_value(7807,100)
    print(my_redis.get_value(7807))