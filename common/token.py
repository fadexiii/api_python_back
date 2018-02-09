# _*_ coding:utf-8 _*_
from flask import request
from common.apiException import APIException
# from app import db
# from models.user import User


def validate(func):
    def wrapper(*args, **kwargs):
        token = ''
        if request.headers.get('token'):
            token = request.headers.get('token')
        elif request.args.get('token'):
            token = request.args.get('token')
        elif request.json.has_key('token'):
            token = request.json['token']

        if token == '':
            raise APIException("token缺失", 202)

        print token
        return func(*args, **kwargs)

    return wrapper
