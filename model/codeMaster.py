from flask import request
from flask_restx import Resource, Api, Namespace
from sql.sql_tools import QueryManager
import json

CodeMaster = Namespace(name='CodeMaster',
                       description="코드마스터를 이용한 관리를 위한 부분"
                       )





@CodeMaster.route('/groupCode')
class CodeMasterGet(Resource):
    def get(self):
        print('/groupCode')
        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'getGroupCode')
        qm.addInputs([])
        qm.service()

        results = qm.serviceResults()
        print(results)
        # json_val = json.dumps(results)
        return results

    def put(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT' :
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
            print(parameters)
        print(parameter_dict)

        print('111111')
        if len(parameter_dict) == 0:
            return 'No parameter'
        print('111122')

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'updateGroupCode')
        qm.addInputs(parameter_dict)
        qm.service()
        return {}, 202

    def post(self):
        params = {}
        params.update(request.form)

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'insertGroupCode')
        qm.addInputs(params)
        qm.serviceUpdate()
        results = qm.serviceResults()
        return {}, 200
@CodeMaster.route('/detailCode')
class CodeMasterGet(Resource):
    def get(self):
        parameter_dict = request.args.to_dict()
        if len(parameter_dict) == 0:
            return 'No parameter'

        parameters = ''
        for key in parameter_dict.keys():
            parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
        print(parameters)

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'getGroupDetailCode')
        qm.addInputs(parameter_dict)
        qm.service()
        results = qm.serviceResults()
        if len(results) > 0:
            print('1.....')
            return results
        else :
            print('2.....')
            return {},200

    def put(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT':
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
            print(parameters)
        print(parameter_dict)

        print('111111')
        if len(parameter_dict) == 0:
            return 'No parameter'
        print('111122')

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'updateDetailCode')
        qm.addInputs(parameter_dict)
        qm.service()
        return {}, 200

    def post(self):
        params = {}
        params.update(request.form)

        qm = QueryManager()
        qm.service_get_query('dashboard', 'sql_dashboard', 'insertDetailGroupCode')
        qm.addInputs(params)
        qm.serviceUpdate()
        results = qm.serviceResults()
        return {}, 200
# 아래는 샘플 예제
# Todo = Namespace('Todo')
# @Todo.route('')
# class TodoPost(Resource):
#     def post(self):
#         global count
#         global todos
#
#         idx = count
#         count += 1
#         todos[idx] = request.json.get('data')
#
#         return {
#             'todo_id': idx,
#             'data': todos[idx]
#         }
#
#
# @Todo.route('/<int:todo_id>')
# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {
#             'todo_id': todo_id,
#             'data': todos[todo_id]
#         }
#
#     def put(self, todo_id):
#         todos[todo_id] = request.json.get('data')
#         return {
#             'todo_id': todo_id,
#             'data': todos[todo_id]
#         }
#
#     def delete(self, todo_id):
#         del todos[todo_id]
#         return {
#             "delete": "success"
#         }