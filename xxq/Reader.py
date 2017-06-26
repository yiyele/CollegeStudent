# -*- coding: utf-8 -*-
'''
Created on 2017年6月26日

@author: USER
'''

import os
from Participle import *

#读取数据，并对数据进行整理。
def readFiles(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        readFile(child)
         

def readFile(filename):
    x_trian = []
    y_trian = []
    print (filename)
    fopen = open(filename, 'r',encoding= 'utf-8') 
    for eachLine in fopen.readlines():
        print ("读取到得内容如下：",eachLine)
        print (' '.join(participle(eachLine)))
        x_trian.append(' '.join(participle(eachLine)))
    fopen.close()
    