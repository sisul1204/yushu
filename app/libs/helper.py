#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@author:sisul
#@time:2020/3/12:13:57


def is_isbn_or_key(word):
    """
        q:普通关键字，isbn
        page:
        :return:
        """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key