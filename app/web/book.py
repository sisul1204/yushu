#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: sisul
# @time:2020/3/12:15:55
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm


@web.route('/book/search')
def search():

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)