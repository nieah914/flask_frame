import xlwings as xw
import pymysql.cursors
import logging
import time
from datetime import datetime

# 통합 앨범테이블을 실제 DB 에 넣어주는 부분
#
import pymssql


connection = pymysql.connect(host='101.101.165.139', port=3306, user='normal_user', password='godls914',
                             db='city_db', use_unicode=True, charset="utf8", autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor,local_infile = 1)
cursor = connection.cursor()
query = '''

select * from t_image limit 100
'''
cursor.execute(query)
results = cursor.fetchall()

for item in results:
    print(item)





connection = pymssql.connect(server='localhost', user='sohoki', password='ki007', database='adliving',charset='utf8' ,autocommit=True,as_dict=True)
cursor = connection.cursor()

query = '''

select top 100 * from t_store
'''
cursor.execute(query)
results = cursor.fetchall()
print(results)
