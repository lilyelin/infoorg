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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#-------------------- make inverted index --------------------#
# might be included later
"""
Input: a list of movies descriptions as strings
Output: a dictionary that maps each word in any document to the set consisting of the
		movie ids (ie, the index in the strlist) for all movie descriptions containing the word.
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

	# DEBUG: check each program list
	"""
	print(javaList)
	print(pythonList)
	print(cList)
	print(cppList)
	print(rList)
	print(d3List)
	print(sqlList)
	#print(progList)
	"""
	return progList

"""
def findTFIDF():
	tfidf = TfidfVectorizer().fit_transform(description_list)
	tfidf

def cosSim():
	cosine_similarities = cosine_similarity(tfidf[0:1], tfidf).flatten()
	cosine_similarities

	most_similar_movie_indices = cosine_similarities.argsort()[:-5:-1]
	most_similar_movie_indices

	cosine_similarities[most_similar_movie_indices]

def findSim(rbook):
	sim_list = list(rbook.Interests+' '+rbook.Industry+' '+rbook.Tools+' '+rbook['Undergrad Majors']+' '+rbook['Seeking (Intern, Full-time)'])
	#print(sim_list)
"""

def sameInterest(rbook, name):
	cand_list =[]
	new_list = []
	cand_index = rbook.loc[rbook['Name']==name].index[0]
	#print(cand_index)
	#print(name)

	for i, elmt in enumerate(rbook['Name']):
		if rbook['Product Management'][cand_index]==True:
			if rbook['Product Management'][i]==True:
				cand_list.append(i)
		if rbook['Data Science'][cand_index]==True:
			if rbook['Data Science'][i]==True:
				cand_list.append(i)
		if rbook['Policy'][cand_index]==True:
			if rbook['Policy'][i]==True:
				cand_list.append(i)
		if rbook['User Experience'][cand_index]==True:
			if rbook['User Experience'][i]==True:
				cand_list.append(i)
		if rbook['Consulting'][cand_index]==True:
			if rbook['Consulting'][i]==True:
				cand_list.append(i)
		if rbook['Engineering'][cand_index]==True:
			if rbook['Engineering'][i]==True:
				cand_list.append(i)

	for i in cand_list:
		if i not in new_list:
			new_list.append(i)
	new_list.remove(cand_index)
	#print(cand_list)
	#print(new_list)
	return new_list


#-------------------- main --------------------#
# Usage: python readfile.py 1 --java True --python True --c True --cpp True --r True --d3 True --sql True
def main():
	# read arguments
	# ex: python xx.py 1 --java True --python False
	#if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("mode", help="mode", choices=["1", "2", "3", "4"])
	parser.add_argument("--java", help="java", choices=["True", "False"], default=False)
	parser.add_argument("--python", help="python", choices=["True", "False"], default=False)
	parser.add_argument("--c", help="c", choices=["True", "False"], default=False)
	parser.add_argument("--cpp", help="cpp", choices=["True", "False"], default=False)
	parser.add_argument("--r", help="r", choices=["True", "False"], default=False)
	parser.add_argument("--d3", help="d3", choices=["True", "False"], default=False)
	parser.add_argument("--sql", help="sql", choices=["True", "False"], default=False)
	parser.add_argument("--name", help="name", default='Dylan R. Fox')

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
	nameList = [1, 2, 3]
	if (vMode==1):
		nameList = findProg(rbook, vJava, vPython, vC, vCPP, vR, vD3, vSQL)
	elif (vMode==2):
		#find similar
		print("Mode 2")
	elif (vMode==3):
		#find dissimilar
		print("Mode 3")
	elif (vMode==4):
		#find same interest
		print("Mode 4")
		nameList = sameInterest(rbook, vName)

	# OUTPUT: name list
	print()
	print("Output:")
	for i, elmt in enumerate(nameList):
		print(rbook['Name'][elmt])
	

main()