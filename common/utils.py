from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
import pymysql.cursors
import time
import os
import sys
import inspect
from datetime import datetime
from common.logger import LOGGER
import sys
import json

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


with open(resource_path('./conf/conf.json')) as json_file:
    json_info = json.load(json_file)["path"]

LOG_PATH = json_info['log_path']
TEMP_PATH = json_info['temp_path']


class Utills(LOGGER):
    def __init__(self,_mode='DEBUG'):
        super().__init__()
        self.mode = _mode
    def createFolder(self,directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. ' + directory)

    # 로그 파일 작성
    def write_log_file(self,_parameter):
        folder_path = LOG_PATH
        self.createFolder(folder_path)
        yyyymmdd = "log_" + time.strftime('%Y%m%d') + ".txt"
        log_file = open(folder_path + "/"+yyyymmdd, "a", encoding="utf-8")
        log_file.write(_parameter)
        log_file.close()

    # 임시 파일 저장
    def write_log_file(self, _parameter):
        folder_path = TEMP_PATH
        self.createFolder(folder_path)
        yyyymmdd = "log_" + time.strftime('%Y%m%d') + ".txt"
        log_file = open(folder_path + "/" + yyyymmdd, "a", encoding="utf-8")
        log_file.write(_parameter)
        log_file.close()

    # 파일 저장
    def write_log_file(self,_parameter):
        folder_path = "C:/HEEIN/logs"
        self.createFolder(folder_path)
        yyyymmdd = "log_" + time.strftime('%Y%m%d') + ".txt"
        log_file = open(folder_path + "/"+yyyymmdd, "a", encoding="utf-8")
        log_file.write(_parameter)
        log_file.close()

    def show_popup_ok(self, title: str, content: str):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec_()

    def getProjectDir(self):
        return os.path.dirname('../' + os.path.abspath(__file__))

    def call_function(self,func):
        func()
        print('function called')

    def print_common_log(self,_param=""):
        print_text = ""
        print_text +=   "*- begin --------------------------------------------------------------------------------"
        print_text += "\n|  Function Name : " + inspect.currentframe().f_back.f_code.co_name
        print_text += "\n|  Date time     : " + time.strftime('%Y-%m-%d %H:%M:%S')
        print_text += "\n|  param         : " + _param
        print_text += "\n*- end   --------------------------------------------------------------------------------\n\n"
        print(print_text)
        self.write_log_file(print_text)

    def print_log(self,_param):
        print_text = ""
        print_text +=   "*- begin --------------------------------------------------------------------------------"
        print_text += "\n|  Function Name : " + inspect.currentframe().f_back.f_code.co_name
        print_text += "\n|  Date time     : " + time.strftime('%Y-%m-%d %H:%M:%S')
        print_text += "\n|  param         : " + _param
        print_text += "\n*- end   --------------------------------------------------------------------------------\n\n"
        if self.mode == 'DEBUG':
            print(print_text)
            self.write_log_file(print_text)

    def print_query(self,_query,_param):
        print_text = ""
        print_text +=   "*- begin --------------------------------------------------------------------------------"
        print_text += "\n|  Function Name : " + inspect.currentframe().f_back.f_code.co_name
        print_text += "\n|  Date time     : " + time.strftime('%Y-%m-%d %H:%M:%S')
        print_text += "\n|  sql         : " + _query
        print_text += "\n|  param         : "
        print_text += "{"
        print(_query)
        for key, value in _param.items():
            print_text += key, ":", value +', '
        print_text += "}"
        print_text += "\n*- end   --------------------------------------------------------------------------------\n\n"
        if self.mode == 'DEBUG':
            print(print_text)
            self.write_log_file(print_text)

    def print_error_log(self,_param):
        print_text = ""
        print_text += "   Date time : " + time.strftime('%Y-%m-%d %H:%M:%S')+'\n'
        print_text += "     !! begin !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        print_text += "     !  Function Name : " + inspect.currentframe().f_back.f_code.co_name+"\n"
        print_text += "     !  exception     : " + _param+"\n"
        print_text += "     !! end   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n"

        if self.mode == 'DEBUG':
            print(print_text)
            self.write_log_file(print_text)