#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@author:sisul
#@time:2020/3/12:11:16

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)
