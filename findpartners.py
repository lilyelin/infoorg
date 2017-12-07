from helper import *
import math
import numpy


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




# given a name and a df, identify the row in the df that the name 
# corresponds with. Otherwise return None.
def get_target_row(df, name):
	target_row = df[df['Name']==name]
	if len(target_row) < 1:
		return None
	else:
		#return target_row.index.item()
		return target_row



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
		if isinstance(target_j, str):
			# norm string
			norm_strings(target_j, ith_j)
		if isinstance(target_j, numpy.bool_):
			# norm bool
			norm_boolean(target_j, ith_j)
		if isinstance(target_j, numpy.int64):
			# norm integer
			norm_result += norm_years_of_experience(target_j, ith_j)
		else:
			#something is wrong with the values here
			# do something
			norm_result += 0
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

	return new_norm

# NA will be treated as 0s
# if both are NA, should that be treated as similar? 
# Current choice is no.
# If both target and ith are NA, target will be 1 as expected
# and ith will be 0, since nothing can be known about similarity
def norm_strings(target_value, ith_value):
	new_norm = 0

	
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
	renorm_ith = renorm_row(target_row, ith_row)
	# if we are confident about renorm_row then just
	# generate enough 1s
	renorm_target = renorm_row(target_row, target_row)
	# calculate the cosine similarity
	# get numerator
	sum_of_dot_product(renorm_target, renorm_ith)
	# get denominator
	denom_of_cos_sim(renorm_target, renorm_ith)
	return None

def sum_of_dot_product(target_row, ith_row):
	return None

def sum_of_sqrs(row):
	return None

def denom_of_cos_sim(target_row, ith_row):
	target_sqrt = math.sqrt(sum_of_sqrt(target_row))
	ith_sqrt = math.sqrt(sum_of_sqrt(ith_row))
	mult_sqrts = target_sqrt*ith_sqrt
	return mult_sqrts


# Given target row, calculate row_i for all other rows
# Return value should be a list where i place is
# the row index and value is 
def calculate_cos_sim(target_row, df):
	cos_results = []
	for i in range(df.rlen):
		ith_row = df.iloc[i]
		cos_results += cos_sim(target_row, ith_row)
	return cos_results




# Given cosine similarity results and value N
# return N entries of the most similar rows
# where the entry is the index of the row
def index_of_most_similar(cos_results, N):
	return None


# Given cosine similarity results and value N
# return N entries of the most dissimilar rows
# where the entry is the index of the row
def index_of_least_similar(cos_results, N):
	return None


# Given list of indices, return corresponding
# names from df in order
def convert_ind_to_names(list):
	return None


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
		return None:
	else:

	return None


