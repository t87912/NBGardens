# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:20:00 2016
@author: Administrator
"""

import pymysql
import numpy as np

class QueryMaker:


    def __init__(self):
        self.conn = pymysql.connect("213.171.200.88", "AlStock", "0N$Project", "nbgardensds")
        self.cursor = self.conn.cursor()
        self.cursor2 = self.conn.cursor()


    def main(self):
        self.matrixSetup()
        self.addTableNamesToMat()
        table_in_x, all_selects = self.addAttributesToMat()
        all_table_aliases, all_table_names, all_aliases = self.findTable(table_in_x, self.matrix_keys)
        select_statement = self.addAliasToElements(all_selects, all_aliases)
#        print (select_statement)
        self.generateQuery(select_statement, all_table_aliases, all_table_names, table_in_x)


    def matrixSetup(self):
        number_of_tables = 20
        max_number_attributes = 13

        self.matrix_all_attributes = np.array(np.arange(number_of_tables * max_number_attributes), dtype=(str, 35)).reshape(number_of_tables, max_number_attributes)
        self.matrix_keys= np.array(np.arange(number_of_tables * max_number_attributes), dtype=(str, 35)).reshape(number_of_tables, max_number_attributes)
        self.matrix_keys[:]=  self.matrix_all_attributes[:] = ''


    def getTableData(self):
        #show columns -
        sqlQuery = "show tables"
        #choose date
        self.cursor.execute(sqlQuery)
        tables = self.cursor.fetchone()
        return tables


    def addTableNamesToMat(self):
        tables = self.getTableData()
        tbl_name_counter = 0
        while tables is not None:
            attribute_column = 0
            table = (str (tables))
            unformatted_table_name = table[2:-3]
            table_name= (str(unformatted_table_name))
            self.matrix_keys[tbl_name_counter, 0] =  self.matrix_all_attributes[tbl_name_counter, 0] =  table_name
        #        print (t)
            results = self.cursor2.execute("describe "+str(table_name))

            attribute_list = str(results)
            attnum = attribute_list[0:1]
            attribute_list = attribute_list[2:0]

            # until element in list do
            while attribute_list is not None:
        #            print(type(attribute_list))
        #            print (str(attribute_list))
                for line in attribute_list:

                    self.matrix_all_attributes[tbl_name_counter, attribute_column] = attribute_list[0]
        #                print(attribute_list[3])
                    # check the attribute list for any attributes for primary or foreign keys
                    if ((str(attribute_list[3]) =='PRI') or (str(attribute_list[3]) =='MUL')):
        #                    print('key found at: ' + str(attribute_list))
                        self.matrix_keys[tbl_name_counter, attribute_column] = attribute_list[0]
                attribute_column +=1
                attribute_list = self.cursor2.fetchone()

        #        print ("\n\n")
            # END WHILE (INNER)
            tables = self.cursor.fetchone()
            tbl_name_counter += 1
        # END WHILE (OUTER)

        print('======= MATRIX ALL ATTRIBUTES ======== \n')
        print (self.matrix_all_attributes)
        print('\n\n======= MATRIX KEYS ONLY ======== \n')
        print (self.matrix_keys)


    def addAttributesToMat(self):
        user_selects = input('Enter attribute you wish to query using space delimination for multiples ')
        coordinate_x = []
        all_selects = ''
        for word in user_selects.split():
            print (word)
            all_selects += word + ' '
            if (np.where(self.matrix_all_attributes == word)):
        #        print (arr_index)

                temp_x, y = np.where(self.matrix_all_attributes == word)
                coordinate_x.append(temp_x)
                print(coordinate_x)
            else:
                print ('NOT FOUND')
        print('user typesd' + all_selects)
        return coordinate_x, all_selects


    def addAliasToElements(self, user_selects, all_aliases):
        select_statement = ''
        i = 0
        for word in user_selects.split():
            print (word)
            select_statement +=  all_aliases[i] + '.' + word + ', '
            i += 1
        return select_statement[:-1]


    def findTable(self, table_in_x, matrix_keys):
        all_table_aliases = []
        all_table_names = []
        all_aliases = []
        for element in table_in_x:
            element_table = (self.matrix_keys[element, 0])[0]
#            print (element_table[0])
            alias = self.createTableAlias(element_table)
            table_with_alias =  element_table + ' as ' + alias
#            print ('table_tag' + str(table_with_alias))
            all_aliases.append(alias)
            all_table_aliases.append(table_with_alias)
            all_table_names.append(element_table)
#        print (all_table_aliases)
#        print (all_table_names)
        return all_table_aliases, all_table_names, all_aliases
        
        
    def createTableAlias(self, element_table):
        alias = ''
        alias = (element_table[0] + element_table[-1]).lower()
        if (alias == 'as'):
                alias = 'ads'
#        print(alias)
        return alias
        

    def generateQuery(self, select_statement, all_table_aliases, all_table_names, table_in_x):
        tables_sorted = []
        join = ''
        select = 'SELECT ' + select_statement[:-1] + ' '
        from_part = 'FROM '+ all_table_aliases[0] + ' '
        tables_sorted.append(all_table_aliases[0])
        i = 0
        found_1 = []
        found_2 = []
        for element in all_table_aliases:
            if (i > 0):
                if (element not in tables_sorted):
                    join = 'JOIN '+ element
                    j = 1
                    print('x 1 is the followiung ===')
                    print (table_in_x[1] )
                    found = ''
                    for y in range (13):
                        for x in range (13):
                            print ((self.matrix_keys[(table_in_x[0])[0], y]),(self.matrix_keys[(table_in_x[1])[0], x]) )
##                            print(((self.matrix_keys[(table_in_x[1])[0], x]).split('_'))[1])
                            if (((self.matrix_keys[(table_in_x[0])[0], y]) == (self.matrix_keys[(table_in_x[1])[0], x])) and ((self.matrix_keys[(table_in_x[1])[0], x]) != '')):
                                print('fhjdhfdhj')                                
                                print(self.matrix_keys[(table_in_x[0])[0], 0])
                                found_1.append(alias_1 + '.' +  (self.matrix_keys[(table_in_x[0])[0], y]))
                                found_2.append(alias_2 + '.' +  (self.matrix_keys[(table_in_x[1])[0], x]))
#                                print(found_1)
#                                print(found_2)
#                                print('found')
                                break
#                            print ((self.matrix_keys[(table_in_x[0])[0], y]),(self.matrix_keys[(table_in_x[1])[0], x]) )
#
                            if ('_' in (self.matrix_keys[(table_in_x[0])[0], y])):
                                
#                                print ('hellloooooo')
                                if ((((self.matrix_keys[(table_in_x[0])[0], y]).split('_'))[1]) == (self.matrix_keys[(table_in_x[1])[0], x])):
                                    print('fhjdhfdhj')                                
                                    alias_1 = self.createTableAlias(self.matrix_keys[(table_in_x[0])[0], 0])
                                    alias_2 = self.createTableAlias(self.matrix_keys[(table_in_x[1])[0], 0])
                                    found_1.append(alias_1 + '.' +  (self.matrix_keys[(table_in_x[0])[0], y]))
                                    found_2.append(alias_2 + '.' +  (self.matrix_keys[(table_in_x[1])[0], x]))
#                                    print('hhigfdsjghjjfdghjdfh')
                                    print(found_1)
                                    print('45546565665')
                                    print(found_2)
                                    break
#                        print ('FOUND')
#                        print(found)

                    tables_sorted.append(element)
            i += 1
        print(found_1)
        print('45546565665')
        print(found_2)
        on = ''
        for k in range (len(found_1) ):
            
            on = ' ON ' + found_2[k] + ' = ' + found_1[k]
#        On c.idCustomer = f.Customer_idCustomer
        print(all_table_aliases)
        print(select_statement)
        query = select + from_part + join + on
        print(query)
        self.runTest(query)
#        for table in all_table_aliases:
#            
#        query = "SELECT " + select_statement + "FROM " + all_table_names
#        print (query)
#        self.runTest(query)        


    def runTest(self, query):
        cursor= self.conn.cursor()
        cursor.execute(query)
        tables = cursor.fetchall()
        print (tables)
        




'''
    ====== TO DO ========
- in findTable() add an extract where based on teh table name you add the first and last character as the alias than store that alias as string
and use it as the alias for that table... do this for each
- if you have multiples then
- check the two values and see if they are in different tables
- if they are see if they share a common key
- create a key share path
Select c.idCustomer as ‘Customer ID’, c.FirstName as ‘First Name’, c.LastName as ‘Surname’, f.DatePublished as ‘Date Published’ , round(f.rating,2) as ‘Average Product Rating’
From Customer as c
Join Feedback as f
On c.idCustomer = f.Customer_idCustomer
WHERE f.Products_idProducts = ‘” + product_number + “’
AND f.DatePublished BETWEEN ‘” + start_date + “’ AND ‘” + end_date+ “’
GROUP BY f.DatePublished;”
'''








#################################
query_maker_obj = QueryMaker()
query_maker_obj.main()
