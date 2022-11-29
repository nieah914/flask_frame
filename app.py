from flask import Flask
from flask_restx import Api
from model.codeMaster import CodeMaster

# static 추가
app = Flask(__name__, static_folder='./static/')
api = Api(app)

api.add_namespace(CodeMaster, '/admin/codeMaster')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port='8080')