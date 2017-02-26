import pymysql

connection = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')
cursor = connection.cursor()

print "drop soccer table"
sql = "DROP TABLE IF EXISTS soccer;"
cursor.execute(sql)

print "drop rugby table"
sql = "DROP TABLE IF EXISTS rugby;"
cursor.execute(sql)

print "drop australian_football table"
sql = "DROP TABLE IF EXISTS australian_football;"
cursor.execute(sql)

print "drop basketball table"
sql = "DROP TABLE IF EXISTS basketball;"
cursor.execute(sql)

print "drop cricket table"
sql = "DROP TABLE IF EXISTS cricket;"
cursor.execute(sql)

print "drop american_football table"
sql = "DROP TABLE IF EXISTS american_football;"
cursor.execute(sql)

print "drop hockey table"
sql = "DROP TABLE IF EXISTS hockey;"
cursor.execute(sql)

print "drop tennis_men table"
sql = "DROP TABLE IF EXISTS tennis_men;"
cursor.execute(sql)

print "drop tennis_women table"
sql = "DROP TABLE IF EXISTS tennis_women;"
cursor.execute(sql)

