#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: sisul
# @time:2020/3/12:15:55
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(q, page):

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)