# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/14 14:57

from flask import Flask, current_app

app = Flask(__name__)


# ctx = app.app_context()
# ctx.push()
# a = current_app
#
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    d = a.config['DEBUG']


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')
        b = 2
        return False

    def query(self):
        print('query data')
try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as e:
    pass