from flask_restx import Resource, Api, Namespace
from sql.sql_tools import QueryManager
import json
import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import datetime
Main = Namespace(
    name='Main',
    description="코드마스터를 이용한 관리를 위한 부분"
)

@Main.route('/test2')
class MainApi(Resource):

    def get(self):
        parameter_dict = request.args.to_dict()
        if len(parameter_dict) == 0:
            return 'No parameter'

        parameters = ''
        for key in parameter_dict.keys():
            parameters += 'key: {}, value: {}\n'.format(key, request.args[key])


        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'get.store.list')
        qm.addInputs(parameter_dict)
        qm.service()
        results = qm.serviceResults()

        if len(results) > 0:
            print('1.....')
            return results
        else :
            print('2.....')
            return {},200


@Main.route('/lessor_detail')
class LesseeDetail(Resource):
    def put(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT':
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

        if len(parameter_dict) == 0:
            return 'No parameter'


        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'update.lessor.detail')
        qm.addInputs(parameter_dict)
        qm.serviceUpdate()
        return {}, 200


@Main.route('/lessee_detail')
class LessorDetail(Resource):
    def put(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT':
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])



        if len(parameter_dict) == 0:
            return 'No parameter'


        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'update.lessee.detail')
        qm.addInputs(parameter_dict)
        qm.serviceUpdate()
        return {}, 200

@Main.route('/mamul_detail/delete')
class deleteMamulDetail(Resource):

    def delete(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'DELETE':
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

        if len(parameter_dict) == 0:
            return 'No parameter'

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'delete.store.detail')
        qm.addInputs(parameter_dict)
        qm.serviceUpdate()

        return {}, 200

@Main.route('/mamul_detail/insert')
class insertMamulDetail(Resource):

    def put(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT':
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

        if len(parameter_dict) == 0:
            return 'No parameter'

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'get.store.detail')
        qm.addInputs(parameter_dict)
        qm.service()
        results = qm.serviceResults()

        # 있으면 update
        if len(results) > 0:
            qm = QueryManager()
            qm.service_get_query('dashboard', 'sql_dashboard', 'update.store.detail')
            qm.addInputs(parameter_dict)
            qm.serviceUpdate()
            return {}, 200
        # 없으면 insert
        else:
            qm = QueryManager()
            qm.service_get_query('dashboard', 'sql_dashboard', 'insert.store.detail')
            qm.addInputs(parameter_dict)
            qm.serviceUpdate()
            return {}, 200


@Main.route('/mamul_detail')
class getMamulDetail(Resource):
    def get(self):
        parameter_dict = request.args.to_dict()
        if len(parameter_dict) == 0:
            return 'No parameter'

        parameters = ''
        for key in parameter_dict.keys():
            parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'get.store.detail')
        qm.addInputs(parameter_dict)
        qm.service()
        results = qm.serviceResults()
        if len(results) > 0:
            return results
        else :
            return {},200

    def put(self):
        parameters = ''
        print("====================================")
        if request.method == 'POST' or request.method == 'PUT':
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
        print(parameters)


        if len(parameter_dict) == 0:
            return 'No parameter'


        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'update.store.detail')
        qm.addInputs(parameter_dict)
        qm.serviceUpdate()
        return {}, 200

@Main.route('/store_image')
class getStoreImage(Resource):
    def get(self):
        parameter_dict = request.args.to_dict()
        if len(parameter_dict) == 0:
            return 'No parameter'

        parameters = ''
        for key in parameter_dict.keys():
            parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'get.store.image')
        qm.addInputs(parameter_dict)
        qm.service()
        results = qm.serviceResults()
        if len(results) > 0:
            return results
        else :
            return {},200

@Main.route('/delete_image', methods=['DELETE'])
class deleteStoreImage(Resource):
    def delete(self):
        parameters = ''
        if request.method == 'DELETE':
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'delete.image')
        qm.addInputs(parameter_dict)
        qm.serviceUpdate()
@Main.route('/insert_image', methods=['POST','PUT'])
class insertStoreImage(Resource):


    def post(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT':
            parameter_dict = request.form.to_dict()
            # file = request.files['file']
            # print(file.filename)
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

        # print('111111')
        # if len(parameter_dict) == 0:
        #     return 'No parameter'
        # print('111122')

        now = datetime.datetime.now()
        yyyymmdd = now.strftime("%Y%m%d")

        image_path = './static/uploads/' + yyyymmdd
        parameter_dict['image_path'] = image_path
        print("0번째")
        file = request.files['file']
        print("1번째")
        # 파일 암호화
        # filename = secure_filename(file.filename)
        parameter_dict['filename'] = file.filename
        print("2번째")
        os.makedirs(image_path ,exist_ok=True)
        print("3번째")
        file.save(os.path.join(image_path, file.filename))
        print("4번째")

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'insert.image')
        qm.addInputs(parameter_dict)
        qm.serviceUpdate()

        return{},200

# # 파일 업로드
# @Main.route('/fileupload', methods=['POST'])
# def file_upload():
#     file = request.files['file']
#
#     filename = secure_filename(file.filename)
#     os.makedirs("image_path", exists_ok=True)
#     file.save(os.path.join("image_path", filename))
#     return

@Main.route('/common/detailCode')
class Common(Resource):
    def get(self):
        param = {"group_cd":"M01"}
        qm = QueryManager()
        qm.service_get_query('common', 'sql_dashboard', 'getCommonDetailCode')
        qm.addInputs(param)
        qm.service()
        results = qm.serviceResults()
        if len(results) > 0:
            print('1.....')
            return results
        else :
            print('2.....')
            return {},202