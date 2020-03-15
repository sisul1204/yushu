#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@author:sisul
#@time:2020/3/12:16:09
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user