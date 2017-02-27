# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:14:09 2017

@author: lior & ori
"""
import dateutil.parser
import xlrd
import pymysql.cursors
import calendar
import warnings


months = dict((v,k) for k,v in enumerate(calendar.month_abbr))

# Open the workbook and define the worksheet
book = xlrd.open_workbook("basketball1.xls")
sheet = book.sheet_by_name("oOo NBA 3in1  EUodds")

# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

# Create the INSERT INTO sql query
query = """INSERT IGNORE INTO basketball VALUES \
(%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

rows = 0

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(4, sheet.nrows):
    values = []
    year = int(sheet.cell(r, 0).value)
    month= months[sheet.cell(r, 2).value]
    day  = int(sheet.cell(r, 1).value)
    py_date = dateutil.parser.parse(str(day) + '-' + str(month) + '-' + str(year)).date()
    values.append(py_date)
    for i in (7,8, 17,15,16,25,26):
        if (sheet.cell_type(r,i) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            values.append(None)
            continue
        values.append(sheet.cell(r, i).value)
    values.insert(1, sheet.cell(r, 5).value)
    cursor.execute(query, values)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rows += cursor.execute(query, values)


# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results

print("I just imported " + str(rows) + " rows to MySQL!")
