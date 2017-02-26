# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:14:09 2017

@author: lior
"""
import datetime
import xlrd
import pymysql.cursors

# Open the workbook and define the worksheet
book = xlrd.open_workbook("super_rugby.xls")
sheet = book.sheet_by_name("Data")

# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", db="project")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO rugby VALUES \
(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
"""


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(2, sheet.nrows):
    values = []
    for i in (47, 2, 3, 4, 5, 7,8,9):
        if (sheet.cell_type(r,i) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            values.append(None)
            continue
        if (i == 47):
            ms_date_number = sheet.cell(r, i).value # Correct option 2
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number, book.datemode)
            py_date = datetime.datetime(year, month, day, hour, minute, second)
            values.append(py_date)
            continue
        values.append(sheet.cell(r, i).value)
    if (sheet.cell(r, 4).value > sheet.cell(r, 5).value):
        values.insert(3, 'H')
    elif (sheet.cell(r, 4).value == sheet.cell(r, 5).value):
        values.insert(3, 'D')
    else:
        values.insert(3, 'A')
    values.insert(1, 'super_rugby')
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
