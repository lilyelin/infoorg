from helper import *

# Note that df is the df
#-------------------- Function 1 --------------------#
def findList(df, prog):
	tempList = []
	for i, elmt in enumerate(df[prog]):
		if elmt==True:
			tempList.append(i)
	return tempList

def select_intersect(collection, vJava=False, vPython=False, vC=False, vCPP=False, vR=False, vD3=False, vSQL=False):
	df = collection.df
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
			javaList = findList(df, elmt)
			tempList.append(javaList)
		elif elmt=='Python':
			pythonList = findList(df, elmt)
			tempList.append(pythonList)
		elif elmt=='C':
			cList = findList(df, elmt)
			tempList.append(cList)
		elif elmt=='C++':
			cppList = findList(df, elmt)
			tempList.append(cppList)
		elif elmt=='R':
			rList = findList(df, elmt)
			tempList.append(rList)
		elif elmt=='D3.js':
			d3List = findList(df, elmt)
			tempList.append(d3List)
		elif elmt=='SQL':
			sqlList = findList(df, elmt)
			tempList.append(sqlList)
		else:
			print("Error Programming types!")
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

#-------------------- Function 4 --------------------#
def same_career_goals(collection, name):
	df = collection.df
	cand_list =[]
	#new_list = []
	cand_index = df.loc[df['Name']==name].index[0]
	#print(cand_index)
	#print(name)
	for i, elmt in enumerate(df['Name']):
		if df['Product Management'][cand_index]==True:
			if df['Product Management'][i]==True:
				cand_list.append(i)
		if df['Data Science'][cand_index]==True:
			if df['Data Science'][i]==True:
				cand_list.append(i)
		if df['Policy'][cand_index]==True:
			if df['Policy'][i]==True:
				cand_list.append(i)
		if df['User Experience'][cand_index]==True:
			if df['User Experience'][i]==True:
				cand_list.append(i)
		if df['Consulting'][cand_index]==True:
			if df['Consulting'][i]==True:
				cand_list.append(i)
		if df['Engineering'][cand_index]==True:
			if df['Engineering'][i]==True:
				cand_list.append(i)
	"""
	for i in cand_list:
		if i not in new_list:
			new_list.append(i)
	new_list.remove(cand_index)
	"""
	#print(cand_list)
	#print(new_list)
	return cand_list