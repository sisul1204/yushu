#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@author:sisul
#@time:2020/3/12:14:07
import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
