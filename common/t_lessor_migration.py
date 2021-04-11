import xlwings as xw
import pymysql.cursors
import logging
import time
from datetime import datetime

# 통합 앨범테이블을 실제 DB 에 넣어주는 부분
#
import pymssql
connection = pymssql.connect(server='localhost', user='sohoki', password='ki007', database='adliving',charset='utf8' ,autocommit=True,as_dict=True)


# connection = pymysql.connect(host='101.101.165.139', port=3306, user='normal_user', password='godls914',
#                              db='city_db', use_unicode=True, charset="utf8", autocommit=True,
#                              cursorclass=pymysql.cursors.DictCursor,local_infile = 1)
cursor = connection.cursor()

col_list = {} # 컬럼명 딕셔너리
col_num = 'A' #컬럼 번호
SEET_NUM = 0 #시트번호
START_ROW = 2 #시작행
start_time = time.time() # 프로세스 시작시간

# INSERT 구문
#INSERT INTO STDMAT (RAW_ALBUM_NM, ST_ALBUM_NM, ST_NEIGHBOR_RIGHTOR)
#   select RAW_ALBUM_NM, ST_ALBUM_NM, ST_NEIGHBOR_RIGHTOR from  STDMAT3 WHERE RAW_ALBUM_NM NOT IN (  SELECT RAW_ALBUM_NM FROM STDMAT )

def insertDatas(_array):
    try:
        query =   '''
  INSERT INTO t_lessor
(
district
,building_nm
,hosu
,get_dt
,lessor1
,lessor2
,sale_price
,sale_py_rating
,lessor_add
,reg_dt
,mod_dt
,sts
,reg_id
)
VALUES
(
CASE WHEN '{0}' = 'None' THEN null ELSE '{0}'END,  --
CASE WHEN '{1}' = 'None' THEN null ELSE '{1}'END,  --
CASE WHEN '{2}' = 'None' THEN null ELSE '{2}'END,  --
CASE WHEN '{3}' = 'None' THEN null ELSE '{3}'END,  --
CASE WHEN '{4}' = 'None' THEN null ELSE '{4}'END,  --
CASE WHEN '{5}' = 'None' THEN null ELSE '{5}'END,  --
CASE WHEN '{6}' = 'None' THEN null ELSE '{6}'END, -- 
CASE WHEN '{7}' = 'None' THEN null ELSE '{7}'END, -- 
CASE WHEN '{8}' = 'None' THEN null ELSE '{8}'END -- 
,getdate()
,getdate()
,'C'
,'ADMIN'

)

'''.format(_array[0],
           _array[1],
           _array[2],
           _array[3],
           _array[4],
           _array[5],
           _array[6],
           _array[7],
           _array[8])
        print(query)
        cursor.execute(query)
        # print('입력완료했습니다.',music_cd)
    except Exception as e:
        print('뭔가 발생함',e)
        logging.debug('Something bad happened', exc_info=True)

        # insertDatas(distributor, music_nm, music_cd, artist_nm, album_nm, album_cd, cost, reg_dt)
try :
    wb = xw.Book('./파이선_데이타_호수정렬.xlsx')  # connect to an existing file in the current working directory
    sht = wb.sheets[SEET_NUM]

    last_row = wb.sheets[SEET_NUM].range('A' + str(wb.sheets[SEET_NUM].cells.last_cell.row)).end('up').row
    print(last_row)

    for i in range(START_ROW, last_row+1):
        colmn = []
        colmn.append(sht.range('A' + str(i)).value)  # 권역
        colmn.append(sht.range('B' + str(i)).value)  # 빌딩명
        colmn.append(sht.range('C' + str(i)).value)  # 호수
        # colmn.append(sht.range('D' + str(i)).value)  # 분류코드
        colmn.append(sht.range('E' + str(i)).value)  # 취득일자
        colmn.append(sht.range('F' + str(i)).value)  # 임대인1
        colmn.append(sht.range('G' + str(i)).value)  # 임대인2
        # colmn.append(sht.range('H' + str(i)).value)  # 상호
        # colmn.append(sht.range('I' + str(i)).value)  # 입주일자
        # colmn.append(sht.range('J' + str(i)).value)  # 대분류
        # colmn.append(sht.range('K' + str(i)).value)  # 중분류
        # colmn.append(sht.range('L' + str(i)).value)  # 업종1
        # colmn.append(sht.range('M' + str(i)).value)  # 업종2
        colmn.append(sht.range('N' + str(i)).value)  # 매매가
        # colmn.append(sht.range('O' + str(i)).value)  # 보증금
        # colmn.append(sht.range('P' + str(i)).value)  # 월세
        # colmn.append(sht.range('Q' + str(i)).value)  # 권리금
        # colmn.append(sht.range('R' + str(i)).value)  # 관리비
        # colmn.append(sht.range('S' + str(i)).value)  # 총비용
        # colmn.append(sht.range('T' + str(i)).value)  # 평단가
        colmn.append(sht.range('U' + str(i)).value)  # 매매평단가
        # colmn.append(sht.range('V' + str(i)).value)  # 수익율
        # colmn.append(sht.range('W' + str(i)).value)  # 전용평
        # colmn.append(sht.range('X' + str(i)).value)  # 분양평
        # colmn.append(sht.range('Y' + str(i)).value)  # 전용율
        colmn.append(sht.range('Z' + str(i)).value)  # 주소
        # colmn.append(sht.range('AA' + str(i)).value)  # 전용M2
        # colmn.append(sht.range('AB' + str(i)).value)  # 분양M2
        # colmn.append(sht.range('AC' + str(i)).value)  # 공용1
        # colmn.append(sht.range('AD' + str(i)).value)  # 공용2
        # colmn.append(sht.range('AE' + str(i)).value)  # 공용3
        # colmn.append(sht.range('AF' + str(i)).value)  # 공용4
        # colmn.append(sht.range('AG' + str(i)).value)  # 공용5
        # colmn.append(sht.range('AH' + str(i)).value)  # 공용6
        # colmn.append(sht.range('AI' + str(i)).value)  # 공용7
        # colmn.append(sht.range('AJ' + str(i)).value)  # 공용합
        # print(colmn)

        insertDatas(colmn)
except Exception as e:
    print('뭔가 발생함',e)
    logging.debug('Something bad happened', exc_info=True)