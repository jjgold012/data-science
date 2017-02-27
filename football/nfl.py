# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:14:09 2017

@author: lior & ori
"""
import datetime
import xlrd
import pymysql.cursors
import re

# Open the workbook and define the worksheet
book = xlrd.open_workbook("nfl.xls")
sheet = book.sheet_by_name("Data")

# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

# Create the INSERT INTO sql query
query = """INSERT IGNORE INTO american_football VALUES \
(%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    values = []
    print r
    for i in (0, 1,2, 3,4, 8,12):
        if (sheet.cell_type(r,i) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            values.append(None)
            continue
        if (i == 0):
            ms_date_number = sheet.cell(r, i).value # Correct option 2
            
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,
            book.datemode)
            py_date = datetime.datetime(year, month, day, hour, minute, second)

            values.append(py_date)
            continue
        values.append(sheet.cell(r, i).value)
    if (sheet.cell(r, 3).value > sheet.cell(r, 4).value):
        values.insert(3, 'H')
    elif (sheet.cell(r, 3).value == sheet.cell(r, 4).value):
        values.insert(3, 'D')
    else:
        values.insert(3, 'A')
    values.insert(1, 'NFL')
    cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print("")
print("All Done! Bye, for now.")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported", columns, " columns and", rows, "rows to MySQL!")
