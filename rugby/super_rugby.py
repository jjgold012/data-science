# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:14:09 2017

@author: lior
"""
import datetime
import xlrd
import pymysql.cursors

# Open the workbook and define the worksheet
book = xlrd.open_workbook("super_rugby.xlsx")
sheet = book.sheet_by_name("Data")

# Establish a MySQL connection
database = pymysql.connect(host="localhost", user="root", db="project")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO super_rugby (\
date , kick_off , home_team , away_team , home_score , away_score\
, playoff_game , home_odds , draw_odds , away_odds, bookmakers_surveyed\
, home_odds_open , home_odds_min , home_odds_max, home_odds_close , away_odds_open\
, away_odds_min , away_odds_max , away_odds_close , home_line_open , home_line_min \
, home_line_max , home_line_close , away_line_open , away_line_min , away_line_max \
, away_line_close , home_line_odds_open , home_line_odds_min ,home_line_odds_max, \
home_line_odds_close , away_line_odds_open,away_line_odds_min ,away_line_odds_max , \
away_line_odds_close , total_score_open , total_score_min , total_score_max , \
total_score_close , total_score_over_open , total_score_over_min , total_score_over_max\
, total_score_over_close , total_score_under_open , total_score_under_min ,\
total_score_under_max , total_score_under_close , notes ) VALUES \
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(2, sheet.nrows):
    values = []
    print(r)
    for i in range(48):
        print (sheet.cell_type(r,i))
        if (sheet.cell_type(r,i) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
            values.append(None)
            continue
        if sheet.cell(r, i).ctype == 3: # 3 means 'xldate' , 1 means 'text'
            ms_date_number = sheet.cell(r, i).value # Correct option 2
            if (i == 0):
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,
                book.datemode)
                py_date = datetime.datetime(year, month, day, hour, minute, second)
                values.append(py_date)
                continue
            if (i == 1):
                x = sheet.cell(r, i).value # a float
                x = int(x * 24 * 3600) # convert to number of seconds
                my_time = datetime.time(x//3600, (x%3600)//60, x%60) # hours, minutes, seconds
                values.append(my_time)
                continue
        values.append(sheet.cell(r, i).value)
    	
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
