# _*_ coding:utf-8 _*_
from database import db


class User(db.Model):  # UserMixin是Flask-Login库中所需要的
    __tablename__ = 'users'
    # 每个属性定义一个字段
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    token = db.Column(db.String(64))
    ttl = db.Column(db.String(64))
