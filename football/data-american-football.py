# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:14:09 2017

@author: lior & ori
"""
import datetime
import pymysql.cursors
import csv
import warnings

from os import listdir
from os.path import isfile, join
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
rows = 0

dir = "data-american_football"
files = [dir+"/"+f for f in listdir(dir) if (isfile(join(dir, f)) and f.endswith('csv'))]

for f in files:

    file = open(f, 'rb')
    reader = csv.reader(file)
    headers = [h.strip() for h in reader.next()]
    # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
    for row in reader:
        values = []
        for i in (headers.index("Date"),headers.index("Home Team"), headers.index("Visitor"),headers.index("Home Score"), headers.index("Visitor Score"), headers.index("Line")):
            if not row[i].strip():
                values.append(None)
                continue
            values.append(row[i])

        date = values[0].split('/')
        values[0] = date[2]+'-'+date[0]+'-'+date[1]
        values.insert(1, 'American Football')
        values.insert(4, 'H' if values[4]>values[5] else 'A')
        values.append(float(values[len(values)-1]) if values[len(values)-1] is not None else None)
        values[len(values)-2] = -float(values[len(values)-2]) if values[len(values)-2] is not None else None
        if (values[5] is None or values[6] is None):
            continue
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

