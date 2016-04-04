# -*- coding: UTF-8 -*-
# !/bin/python2

# name: Multithreaded Txt Search
# author: Shaffer John
# homepage: http://www.shaffer.cn

import os
import sys, getopt
from multiprocessing import Pool,freeze_support

opts, args = getopt.getopt(sys.argv[1:], "d:s:t:")
for op, value in opts:
	if op == "-d":
		folderpath = value
	if op == "-s":
		querystr = value
	if op == "-t":
		maxthreads = int(value)

# folderpath="./file"
# querystr="shaffer"
# maxthreads=2

def searchinfile(file):
	ret_val=list()
	i=0
	print "Searching in:"+file
	for line in open(file,'r').readlines():
		i+=1
		if line.find(querystr)!=-1:
			print "IN LINE: "+str(i)+" MATCH FOUND :"+line
			ret_val.append(line)
	return ret_val

if __name__ == '__main__':
	#for windows compatibility
	freeze_support()
	#work pool
	pool=Pool(maxthreads)
	#get file paths list
	filepaths=list()
	for root, _, files in os.walk(folderpath):
		for name in files:
			filepaths.append(os.path.join(root,name))
	#launch workers
	res=pool.map(searchinfile,filepaths)
	#extract results
	for ls in res:
		for ln in ls:
			print ln