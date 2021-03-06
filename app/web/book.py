#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: sisul
# @time:2020/3/12:15:55
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm
from ..view_models.book import BookViewModel


@web.route('/book/test')
def test1():
    from flask import request
    from app.libs.nonelocal import n
    print(n.v)
    n.v = 2
    print('---------------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print(request.v)
    print('---------------------')
    return ''







@web.route('/book/search')
def search():

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        return jsonify(result)
    else:
        return jsonify(form.errors)