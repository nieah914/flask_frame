from flask import Flask, render_template , request
from sql.sql_tools import QueryManager
import json
import asyncio
from flask_restx import Resource, Api
from model.codeMaster import CodeMaster
from model.main import Main
from model.popup.mamul import POPUP_MAMUL
# from todo import Todo
#
# app = Flask(__name__)
# api = Api(app)
#
# api.add_namespace(Todo, '/todos')
# 기본은 아래
# app = Flask(__name__)

# static 추가
app = Flask(__name__, static_folder='./static/')
api = Api(app)

api.add_namespace(CodeMaster, '/admin/codeMaster')
api.add_namespace(Main, '/')
api.add_namespace(POPUP_MAMUL, '/mamul_desc')


@app.route('/juja')
def view_juja():
    return render_template('index.html')


@app.route('/juja2')
def view_juja2():
    return render_template('widgets.html')

@app.route('/default3')
def view_default3():
    return render_template('view03.html')

@app.route('/default2')
def view_default2():
    return render_template('view02.html')

@app.route('/main')
def main():
    return render_template('view01.html')

@app.route('/test')
def test23():
    return render_template('test.html')
@app.route('/login')
def login():
    return render_template('auth_login.html')


@app.route('/mamul_desc')
def popup_mamul():
    return render_template('popup_mamul_detail.html')


@app.route('/default')
def view_default():
    return render_template('view01.html')





@app.route('/admin/codeMaster/delete', methods=['DELETE'])
def query06():
    parameters = ''
    if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE' :
        parameter_dict = request.form.to_dict()
    else:
        parameter_dict = request.args.to_dict()
        for key in parameter_dict.keys():
            parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

    if len(parameter_dict) == 0:
        return 'No parameter'

    qm = QueryManager()
    qm.service_get_query('dashboard', 'sql_dashboard', 'deleteGroupCode')
    qm.addInputs(parameter_dict)
    qm.service()
    results = qm.serviceResults()
    print("===================================")
    print(results)
    json_val = json.dumps(results)
    return json_val



@app.route('/admin/codeMaster/detailCode/delete', methods=['DELETE'])
def query07():
    parameters = ''
    if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE' :
        parameter_dict = request.form.to_dict()
    else:
        parameter_dict = request.args.to_dict()
        for key in parameter_dict.keys():
            parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

    if len(parameter_dict) == 0:
        return 'No parameter'

    qm = QueryManager()
    qm.service_get_query('dashboard', 'sql_dashboard', 'deleteDetailCode')
    qm.addInputs(parameter_dict)
    qm.service()
    results = qm.serviceResults()

    json_val = json.dumps(results)
    return json_val

# @app.route('/admin/codeMaster/update', methods=['PUT'])
# @app.route('/admin/codeMaster/delete', methods=['DELETE'])


@app.route('/test', methods=['GET'])
def main2():
    qm = QueryManager()
    qm.service_get_query('dashboard', 'sql_dashboard', 'get.email.list')
    qm.addInputs([])
    qm.service()
    results = qm.serviceResults()
    json_val = json.dumps(results)
    return json_val


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port='8080')