#-*- coding: EUC-KR -*-
import pymysql.cursors
import os,sys
from common.logger import LOGGER
import json
from common import utils
import pymssql

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class DBO(LOGGER) :
    def __init__(self):
        try:
            print('class DBO(LOGGER) :')
            self.util = utils.Utills()
            with open(resource_path('./conf/conf.json')) as json_file:
                db_info = json.load(json_file)["db_info"]
            super().__init__()  # 부모클래스의 __init__ 메소드 호출
            _host = db_info["host"]
            _port = db_info["port"]
            _db_user_id = db_info['user']
            _db_user_pass = db_info['password']
            _db = db_info['database']
            _charset = db_info['charset']
            _auto_commit = db_info['autocommit']
            _lacal_infile = 1

            self.__connection = pymssql.connect(server=_host
                                                , user=_db_user_id
                                                , password=_db_user_pass
                                                , database=_db
                                                , charset='utf8'
                                                , autocommit=_auto_commit, as_dict=True)
            print("ggg")
        except Exception as e:
            self.util.print_error_log(str(e))

    def log_update(self,_desc):
        # 데이터 업데이트
        try:
            self.cursor = self.__connection.cursor()
            self.cursor.execute( 'INSERT INTO t_logs (desc) values (%s)',_desc)
            self.cursor.close()

        except Exception as e:
            self.util.print_error_log(str(e))

    # 데이터 업데이트
    def update(self,_query,_param=[]):
        try:
            self.cursor = self.__connection.cursor()
            # self.util.print_query(_query, _param)
            self.cursor.execute(_query, _param)
            # DB 연결 닫기
            self.cursor.close()

            self.logger.debug('업데이트가 끝났습니다.')
        except Exception as e:
            self.log_update(e.__doc__ + ' '+ e.__str__())
            self.util.print_error_log(str(e))


    # 컬렉션 로드
    def getQueryList(self,_query):
        print("def getQueryList(self,_query):")
        try:

            self.cursor = self.__connection.cursor()
            self.cursor.execute(_query)
            result = self.cursor.fetchall()
            # DB 연결 닫기
            self.cursor.close()
            self.logger.debug('업데이트가 끝났습니다.')
            return result
        except Exception as e:
            print("[error] : " + str(e))
            self.log_update(e.__doc__ + ' '+ e.__str__())
            self.util.print_error_log(str(e))

    # 아이템 로드
    def getQuery(self,_query,_param=[]):
        try:
            self.cursor = self.__connection.cursor()
            # self.util.print_query(_query, _param)
            self.cursor.execute(_query, _param)

            result = self.cursor.fetchone()

            # DB 연결 닫기
            self.cursor.close()
            return result
        except Exception as e:
            self.log_update(e.__doc__ + ' '+ e.__str__())
