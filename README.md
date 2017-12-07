# infoorg
Final Project Info Org Demo

## Controller of MVC for Talent Acquisition Exploration Platform

Our goal was to organize MIMS students to allow for greater ease in acquiring the right talent!
Whether you be a school administrator, recruiter, or fellow student looking for the right skills or the right matches between people.

## Useful commands
> select_intersect(collection, Java, Python, C, CPP, R, D3, SQL)

Where the collection is the Object containing the collection of student representations. The other values are booleans, True to select for this skill, False to ignore.

> same_career_goals(collection, name)

Name is the person who our target is and output will be all students who have listed the same career goals.

> find_tfidf_sim(collection, name, N, options=None)

Name is our target, N is number of outputs, option can be set to 'verbose'.
This will return the N most similar students to our target. When options set to 'verbose', this will also return the corresponding cosine similarities calculated. This uses the term frequency–inverse document frequency method of calculating similarity between target and entry.

> find_tfidf_dis(collection, name, N, options=None)

Same as above, but instead the N most dis-similar students.

> find_sim_partners(collection, name, N, options=None)

Again, name is our target, N is number of outputs, option can be set to 'verbose', with the same results as above.
However this time, we are not using the tf-idf method and instead do a direct cosine similarity calculation with all columns except for context columns (0-5). All columns have a maximum value of 1 normalized against the target row. Specific interpretations for each column and choices in normalization can be found in commented code.

> find_dis_partners(collection, name, N, options=None)

Same as above, but instead the N most dis-similar students.



## Future Implementation

* Build Flask UI for web deployment
* Add D3 visualization for social graph and metric distributions
* Auto-convert pdf files to csv row entry
* Allow independent users to update their row entry
* Track changes over time for users for their career journey, give suggestions
* Allow users to give feedback on usefulness of suggested collaborators, contrast weighing schemes
* Auto-generate groups given size of group and amount of difference between members

## Other To Dos

- Apply tfidf to raw of pdf document
- Add ability to apply non-one weights to findpartners feature sets
- Convert select_intersect to use JSON string as input

## Extra

Test