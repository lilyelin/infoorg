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


def findProg(rbook, vJava, vPython, vC, vCPP, vR, vD3, vSQL):
	javaList = []
	pythonList = []
	cList = []
	cppList = []
	rList = []
	d3List = []
	sqlList = []
	progList = []
	tempList = []

	if vJava==True:
		progList.append('Java')
	if vPython==True:
		progList.append('Python')
	if vC==True:
		progList.append('C')
	if vCPP==True:
		progList.append('C++')
	if vR==True:
		progList.append('R')
	if vD3==True:
		progList.append('D3.js')
	if vSQL==True:
		progList.append('SQL')

	for i, elmt in enumerate(progList):
		#print(elmt)
		if elmt=='Java':
			javaList = findList(rbook, elmt)
			tempList.append(javaList)
		elif elmt=='Python':
			pythonList = findList(rbook, elmt)
			tempList.append(pythonList)
		elif elmt=='C':
			cList = findList(rbook, elmt)
			tempList.append(cList)
		elif elmt=='C++':
			cppList = findList(rbook, elmt)
			tempList.append(cppList)
		elif elmt=='R':
			rList = findList(rbook, elmt)
			tempList.append(rList)
		elif elmt=='D3.js':
			d3List = findList(rbook, elmt)
			tempList.append(d3List)
		elif elmt=='SQL':
			sqlList = findList(rbook, elmt)
			tempList.append(sqlList)
		else:
			print("Error Progaming types!")

	progList = set(tempList[0])
	for s in tempList[1:]:
		progList.intersection_update(s)

	print(javaList)
	print(pythonList)
	print(cList)
	print(cppList)
	print(rList)
	print(d3List)
	print(sqlList)
	#print(progList)
	return progList

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

	# DEBUG: check input arguments
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
	progList = []
	if (vMode==1):
		progList = findProg(rbook, vJava, vPython, vC, vCPP, vR, vD3, vSQL)
	print(progList)

	# DEBUG: check function 1
	
	for i, elmt in enumerate(progList):
		print(rbook['Name'][elmt])
	


main()