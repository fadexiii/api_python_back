from flask_restful import Resource
from flask import request
from common.token import validate
from database import db
from models.user import User


class Login(Resource):
    @validate
    def post(self):
        return request.json

    def get(self):
        return {'a': 1}

    def put(self):
        user = User()
        user.username = 'kx'
        user.password = '123456'
        user.token = 'ddd'
        user.ttl = '7200'

        db.session.add(user)
        db.session.commit()
        return {'message': 'add success'}
