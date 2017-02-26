# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:14:09 2017

@author: lior & ori
"""
import datetime
import xlrd
import pymysql.cursors

# Open the workbook and define the worksheet
book = xlrd.open_workbook("E0.xlsx")
sheet = book.sheet_by_name("E0")

# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

# Create the INSERT INTO sql query
query = """INSERT INTO soccer VALUES \
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(2, sheet.nrows):
    values = []
    print(r)

    for i in (1, 2, 3, 6, 4,5):
        if (sheet.cell_type(r,i) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            values.append(None)
            continue
        if sheet.cell(r, i).ctype == 3: # 3 means 'xldate' , 1 means 'text'
            if (i == 1):
                ms_date_number = sheet.cell(r, i).value # Correct option 2
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,
                book.datemode)
                py_date = datetime.datetime(year, month, day, hour, minute, second)
                values.append(py_date)
                continue
        values.append(sheet.cell(r, i).value)
    for i in range(23, 44):
        values.append(sheet.cell(r, i).value)
    values.insert(1, sheet.cell(r, 0).value)
    print values
    cursor.execute(query, values[:10])
    cursor.execute(query, values[:7]+values[10:13])
    cursor.execute(query, values[:7]+values[13:16])
    cursor.execute(query, values[:7]+values[16:19])
    cursor.execute(query, values[:7]+values[19:22])
    cursor.execute(query, values[:7]+values[22:25])
    cursor.execute(query, values[:7]+values[25:28])

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
