from flask import request
from flask_restx import Resource, Api, Namespace
from sql.sql_tools import QueryManager

CodeMaster = Namespace(name='CodeMaster', description="코드마스터를 이용한 관리를 위한 부분")

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