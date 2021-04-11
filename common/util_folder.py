import os

import xlwings as xw
import pymysql.cursors
import logging
import time
from datetime import datetime

connection = pymysql.connect(host='101.101.165.139', port=3306, user='normal_user', password='godls914',
                             db='city_db', use_unicode=True, charset="utf8", autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor,local_infile = 1)
cursor = connection.cursor()


def insertDatas(_array):
    try:
        query = '''
INSERT INTO `city_db`.`t_image`
(`district`,
`building_nm`,
`hosu`,
`category`,
`path`,
`file_nm`,
`reg_dt`,
`mod_dt`,
`reg_id`,
`sts`)
VALUES        
(
%s,  -- 권역
%s,  -- 빌딩명
%s,  -- 호수
%s,  -- 카테고리
%s,  -- 파일패스
%s,  -- 파일명
now(),
now(),
'ADMIN',
'C'
)

'''
        cursor.execute(query, _array)
        # print(_array)
        # print('입력완료했습니다.',music_cd)
    except Exception as e:
        print('뭔가 발생함', e)
        logging.debug('Something bad happened', exc_info=True)



class FolderFinder:
    def __init__(self, _inputPath='./docs/배급사별폼양식/배급사별폼.xlsx', _outputPath='./docs/Raw Data/기획사별rawdata/'):
        self.FORM_FOLDER = os.path.abspath(_inputPath)
        self.RAW_DATA_PATH = os.path.abspath(_outputPath)
# print( RAW_DATA_PATH)


    def get_folder_path_list_from(self,path):
        print('--폴더 내부 폴더리드스----------------------------------------------------------')
        print('폴더 경로 : ' + path)
        filesWithFolder = os.listdir(path)
        folderPathList = []
        for object in filesWithFolder:
            target_obejct_path = os.path.join(path, object)
            if os.path.isdir(target_obejct_path) == True:
                folderPathList.append(target_obejct_path)

        return folderPathList



    def get_folder_name_from_path(self,path):
        folder_path = path.split('/')
        return folder_path[-1]

    def get_file_name_from_file_path(self,path):
        file_path_without_ext = path.split('.')[0]
        file_name =file_path_without_ext.split('/')[-1]
        return file_name


    def get_files_path_from(self,path):
        print('--폴더 내부 폴더리드스----------------------------------------------------------')
        print('폴더 경로 : ' + path)
        files = os.listdir(path)
        for i in range(0, len(files)):
            files[i] =  os.path.join(path, files[i])
        print(files)
        print('--------------------------------------------------------------------------------')
        return files

    def get_files_from(self,folder_path):
        print('--폴더 내부 파일리스트----------------------------------------------------------')
        print('폴더 경로 : ' + folder_path)
        filenames = os.listdir(folder_path)

        return filenames

    def get_folder_name(self,folder_path):
        print(folder_path.split('\\')[-1])
        return folder_path.split('\\')[-1]


    def get_all_files_from_folder(self,_folder_path):
        file_list = []
        for root, dirs, files in os.walk(_folder_path):
            for fname in files:
                full_fname = os.path.join(root, fname)
                file_list.append(full_fname)
        return file_list


FF = FolderFinder('C:\\Users\\nieah\\Desktop\\2021년\\사이드프로젝트\\시티부동산\\건축물대장','C:\\Users\\nieah\\Desktop\\2021년\\사이드프로젝트\\시티부동산\\아웃풋')
# foler_list =FF.get_folder_path_list_from('C:\\Users\\nieah\\Desktop\\2021년\\사이드프로젝트\\시티부동산\\건축물대장')
file_list =FF.get_all_files_from_folder('C:\\Users\\nieah\\Desktop\\2021년\\사이드프로젝트\\시티부동산\\건축물대장')

for file_path in file_list:
    print(file_path)
    file_name = file_path.split('\\')[-1]
    print(file_name.split('.')[0])
    hosu = file_name.split('.')[0]
    category = file_path.split('\\')[-2]
    print(category) #건축물대장/ 도면
    building_nm = file_path.split('\\')[-3]

    server_file_path = '/uploads/' + building_nm + '/' + category + '/' + file_name
    print(server_file_path)


    parameter_dict = {}
    parameter_dict['district'] = ''
    parameter_dict['building_nm'] = building_nm
    parameter_dict['hosu'] = hosu
    parameter_dict['category'] = category
    parameter_dict['file_path'] = server_file_path
    parameter_dict['file_name'] = file_name

    param = []
    param.append(parameter_dict['district'])
    param.append(parameter_dict['building_nm'])
    param.append(parameter_dict['hosu'])
    param.append(parameter_dict['category'])
    param.append(parameter_dict['file_path'])
    param.append(parameter_dict['file_name'])
    insertDatas(param)