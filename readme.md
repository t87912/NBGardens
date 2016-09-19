## Jobs for people:

# 1. writeToCSV() Function:

This function will accept data in the form [[row 1],[row 2]...[row n]] where a row is a list of elements, e.g. row1 = [1.0, 2015, 5, "Some string"] e.t.c.

The writeToCSV.py file can be found in the same place as MainTUI/MainGUI e.t.c

My old code from my original program is in there, this could probably be extended.

This function should accept data with any number of rows and columns and write it to a csv file.

# 2. Finish off Mongo Queries that use SQL (ANDREW):

This involves finishing the Mongo Queries that need data from the MySQL database.

# 3. Get Logging sorted:

In MainTUI() there is commented out code related to logging. Basically it creates a logger object and whenever a user attempts to login, their username and password is logged.

In addition to this, whenever a custom SQL OR custom Mongo query is exececuted (or tries and fails to execute), it should be logged in this file.

If a user logs out this should also be logged.

The code is mostly done, the logger can be created and written to, however I had some issues when passing the logger object to MySQLDatabase.py and MongoDatabase.py. To get this working these classes need to be instantiated with the logger object called in.

# 4. Comments and DocStrings in AllUserStories.py and methodFinder() in MySQLDatabase (AMEEN):

Just go back through the code and comment any parts that are complicated and write the docstrings explaining what the methods do.

# 5. Put the Class Diagram on Github (DAMIEN):

Either email the class diagram to me or put it on Github.

# 6. Search MongoDB by review keyword (ANDREW?):

It would be nice to allow the user to search the MongoDB based upon a keyword.

So if the user search for "Good", all reviews with the keyword "Good" would be returned.

# 7. Ensure all User Stories ask for the right inputs and return the right data (DATABASE TEAMS):

This job is for both database teams. Basically just run the program and go through the user stories, making sure each user story returns the correct data, ordered correctly etc.

# 8. Find a way of getting column names for query results (DATABASE TEAM):

Currently, when queries are executed, only the data is returned, so the user has to guess what the column names are.

The Database team needs to find a way of executing a query that returns the column names.

So if a query returns the following: [[1], ['Gnome'], ['A normal Gnome'], [68.64], [80.12], [44]]

It would be: 

[Product ID, Name, Description, Price, Etc, Etc]
[[1], ['Gnome'], ['A normal Gnome'], [68.64], [80.12], [44]]

I am not sure whether this would be a seperate query or if there is an option to return column names in MySQL.

If a seperate query is nescessary, the Database team needs to write those queries and then the python team will append the column names to the first element of the returned data.


# Old ToDO stuff:

3. Make sure graphs are correct, right axes and data etc
5. Get documentation sorted - see below
6. Useful doc strings on every method/class/erd
7. Useful comments where needed
8. Put class diagram on github
9. Once SQL user logins added, have one login system in the TUI

**Documentation Information**
Tried to get the documentation working using Sphinx. Managed to get a HTML file but couldn't get any data from the Python files.



