import pymysql

connection = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')
cursor = connection.cursor()

print "create soccer table"
sql = "CREATE TABLE IF NOT EXISTS soccer " \
      "(date DATE, league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " draw_odds FLOAT," \
      " away_odds FLOAT);"
cursor.execute(sql)