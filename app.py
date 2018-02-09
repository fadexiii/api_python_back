# _*_ coding:utf-8 _*_
from flask import Flask, jsonify
from flask_restful import Api
from common.apiException import APIException
from resources.login import Login
from config import config

app = Flask(__name__)


# 异常处理
@app.errorhandler(APIException)
def handle_api_exception(error):
    result = jsonify(error.to_dict())
    return result, error.status


# 各项插件的配置
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']  # 配置数据库

api = Api(app)
api.add_resource(Login, '/login')

if __name__ == '__main__':
    from database import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
