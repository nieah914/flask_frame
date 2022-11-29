from flask import request
from flask_restx import Resource, Api, Namespace

CodeMaster = Namespace(name='CodeMaster', description="코드마스터를 이용한 관리를 위한 부분")

@CodeMaster.route('/groupCode')
class CodeMasterGet(Resource):
    def get(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT' :
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
        print('/groupCode')
        return "200"

    def put(self):
        parameters = ''
        if request.method == 'POST' or request.method == 'PUT' :
            parameter_dict = request.form.to_dict()
        else:
            parameter_dict = request.args.to_dict()
            for key in parameter_dict.keys():
                parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

        return {}, 202

    def post(self):
        params = {}
        params.update(request.form)
        return {}, 200