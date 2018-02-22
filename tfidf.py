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

def find_tfidf_sim(collection, name, N, options=None):
	df = collection.df
	nameList = []
	sim_list = list(df['Industry']+' '+df['Interests']+' '+df['Tools']+' '+df['Undergrad Majors']+' '+df['Seeking (Intern, Full-time)'])
	for i, elmt in enumerate(sim_list):
		if (df['UX Designer'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Designer'
		if (df['UX Researcher'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Researcher'
		if (df['Databases'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Databases'
		if (df['Machine Learning'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Machine Learning'
		if (df['Data warehousing'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Data warehousing'
		if (df['Leadership'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Leadership'
		if (df['Business'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Business'
		if (df['Teamwork'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Teamwork'
	tfidf = TfidfVectorizer().fit_transform(sim_list)
	cand_index = df.loc[df['Name']==name].index[0]
	cosine_similarities = cosine_similarity(tfidf[cand_index:cand_index+1], tfidf).flatten()
	most_similar_ppl = cosine_similarities.argsort()[:-N-2:-1]
	sim_names = get_names(collection, most_similar_ppl, name)
	select_cr = cosine_similarities[cosine_similarities.argsort()][:-N-2:-1][1:]
	if options == 'verbose':
		return sim_names, select_cr
	else:
		return sim_names
	#return most_similar_ppl

#-------------------- Function 3 --------------------#
def find_tfidf_dis(collection, name, N, options=None):
	df = collection.df
	nameList = []
	sim_list = list(df.Industry+' '+df.Interests+' '+df.Tools+' '+df['Undergrad Majors']+' '+df['Seeking (Intern, Full-time)'])
	for i, elmt in enumerate(sim_list):
		if (df['UX Designer'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Designer'
		if (df['UX Researcher'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' UX Researcher'
		if (df['Databases'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Databases'
		if (df['Machine Learning'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Machine Learning'
		if (df['Data warehousing'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Data warehousing'
		if (df['Leadership'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Leadership'
		if (df['Business'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Business'
		if (df['Teamwork'][i] >= 0):
			sim_list[i] = str(sim_list[i])+' Teamwork'
	tfidf = TfidfVectorizer().fit_transform(sim_list)
	cand_index = df.loc[df['Name']==name].index[0]
	cosine_similarities = cosine_similarity(tfidf[cand_index:cand_index+1], tfidf).flatten()
	most_similar_ppl = cosine_similarities.argsort()[:N:1]
	sim_names = get_names(collection, most_similar_ppl, name)
	select_cr = cosine_similarities[cosine_similarities.argsort()][:N:1]
	if options == 'verbose':
		return sim_names, select_cr
	else:
		return sim_names
	#return most_similar_ppl