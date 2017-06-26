# -*- coding: utf-8 -*-
'''
Created on 2017年6月26日

@author: USER
'''

import jieba

def participle(value):
    seg_list = jieba.cut(value)
    return seg_list
