#-*- coding: EUC-KR -*-
from common.dbcon import DBO
from common import utils
import sys,os
import xml.etree.ElementTree as elemTree

# 2021-02-23 확인한 최신본
NO_EXIST = -1
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        print(base_path)
        print(base_path)
        print(base_path)
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class QueryManager(DBO, utils.Utills):
    def __init__(self):
        super().__init__()
        print('__init__')
        self.query = ''
        self.input_param = {'user_id':'nieah914','category':'ct'}
        self.results = {}

    def service_get_query(self,_service_folder_name,_service_file_name,_service_id):
        print('service_get_query')
        tree = elemTree.parse(resource_path('./sql/' + _service_folder_name + '/' + _service_file_name + '.xml'))
        self.query = tree.find('query[@id="' + _service_id + '"]').text
        print(self.query)

    def service_set_query(self,query):
        self.query = query

    def clearIinputs(self):
        print('clearIinputs')
        self.input_param = {}


    def addInputs(self,_param):
        print('addInputs')
        self.input_param = _param



    def service(self):
        print("[service]==============================================")
        i = 0
        for key in self.input_param:
            # print("key: " + key)
            # print("val: " + self.input_param[key])
            self.query = self.query.replace("#"+key+"#","'" +self.input_param[key] + "'")

        # [ 가 있을경우
        for i in range(0,self.query.count('[')):
            i = i + 1

            start_point = self.query.find('[')
            end_point = self.query.find(']')


            # print(self.query[start_point:end_point+1])

            # #이 있을경우 즉 행을 날려야함.
            if self.query[start_point:end_point].find('#') != NO_EXIST:
                self.query = self.query[0:start_point] + self.query[end_point+1:]

            # #이 없을경우 [ 만 날려야함.
            else :
                self.query = self.query[0:start_point] + self.query[start_point+1:end_point] \
                             + self.query[end_point+1:]



        print(self.query)

        self.results = self.getQueryList(self.query)
        # print(self.results)



    def serviceUpdate(self):
        for key in self.input_param:
            self.query = self.query.replace("#"+key+"#","'" +self.input_param[key] + "'")

        # [ 가 있을경우
        for i in range(0,self.query.count('[')):
            print(i)
            i = i + 1
            start_point = self.query.find('[')
            end_point = self.query.find(']')


            print(self.query[start_point:end_point+1])

            # #이 있을경우 즉 행을 날려야함.
            if self.query[start_point:end_point].find('#') != NO_EXIST:
                self.query = self.query[0:start_point] + self.query[end_point+1:]
            # #이 없을경우 [ 만 날려야함.
            else :
                self.query = self.query[0:start_point] + self.query[start_point+1:end_point] \
                             + self.query[end_point+1:]
        print(self.query)
        self.results = self.update(self.query,[])


    def serviceResults(self):
        return self.results