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





if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port='8080')