# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:20:00 2016

@author: Ameen
"""

import pymysql
import numpy as np

class QueryMaker:
    
    def __init__(self):
        conn = pymysql.connect("213.171.200.88", "AlStock", "0N$Project", "nbgardensds")
        self.cursor = conn.cursor()
        self.cursor2 = conn.cursor()
    
    def main(self):
        # ============ SETUP MATRIX
        number_of_tables = 20
        max_number_attributes = 13
        
        matrix_all_atts = np.array(np.arange(number_of_tables * max_number_attributes), dtype=(str, 35)).reshape(number_of_tables, max_number_attributes)
        matrix_keys= np.array(np.arange(number_of_tables * max_number_attributes), dtype=(str, 35)).reshape(number_of_tables, max_number_attributes)
        matrix_keys [:]=  matrix_all_atts[:] = ''
        # ===================== END 
        
        
        #show columns - 
        sqlQuery = "show tables"
        #choose date
        
        self.cursor.execute(sqlQuery)
        tables = self.cursor.fetchone()
        tbl_name_counter = 0
        
        
        while tables is not None:
            attribute_column = 0
            table = (str (tables))
            unformatted_table_name = table[2:-3]
            table_name= (str(unformatted_table_name))
            matrix_keys[tbl_name_counter, 0] =  matrix_all_atts[tbl_name_counter, 0] =  table_name
        #        print (t)
            att1 = self.cursor2.execute("describe "+str(table_name))
            
            att = str(att1)
            attnum = att[0:1]
            att = att[2:0]
            
            # until element in list do
            while att is not None:
        #            print(type(att))
        #            print (str(att))
                for line in att:
                    
                    matrix_all_atts[tbl_name_counter, attribute_column] = att[0]
        #                print(att[3])
                    # check the attribute list for any attributes for primary or foreign keys
                    if ((str(att[3]) =='PRI') or (str(att[3]) =='MUL')):
        #                    print('key found at: ' + str(att))
                        matrix_keys[tbl_name_counter, attribute_column] = att[0]
                attribute_column +=1
                att = self.cursor2.fetchone()
                
        #        print ("\n\n")
            # END WHILE (INNER)
            tables = self.cursor.fetchone()
            tbl_name_counter += 1
        # END WHILE (OUTER)
        
        print('======= MATRIX ALL ATTRIBUTES ======== \n')
        print (matrix_all_atts)
        print('\n\n======= MATRIX KEYS ONLY ======== \n')
        print (matrix_keys)
        
        
        user_selects = input('Enter attribute you wish to query using space delimination for multiples ')
        x = []
        all_selects = ''
        for word in user_selects.split():
            print (word)
            all_selects += word + ' ' 
            if (np.where(matrix_all_atts == word)):
        #        print (arr_index)
            
                temp_x, y = np.where(matrix_all_atts == word)
                x.append(temp_x)
                print(x)
            else:
                print ('NOT FOUND')
        concat_selects = self.findTable(x, matrix_keys)
        print (concat_selects)
        self.generateQuery(all_selects, concat_selects)

  
    def findTable(self, x, matrix_keys):
        concat_selects = ''
        for element in x:
            element_table = matrix_keys[element, 0]
#            print (element_table[0])
            concat_selects +=  element_table[0] + ' '
#            all_table_names.append(element_table[0]) 
        return (concat_selects)

    
    def generateQuery(self, all_selects, all_table_names):
        select_command = "SELECT " + all_selects + "FROM" + all_table_names
        print (select_command)


#################################
maker_obj = QueryMaker()
maker_obj.main()
