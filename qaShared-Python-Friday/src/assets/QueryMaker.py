# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:20:00 2016
@author: Ameen-Ul Haq
"""

import pymysql
import numpy as np
import re

class QueryMaker:
    '''
    The class is responsible for generating user stories in real time/ at run time.
    It determines the user story by taking a single paramter and then generates a user
    story by evaluating the parameter (string). It abstract elements and compares and
    analyses them by using a data matrix (datastructure - which stores all data from
    the MySQL database). Although in beta this feature class is able to draw join
    between tables by deducing relatable keys.
    '''

    def __init__(self, conn):
        '''
        Instantiating of this object executes the making of a query --> instance created
        Responsible for setting up key cursors - sporadically used and deals with SQL conenction

        @attention: The connection statement is an external parameter for concealing sensitive details
        '''
        #self.conn = pymysql.connect("", "", "", "nbgardensds")
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.cursor2 = self.conn.cursor()


    def main(self):
        '''
        Main method - control and run sub-methods. Acts as iniaiter for other procedures.

        @return: query: the generated user story
        '''
        self.matrixSetup()
        self.addTableNamesToMat()
        table_in_x, all_selects, query_type, input_where, input_and = self.processUserInput()
        all_table_aliases, all_table_names, all_aliases = self.findTable(table_in_x)
        select_statement, selects_list = self.addAliasToElements(all_selects, all_aliases)
        query = self.generateQuery(select_statement, selects_list, all_table_aliases, all_table_names, table_in_x, query_type, input_where, input_and)
        output = self.runTest(query)
        print (output)
        return query


    def matrixSetup(self):
        '''
        Creates matricies, to store all attributes and all the keys only in seperate matricies.
        These are then used as a local database and to evaluating the user inputs The latter
        matrix is used for common key discovery.

        @attention: This is generic and does not require pre-set values.
        '''
        # AUTO ====================
        number_of_tables, max_number_attributes = self.getDBDetails()

        # PREDEFINED ===============
        # number_of_tables = 20
        # max_number_attributes = 13

        # setting up dimensions of matrix (n, h x l) and set attribute char length
        self.matrix_all_attributes = np.array(np.arange(number_of_tables * max_number_attributes), dtype=(str, 35)).reshape(number_of_tables, max_number_attributes)
        self.matrix_keys= np.array(np.arange(number_of_tables * max_number_attributes), dtype=(str, 35)).reshape(number_of_tables, max_number_attributes)
        # all cells to empty
        self.matrix_keys[:]=  self.matrix_all_attributes[:] = ''


    def getTableData(self):
        '''
        Retrieves all data from the database and iterates through each one to process.

        @return: tables: eahc of the tables in the database
        '''
        sqlQuery = "show tables"
        self.cursor.execute(sqlQuery)
        # gets each table
        tables = self.cursor.fetchone()
        return tables


    def getAttributeList(self, table_name):
        '''
        Retrives all attributes for a given table

        @param table_name: name of table from db to retrieve atributes from
        @return: results of attributes as string
        '''
        results = self.cursor2.execute("describe " + table_name)
        return results


    def getDBDetails(self):
        '''
        Processes returned database data and reformats for storing in matrix. Also
        retrieves attributes list for each table and then stores in cooresponding row.
        Sorts all idenitifed key types in seperate matrix.

        @attention: This is a crucial part of the set up
        '''
        tables = self.getTableData()
        tbl_name_counter = 0
        number_of_attributes = []
        while tables is not None:
            print (tables)
            table_name = str(str(tables)[2:-3])
            attributes_found = self.getAttributeList(str(table_name))
            number_of_attributes.append(attributes_found)
            attribute_list = self.cursor2.fetchone()
            tables = self.cursor.fetchone()
            tbl_name_counter += 1
        return tbl_name_counter, (max(number_of_attributes))+1


    def addTableNamesToMat(self):
        '''
        Processes returned database data and reformats for storing in matrix. Also
        retrieves attributes list for each table and then stores in cooresponding row.
        Sorts all idenitifed key types in seperate matrix.

        @attention: This is a crucial part of the set up
        '''
        tables = self.getTableData()
        tbl_name_counter = 0
        while tables is not None:
            attribute_column = 0
            table = (str (tables))
            # extracts table name only
            unformatted_table_name = table[2:-3]
            table_name= (str(unformatted_table_name))
            # store table name as header row
            self.matrix_keys[tbl_name_counter, 0] =  self.matrix_all_attributes[tbl_name_counter, 0] =  table_name
            # get attributes
            results = self.getAttributeList(str(table_name))
            attribute_list = str(results)
            attnum = attribute_list[0:1]
            attribute_list = attribute_list[2:0]

            # until element in list do
            while attribute_list is not None:

                for line in attribute_list:
                    self.matrix_all_attributes[tbl_name_counter, attribute_column] = attribute_list[0]
                    # check the attribute list for any attributes for primary or foreign keys
                    if ((str(attribute_list[3]) =='PRI') or (str(attribute_list[3]) =='MUL')):
                        # store the key to is corresponding table and position found
                        self.matrix_keys[tbl_name_counter, attribute_column] = attribute_list[0]
                attribute_column +=1
                attribute_list = self.cursor2.fetchone()
            # END WHILE (INNER)
            tables = self.cursor.fetchone()
            tbl_name_counter += 1
        # END WHILE (OUTER)
        self.viewMatricies()


    def viewMatricies(self):
        '''
        Print all data stored in matricies - both

        @attention: Not needed in actual execution
        '''
        print('======= MATRIX ALL ATTRIBUTES ======== \n')
        print (self.matrix_all_attributes)
        print('\n\n======= MATRIX KEYS ONLY ======== \n')
        print (self.matrix_keys)


    def getUserInput(self, instruction):
        '''
        ** DEPRECATED METHOD **

        Attempt to get a valid input if its wrong then produces error message
        and then repeeats method

        @param instruction:the stringto print to the user
        @return: user_select is astring of valid attributes
        '''
        # get user input
        user_selects = input(instruction)
        for word in user_selects.split():
            # check if word exists
            if (np.where(self.matrix_all_attributes != word)):
                print ('Invalid input. Please try again!')
                self.getUserInput(instruction)
        return user_selects


    def processUserInput(self):
        '''
        Processes user input and extracts elements and discovers where the element is
        in the tables as attribute. Location is stored

        @return: coordinate_x is a list of each table that the element input is in and
        all_selects is the copied input string to add alias to later
        '''
        # get user input on attributes their interessted in
        #user_selects = self.getUserInput('Enter attribute you wish to query using space delimination for multiples ')
        user_input = input("Please enter what you'd like to search for? \n")

        coordinate_x = []
        all_selects = ''
        query_type = ''
        input_where = ''
        input_and = ''

        # created a exachnge key dictionary to replace basic term for opertors
        exchange_terms = { 'more than':'>', 'less than':'<', 'equal to':'='}

        # substitution code - replace the words taht correspond to dictionary
        pattern = re.compile(r'\b(' + '|'.join(exchange_terms.keys()) + r')\b')
        user_selects = pattern.sub(lambda x: exchange_terms[x.group()], user_input)
        # query_type = user_input.split(' ', 1)[0]
        # user_selects = user_input.split(' ', 1)[1]

        if 'where' in user_selects:
            input_where = user_selects.split('where', 1)[1]
            user_selects = user_selects.split('where', 1)[0]
            if 'and' in user_selects:
                input_where = input_where.split('and', 1)[0]
                input_and = input_where.split('and', 1)[1]

        # identify and break into elements
        for word in user_selects.split():
            print (word)
            all_selects += word + ' '
            # deduct the table its belongs
            if (np.where(self.matrix_all_attributes == word)):
                # store location
                temp_x, y = np.where(self.matrix_all_attributes == word)
                coordinate_x.append(temp_x)
                print(coordinate_x)
            else:
                print ('NOT FOUND')
        print('Processing input: ' + all_selects)
        return coordinate_x, all_selects, query_type, input_where, input_and


    def addAliasToElements(self, user_selects, all_aliases):
        '''
        this method is responsible for adding aliases to each of the attribute found
        in the user input

        @param user_selects: a copy of the user input as string
        @param all_aliases: each alias for each of the attributes
        @return: select_statement is a modified input string but with alias for
        each attribute added
        '''
        select_statement = ''
        selects_list = []
        i = 0
        for word in user_selects.split():
            print (word)
            select_statement +=  all_aliases[i] + '.' + word + ', '
            selects_list.append(all_aliases[i] + '.' + word)
            i += 1
        # take last comma off
        return select_statement[:-1], selects_list


    def findTable(self, table_in_x):
        '''
        similar to addAliasToElements adds the alias to the tables in
        SQL like format
        retrives the table name based on the x discover - from param
        stores the element aliases and table and tablles with aliases for
        generating the query

        @param table_in_x: x = reveals table name
        @return: all_table_aliases contain the table with attached alias in
        correct SQL syntax, all_tables_name is just a table with the tables
        found in location x and all_aliases is the table aliases only
        '''
        all_table_aliases = []
        all_table_names = []
        all_aliases = []
        # get table name
        for element in table_in_x:
            # validate the user input and see if it can be retrieved and stored
            try:
                element_table = (self.matrix_keys[element, 0])[0]
            # if it cannot be found and out of bounds -> ask user for another input
            except IndexError:
                print("Invalid Input - Cannot be Found! Try again...")
                self.main()
            alias = self.createTableAlias(element_table)
            table_with_alias =  element_table + ' as ' + alias
            all_aliases.append(alias)
            all_table_aliases.append(table_with_alias)
            all_table_names.append(element_table)
        return all_table_aliases, all_table_names, all_aliases


    def createTableAlias(self, element_table):
        '''
        creates a alias from the last and first character of the attributes
        table name.

        @attention: 'as' is an operator thus Address is converted to 'ads'
        not 'as'

        @param element_table: table name to be used as alias
        @return: alias is the generated alias formed fromt eh table name that
        the attribute belongs to
        '''
        alias = ''
        # get first and last char
        alias = (element_table[0] + element_table[-1]).lower()
        # current operator so change if reached
        if (alias == 'as'):
                alias = 'ads'
        return alias


    def generateQuery(self, select_statement, selects_list, all_table_aliases, all_table_names, table_in_x, query_type, input_where, input_and):
        '''
        The core part of this feature, its responsible of fidn a related key between
        the elemented specified as user input. After discoevry these they are added to
        the 'ON' statement of a table join query.
        All part of the query is added up here

        @attention: 'as' is an operator thus Address is converted to 'ads'
        not 'as'

        @param select_statement: a string of all attriubutes user inputted with aliases
        @param all_table_aliases: tables cooresponding to attributes chosen by user
        witrh aliases
        @param all_table_names: a list of tables found in location x based on user
        chosen attributes
        @param table_in_x: the location x of each interest table
        @return: query is the var containing the generated query formed by the various
        methods
        '''
        tables_sorted = []
        join = ''
        # create the select and from SQL statement by adding params
        select = 'SELECT ' + select_statement[:-1] + ' '
        from_part = 'FROM '+ all_table_aliases[0] + ' '
        # list to keep track of tables already added to the SQL query - avoid
        # duplicate joins of same table
        tables_sorted.append(all_table_aliases[0])
        # used to avoid the first index of matrix -> tbl name not attribute
        row_index_flag = 0
        found_1 = []
        found_2 = []
        # find a related key between each table
        for element in all_table_aliases:
            # skip the first one as that acts as start node
            if (row_index_flag > 0):
                # ensure its not a duplicate table - hasn't already been added
                if (element not in tables_sorted):
                    join = 'JOIN '+ element

                    # go through each attribute the table one (y) and then (x) and try to find a
                    # similar common key
                    for y in range (13):

                        for x in range (13):
                             # print ((self.matrix_keys[(table_in_x[0])[0], y]),(self.matrix_keys[(table_in_x[1])[0], x]) )
                            first_table_attribute = (self.matrix_keys[(table_in_x[0])[0], y])
                            next_table_attribute = (self.matrix_keys[(table_in_x[1])[0], x])
                            if ((first_table_attribute == next_table_attribute) and (next_table_attribute != '')):
                                found_1, found_2 = self.concatenateAliases(found_1, found_2, table_in_x, y, x)
                                break
                            # it may be a foreign key so extract everything beofre the underscore and
                                # then try to deduce. if found then break out of chain
                            if ('_' in first_table_attribute):
                                if ( ((first_table_attribute.split('_'))[1]) == next_table_attribute ):
                                    found_1, found_2 = self.concatenateAliases(found_1, found_2, table_in_x, y, x)
                                    break

                            if ('_' in next_table_attribute):
                                if ( first_table_attribute == (( next_table_attribute.split('_'))[1])  ):
                                    found_1, found_2 =self.concatenateAliases(found_1, found_2, table_in_x, y, x)
                                    break
                    # store each analyseed tables
                    tables_sorted.append(element)
            # if not related then go to next attribute in table
            row_index_flag += 1
        on = ''

        # begin adding each realted key as an ON string
        for k in range (len(found_1) ):

            on = ' ON ' + found_2[k] + ' = ' + found_1[k]

        query = select + from_part + join + on
        if input_where != '':
            query = select + from_part + join + on + ' WHERE ' + input_where
        if input_and != '':
            query = select + from_part + join + on + ' WHERE ' + input_where + ' AND ' + input_and
        query = query + ' GROUP BY ' + selects_list[0]
        return query


    def concatenateAliases(self, found_1, found_2, table_in_x, y, x):
        '''
        creates / adds aliases for the key of the tables and reformat in SQL format

        @attention: method developed to eliminate duplicate coding

        @param found_1: the related key from start table
        @param found_2: the related key from relateable table
        @param table_in_x: table name location
        @param y: location of the attribute
        @param x: location of the attribute
        '''
        alias_1 = self.createTableAlias(self.matrix_keys[(table_in_x[0])[0], 0])
        alias_2 = self.createTableAlias(self.matrix_keys[(table_in_x[1])[0], 0])
        # the table reamins the same its the x and y that changes --> column changes only
        # append to list to store
        found_1.append(alias_1 + '.' +  (self.matrix_keys[(table_in_x[0])[0], y]))
        found_2.append(alias_2 + '.' +  (self.matrix_keys[(table_in_x[1])[0], x]))
        return found_1, found_2


    def runTest(self, query):
        '''
        runs the SQL command that the class has generated. this is not sent back to
        the parent class

        @param query: the final generated query from above class
        @param output: the output of the execution is returned
        '''
        cursor= self.conn.cursor()
        cursor.execute(query)
        # retrives all data found
        output = cursor.fetchall()
        return output


'''
    ====== TO DO ========
- allow for multiple joins -> recursion...

    ====== PRESENTATION =======
- partials
- matrix COMPLETE
- numpy COMPLETE
- system itself COMPLETE
'''

#################################
# <conn>
# query_maker_obj = QueryMaker(conn)
# query_maker_obj.main()

