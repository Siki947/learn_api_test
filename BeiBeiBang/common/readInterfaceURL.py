import os
import xml.etree.ElementTree as ET

proDir = os.path.dirname(os.getcwd())
# ****************************** read interfaceURL xml ********************************
class Read_Interface_URL():
    def get_url_from_xml(name):
        """
        By name get url from interfaceURL.xml
        :param name: interface's url name
        :return: url
        """

        url_path = os.path.join(proDir, 'testFile', 'interfaceURL.xml')
        tree = ET.parse(url_path)
        for u in tree.getroot():
            url_name = u.get('name')
            if url_name == name:
                url = u.text.strip()
                break
        return url


