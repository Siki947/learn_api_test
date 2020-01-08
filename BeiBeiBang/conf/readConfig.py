import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        with open(configPath,'r') as fd:
            data = fd.read()
            #  remove BOM
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                with codecs.open(configPath, "w") as file:
                    file.write(data)
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    # def set_headers(self, name, value):
    #     self.cf.set("HEADERS", name, value)
    #     with open(configPath, 'w+') as f:
    #         self.cf.write(f)

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value


    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

