import csv
import pymysql.cursors
import os
import warnings




# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

# Create the INSERT INTO sql query
query = """INSERT IGNORE INTO soccer VALUES \
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
rows = 0

abbrDict = {'HT':'HomeTeam', 'AT':'AwayTeam'}
dir = "soccer - countries"
for filename in os.listdir(dir):
    if not filename.endswith('.csv'):
        continue
    f = open(dir+"/"+filename, 'r')
    reader = csv.reader(f)
    headers = [h.strip() for h in reader.next()]
    if 'HT' in headers:
        headers[headers.index('HT')] = abbrDict['HT']
        headers[headers.index('AT')] = abbrDict['AT']
    for row in reader:
        values = []
        if not row[1] or not row[2] or not row[3]:
            continue
        for i in (headers.index("Date"),headers.index("Div"),headers.index("HomeTeam"),headers.index("AwayTeam"),
                  headers.index("FTR"), headers.index("FTHG"), headers.index("FTAG"), headers.index("B365H"),
                  headers.index("B365D"), headers.index("B365A")):
            if (row[i] is None or not row[i]):
                values.append(None)
                continue
            if i in (headers.index("B365H"), headers.index("B365D"), headers.index("B365A")):
                values.append(float(row[i]))
                continue
            if i in (headers.index("FTHG"), headers.index("FTAG")):
                values.append(int(row[i]))
                continue
            if i == headers.index("Date"):
                parts = str(row[i]).split('/')
                py_date = parts[2] + '-' + parts[1] + '-' + parts[0]
                values.append(py_date)
                continue
            values.append(row[i])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            rows += cursor.execute(query, values)
    f.close()

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print("I just imported " + str(rows) + " rows to MySQL!")






