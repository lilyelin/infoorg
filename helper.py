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

# For shared helper functions

# ResumeCollection is df of resumes
# add additional functionality as needed
class ResumeCollection:
	rlen = None
	clen = None
	df = None

	def __init__(self, row_length, col_length, df):
		self.rlen = row_length
		self.clen = col_length
		self.df = df


# loads the dataset
# TODO: change to take in any data file
def read_dataset():
	# load dataset
	fname = "Info Org - Resume Data - Final.csv"
	if(os.path.isfile(fname) == False):
		print("File does NOT exist!")
		return None

	rbook = pd.read_csv(fname, low_memory=False, encoding = "ISO-8859-1")
	
	#rbook = rbook.head() #temp for debug
	rows, columns = rbook.shape
	resumes = ResumeCollection(rows, columns, rbook)
	return resumes

def get_names(collection, list_of_indices, name):
	df = collection.df
	new_list = []
	name_list = []
	cand_index = df.loc[df['Name']==name].index[0]
	for i in list_of_indices:
		if i not in new_list:
			new_list.append(i)
		if (i==cand_index):
			new_list.remove(i)
	for i, elmt in enumerate(new_list):
		name_list += [df['Name'][elmt]]
	return name_list

