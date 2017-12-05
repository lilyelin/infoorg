# import Library
import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from sklearn import feature_extraction

from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from itertools import chain
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

import os.path
import argparse


#-------------------- make inverted index --------------------#
"""
Input: a list of movies descriptions as strings
Output: a dictionary that maps each word in any document to the set consisting of the
		movie ids (ie, the index in the strlist) for all movie descriptions containing the word.

Example:
>>> makeInvertedIndex(['hello world','hello','hello cat','hellolot of cats'])
>>> {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
"""
def makeInvertedIndex(strlist):
	
	#strlist = strlist[:3]
	InvDict = {}
	for tweetKey, tweetText in enumerate(strlist):
		for word in tweetText.split():
		#for word in tweetText.lower().split():
			if InvDict.get(word,False):
				if tweetKey not in InvDict[word]:
					InvDict[word].append(tweetKey)
			else:
				InvDict[word] = [tweetKey]
	return InvDict


def findList(df, prog):
	tempList = []
	for i, elmt in enumerate(df[prog]):
		if elmt==True:
			tempList.append(i)
	return tempList



#-------------------- main --------------------#
# Usage: python readfile.py 1 --java True --python True --c True --cpp True --r True --d3 True --sql True
def main():
	# read arguments
	# ex: python xx.py 1 --java True --python False
	#if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("mode", help="mode", choices=["1", "2", "3"])
	parser.add_argument("--java", help="java", choices=["True", "False"], default=False)
	parser.add_argument("--python", help="python", choices=["True", "False"], default=False)
	parser.add_argument("--c", help="c", choices=["True", "False"], default=False)
	parser.add_argument("--cpp", help="cpp", choices=["True", "False"], default=False)
	parser.add_argument("--r", help="r", choices=["True", "False"], default=False)
	parser.add_argument("--d3", help="d3", choices=["True", "False"], default=False)
	parser.add_argument("--sql", help="sql", choices=["True", "False"], default=False)
	parser.add_argument("--name", help="name")

	args = parser.parse_args()

	"""
	print("============================")
	print("Mode: ", args.mode)
	print("Java: ", args.java)
	print("Python: ", args.python)
	print("C: ", args.c)
	print("CPP: ", args.cpp)
	print("R: ", args.r)
	print("D3: ", args.d3)
	print("SQL: ", args.sql)
	print("Name: ", args.name)
	"""

	vMode = int(args.mode)
	vJava = bool(args.java)
	vPython = bool(args.python)
	vC = bool(args.c)
	vCPP = bool(args.cpp)
	vR = bool(args.r)
	vD3 = bool(args.d3)
	vSQL = bool(args.sql)
	vName = str(args.name)

	# BUG: "--python False" does not work but it's okay just don't type "--python"
	"""
	print("============================")
	print(vMode, vJava, vPython, vC, vCPP, vR, vD3, vSQL)
	print(vName)
	"""

	# load dataset
	fname = "Info Org - Resume Data - Final.csv"
	if(os.path.isfile(fname) == False):
		print("File does NOT exist!")

	rbook = pd.read_csv(fname, low_memory=False, encoding = "ISO-8859-1")
	#rbook = rbook.head() #temp for debug
	rows, column = rbook.shape
	#print(rbook)
	#print(rows)
	#print(column)
	#print(rbook.columns)
	# 
	#print(rbook.Java)
	#print(rbook['Java'])

	"""
	javaList = []
	if vJava==True:
		lookup = 'Java'
		for i, elmt in enumerate(rbook[lookup]):
			if elmt==True:
				javaList.append(i)
				#print(i, rbook['Name'][i])
	print(javaList)
	"""

	javaList = []
	if vJava==True:
		lookup = 'Java'
		javaList = findList(rbook, lookup)
	print(javaList)

	pythonList = []
	if vPython==True:
		lookup = 'Python'
		pythonList = findList(rbook, lookup)
	print(pythonList)

	cList = []
	if vC==True:
		lookup = 'C'
		cList = findList(rbook, lookup)
	print(cList)

	cppList = []
	if vCPP==True:
		lookup = 'C++'
		cppList = findList(rbook, lookup)
	print(cppList)

	rList = []
	if vR==True:
		lookup = 'R'
		rList = findList(rbook, lookup)
	print(rList)

	d3List = []
	if vD3==True:
		lookup = 'D3.js'
		d3List = findList(rbook, lookup)
	print(d3List)

	sqlList = []
	if vSQL==True:
		lookup = 'SQL'
		sqlList = findList(rbook, lookup)
	print(sqlList)




main()