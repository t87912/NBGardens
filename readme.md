## Jobs for people:

# 1. Finish off Mongo Queries that use SQL (ANDREW):

This involves finishing the Mongo Queries that need data from the MySQL database.

# 2. Get Logging sorted (TOM C):

In MainTUI() there is commented out code related to logging. Basically it creates a logger object and whenever a user attempts to login, their username and password is logged.

In addition to this, whenever a custom SQL OR custom Mongo query is exececuted (or tries and fails to execute), it should be logged in this file.

If a user logs out this should also be logged.

The code is mostly done, the logger can be created and written to, however I had some issues when passing the logger object to MySQLDatabase.py and MongoDatabase.py. To get this working these classes need to be instantiated with the logger object called in.

# 3. Comments and DocStrings (EVERYBODY):

Just go back through the code and comment any parts that are complicated and write the docstrings explaining what the methods do.

# 4. Search MongoDB by review keyword (ANDREW?):

It would be nice to allow the user to search the MongoDB based upon a keyword.

So if the user search for "Good", all reviews with the keyword "Good" would be returned.

# 5. Make sure graph data/axes/labels are correct (TOM C)

# 6. Login to Mongo and SQL, not just SQL (TOM C)

# 7. Add toCSV method to each Mongo story and Mongo Stories in AllUserStories.py (TOM C)

# 8. In AllUserStories, need to add headers to results (AMEEN)

# 9. Add Scroll Bar to GUI results box (TOM)

# 10. Add new user stories without coding, eg generate new code for user stories?

## DevOps Jobs:

# 1. CloudFoundry:

Need to set up CloudFoundry to deploy our project.

# 2. Jenkins:

Not sure if this is possible, but it would be nice to have Jenkins run the project to see if there are any errors?

