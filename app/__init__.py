#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@author:sisul
#@time:2020/3/12:16:08
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app
