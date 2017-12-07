from helper import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

######################
# Modes 2 and 3
# Using TFIDF to get cosine similarity, where elements
# are all text are row data.
# 
# Future implementation may be to consider using text
# as all text in pdf of resumes
######################



#-------------------- Function 2 --------------------#
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
"""

def findSim(rbook, name, N, options=None):
	nameList = []
	sim_list = list(rbook.Industry+' '+rbook.Interests+' '+rbook.Tools+' '+rbook['Undergrad Majors']+' '+rbook['Seeking (Intern, Full-time)'])
	for i, elmt in enumerate(sim_list):
		if (rbook['UX Designer'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Designer'
		if (rbook['UX Researcher'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Researcher'
		if (rbook['Databases'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Databases'
		if (rbook['Machine Learning'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Machine Learning'
		if (rbook['Data warehousing'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Data warehousing'
		if (rbook['Leadership'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Leadership'
		if (rbook['Business'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Business'
		if (rbook['Teamwork'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Teamwork'
	tfidf = TfidfVectorizer().fit_transform(sim_list)
	cand_index = rbook.loc[rbook['Name']==name].index[0]
	cosine_similarities = cosine_similarity(tfidf[cand_index:cand_index+1], tfidf).flatten()
	most_similar_ppl = cosine_similarities.argsort()[:-N-2:-1]
	sim_names = get_names(test, most_similar_ppl, name)
	select_cr = cosine_similarities[cosine_similarities.argsort()][:-N-2:-1][1:]
	if options == 'verbose':
		return sim_names, select_cr
	else:
		return sim_names
	#return most_similar_ppl

#-------------------- Function 3 --------------------#
def findDis(rbook, name, N, options=None):
	nameList = []
	sim_list = list(rbook.Industry+' '+rbook.Interests+' '+rbook.Tools+' '+rbook['Undergrad Majors']+' '+rbook['Seeking (Intern, Full-time)'])
	for i, elmt in enumerate(sim_list):
		if (rbook['UX Designer'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Designer'
		if (rbook['UX Researcher'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Researcher'
		if (rbook['Databases'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Databases'
		if (rbook['Machine Learning'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Machine Learning'
		if (rbook['Data warehousing'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Data warehousing'
		if (rbook['Leadership'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Leadership'
		if (rbook['Business'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Business'
		if (rbook['Teamwork'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Teamwork'
	tfidf = TfidfVectorizer().fit_transform(sim_list)
	cand_index = rbook.loc[rbook['Name']==name].index[0]
	cosine_similarities = cosine_similarity(tfidf[cand_index:cand_index+1], tfidf).flatten()
	most_similar_ppl = cosine_similarities.argsort()[:N:1]
	sim_names = get_names(test, most_similar_ppl, name)
	select_cr = cosine_similarities[cosine_similarities.argsort()][:N:1]
	if options == 'verbose':
		return sim_names, select_cr
	else:
		return sim_names
	#return most_similar_ppl