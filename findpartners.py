from helper import *
import math
import numpy
import numpy as np


######################
# Modes 2 and 3
# create normalized values for all entries based on target person
# then determine closest and furthest based on cosine similarity
#
# Equation for cosine similarity will be
# sum of dotproduct of target vector and vector i
# divided by multiple of sqrt of sum of vector components of target vector 
# squared and sqrt of sum of vector components of vector i squared
######################

def find_sim_partners(collection, name, N, options=None):
	target_row = get_target_row(collection.df, name)
	if isinstance(target_row, pd.Series):
		cos_results = calculate_cos_sim(target_row, collection)
		sim_index = index_of_most_similar(cos_results, N)
		sim_names = convert_ind_to_names(sim_index, collection)
		if options == 'verbose':
			if N >= len(cos_results)-1:
				maxN = len(cos_results)
			else:
				maxN = N+1
			cr = np.array(cos_results)
			select_cr = cr[cr.argsort()[::-1]][1:maxN]
			return sim_names, select_cr
		else:
			return sim_names
	else:
		return None

def find_dis_partners(collection, name, N, options=None):
	target_row = get_target_row(collection.df, name)
	if isinstance(target_row, pd.Series):
		cos_results = calculate_cos_sim(target_row, collection)
		dis_index = index_of_least_similar(cos_results, N)
		dis_names = convert_ind_to_names(dis_index, collection)
		if options == 'verbose':
			cr = np.array(cos_results)
			select_cr = cr[cr.argsort()][:N]
			return dis_names, select_cr
		else:
			return dis_names
	else:
		return None


# given a name and a df, identify the row in the df that the name 
# corresponds with. Otherwise return None.
def get_target_row(df, name):
	target_index_list = df.index[df['Name']==name].tolist()
	if len(target_index_list)>=1:
		target_index = target_index_list[0]
		target_row = df.iloc[target_index]
		return target_row
	else:
		return None


# Renorm row. Given target_row and ith_row
# return values for the ith_row based upon being normalized
# against the target_row. All new values
# should fall between 0 and 1, 0 being unlike
# the target row, 1 being identical.
# If this function is applied onto the target_row
# all values should be 1.
#
# NOTE: We will be ignoring the context variables
# which are columns 1-5. We will only be using columns 6-33
# There are 34 columns, we are ignoring 0-5. 0th is the name.
# For future: Year and Seeking may be options from context
# that may be useful to include, may allow option in future
def renorm_row(target_row, ith_row):
	norm_result = []
	# column 7-12 is boolean
	# 13 is string
	# 14-21 is years of experience
	# 22-23 string
	# 24-29 is boolean
	# 30-31 is string
	# 32-33 is boolean
	for j in range(6, len(target_row)):
		target_j = target_row[j]
		ith_j = ith_row[j]
		# check for "nan"
		# if target is null then ith will be 0, since it cannot be known
		# if target is not null but ith is null, then 0, since not same
		# if either target or ith or nan, then it should be set to 0
		if target_j==ith_j:
			norm_result += [1]
		#if math.isnan(target_j) or math.isnan(ith_j):
		#	norm_result += [0]
		elif isinstance(target_j, str):
			# norm string
			#print("str")
			norm_result += [norm_strings(target_j, ith_j)]
		elif isinstance(target_j, numpy.bool_):
			# norm bool
			norm_result += [norm_boolean(target_j, ith_j)]
		elif isinstance(target_j, numpy.int64):
			# norm integer
			#print("int")
			norm_result += [norm_years_of_experience(target_j, ith_j)]
		elif isinstance(target_j, float) and isinstance(ith_j, float):
			if math.isnan(target_j) and math.isnan(ith_j):
				norm_result += [1]
			else:
				norm_result += [0]
		else:
			#something is wrong with the values here
			# do something
			norm_result += [0]
	return norm_result

# add 1 to values to shift everything
# such that False = -1 becomes 0
# and 0 as True becomes 1
# and years of experience 1/+ becomes 2/+
# divided by target value, so this is equally weighted
# additionally if ith_value is greater than target_value
# it will be treated as equal to target_value, so that we do not
# treat people with more experience the same as those with less
# Logic being that there is less differences between people 
# who are both experienced than those with less experience.
def norm_years_of_experience(target_value, ith_value):
	new_norm = 0
	adjusted_target = target_value +1
	adjusted_ith = ith_value+1
	if adjusted_ith == adjusted_target:
		new_norm = 1
	elif adjusted_ith==0 and adjusted_target==0:
		# if ith is 0 and target is 0 then 1
		new_norm = 1
	elif adjusted_ith != 0 and adjusted_target == 0:
		# if target is 0 and ith is not 0 then 0
		new_norm = 0
	elif adjusted_ith >= adjusted_target:
		# if target is non-zero and ith is >= target, then 1
		new_norm = 1
	else:
		# if target is non-zero and ith is < target then, ith/target
		new_norm = adjusted_ith/adjusted_target
	return new_norm

# NA will be treated as 0s
# if both are NA, should that be treated as similar? 
# Current choice is no.
# If both target and ith are NA, target will be 1 as expected
# and ith will be 0, since nothing can be known about similarity
def norm_strings(target_value, ith_value):
	new_norm = 0
	if target_value == ith_value:
		new_norm = 1
	elif not isinstance(target_value,str) and math.isnan(target_value):
		new_norm = 0
	elif not isinstance(ith_value,str) and math.isnan(ith_value):
		new_norm = 0
	else:
		split_target = target_value.lower().replace(',','').split()
		split_ith = ith_value.lower().replace(',','').split()
		intersect = set(split_target).intersection(split_ith)
		new_norm = len(intersect)/len(split_target)
	return new_norm

# Target boolean will be 1 and ith will be 1 if it matches
# 0 if not
def norm_boolean(target_value, ith_value):
	new_norm = 0
	if target_value==ith_value:
		new_norm = 1
	return new_norm

# Given target row and row_i return cosine similarity
def cos_sim(target_row, ith_row):
	# get renorm-ed ith row based on target row, so that
	# minimum is 0 and maximum is 1
	rtv = np.asarray(renorm_row(target_row, ith_row))
	# if we are confident about renorm_row then just
	# generate enough 1s
	riv = np.asarray(renorm_row(target_row, target_row))
	# calculate the cosine similarity
	num = sum(rtv*riv)
	denom = (math.sqrt(sum(rtv*rtv))*math.sqrt(sum(riv*riv)))
	cos_sim = num/float(denom)
	return cos_sim

# Given target row, calculate row_i for all other rows
# Return value should be a list where i place is
# the row index and value is 
def calculate_cos_sim(target_row, collection):
	cos_results = []
	for i in range(collection.rlen):
		ith_row = collection.df.iloc[i]
		cos_results += [cos_sim(target_row, ith_row)]
	return cos_results

# Given cos_results, return ordered list of sims
# ordered from highest to lowest
def ordered_results(cos_results):
	return cos_results[cos_results.argsort()[::-1]]


# Given cosine similarity results and value N
# return N entries of the most similar rows
# where the entry is the index of the row
def index_of_most_similar(cos_results, N):
	if N >= len(cos_results)-1:
		maxN = len(cos_results)
	else:
		maxN = N+1
	arr = np.array(cos_results)
	results = arr.argsort()[-maxN:][::-1]
	# We only return the N values shifted by one, because
	# first entry (most similar) will of course be our target row
	actual_results = arr.argsort()[-maxN:][::-1][1:]
	return actual_results


# Given cosine similarity results and value N
# return N entries of the most dissimilar rows
# where the entry is the index of the row
def index_of_least_similar(cos_results, N):
	arr = np.array(cos_results)
	return arr.argsort()[:N]


# Given list of indices, return corresponding
# names from df in order
def convert_ind_to_names(list, collection):
	res_names = []
	df = collection.df
	for index in list:
		res_names += [df['Name'][index]]
	return res_names


######################
# Deprecated functions
### not necessary, but just for thoughts
# Or modify dataframe to include for name as column value
# row value is the cos-sim value
def add_cos_sim_to_df(target_row, df):
	return None

# Re-normalize is a transformation of the df such that
# given a name, identify a target row. All values in that row will be 1
# For all othe rows value should fall between 0 and 1, 0 being unlike
# the target row, 1 being identical 
def renorm(df, name):
	target_row = get_target_row(df, name)
	if target_row == None:
		return None
	else:
		return None
	return None


