    def print_records(self, row, cursor):
        for i in range(len(cursor.description)):
            print (cursor.description[i][0], " ", end="")
        print('\n')
        while row is not None:
            print (row)
            row = cursor.fetchone()   
        cursor.close()
        self.db.close()
