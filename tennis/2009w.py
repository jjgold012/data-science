# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:14:09 2017

@author: lior & ori
"""
import dateutil.parser
import datetime
import xlrd
import pymysql.cursors

# Open the workbook and define the worksheet
book = xlrd.open_workbook("2009w.xls")
sheet = book.sheet_by_name("2009")

# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

# Create the INSERT INTO sql query
query = """INSERT IGNORE INTO tennis_women VALUES \
(%s, %s, %s, %s, %s, %s, %s, %s)
"""


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    values = []
    ms_date_number = sheet.cell(r, 3).value  # Correct option 2
    year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,
                                                                  book.datemode)
    py_date = datetime.datetime(year, month, day, hour, minute, second)
    values.append(py_date)
    for i in (2,9, 10,21,22,24,25):
        if (sheet.cell_type(r,i) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            values.append(None)
            continue
        values.append(sheet.cell(r, i).value)
    values.insert(4,1)
    values.insert(5, str(int(values[5] if values[5] is not None else 0)) + "-" + str(int(values[6] if values[6] is not None else 0)))
    values.pop(6)
    values.pop(6)

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
print("I just imported ", rows, " rows to MySQL!")
