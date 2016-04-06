# -*- coding: UTF-8 -*-
# !/bin/python2

# name: MD5 encrypted File of Directory Traversal
# author: Shaffer John
# homepage: http://www.shaffer.cn

import os
import sys, getopt
from hashlib import md5

def md5_file(name):
	m = md5()
	f = open(name, 'rb')    #需要使用二进制格式读取文件内容
	m.update(f.read())
	f.close()
	return name+" : "+m.hexdigest()

opts, args = getopt.getopt(sys.argv[1:], "d:o:")
for op, value in opts:
	if op == "-d":
		folderpath = value.replace('\\','/')
		# folderpath = value.replace('/',os.sep).replace('\\',os.sep)
	if op == "-o":
		output = value

filepaths=list()
f = open('test.txt', 'a')

for dirpath, dirnames, filenames in os.walk(folderpath):
	for filename in filenames:
		filepaths.append(os.path.join(dirpath,filename).replace('\\','/'))
for filename in filepaths:
	print md5_file(filename)
	f.write(md5_file(filename)+'\n')
f.close()

# Readme:
# launch with params, like:
# python md5.py -d ./file -o md5.txt
# the filename of this script is md5.py
# -d means which folder (all files in it) do you traverse
# -o output a bunch of md5 value to a certain file (append method).

# You can do what you want about this script.
# By shaffer.cn

# 使用方法：
# 带参数执行，例如python md5.py -d ./file -o md5.txt
# 脚本文件是md5.py
# -d 遍历文件夹（下的所有文件）
# -o 输出MD5值到某一文件（追加方式）

# 你可以任意修改此脚本
# By shaffer.cn