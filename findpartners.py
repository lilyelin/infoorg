import helper

# Modes 2 and 3
# create normalized values for all entries based on target person
# then determine closest and furthest based on cosine similarity
#
# Equation for cosine similarity will be
# sum of dotproduct of target vector and vector i
# divided by multiple of sqrt of sum of vector components of target vector 
# squared and sqrt of sum of vector components of vector i squared




# Re-normalize is a transformation of the df such that
# given a name, identify a target row. All values in that row will be 1
# For all othe rows value should fall between 0 and 1, 0 being unlike
# the target row, 1 being identical
def renorm(df, name):
	return None

# given a name and a df, identify the row in the df that the name 
# corresponds with. Otherwise return None.
