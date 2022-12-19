#!/usr/bin/env python
#-*- coding:utf-8 -*-

def find_all_char(text):
	tab=""
	for char in text:
		if char not in tab : tab=tab+char
	print(tab)




text="lkd,fscklnvkezjfnvlkdk,"
find_all_char(text)