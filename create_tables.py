import pymysql

connection = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')
cursor = connection.cursor()

print "create soccer table"
sql = "CREATE TABLE IF NOT EXISTS soccer " \
      "(date DATE," \
      " league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " draw_odds FLOAT," \
      " away_odds FLOAT," \
      "PRIMARY KEY (date ,home_team, away_team));"
cursor.execute(sql)

print "create rugby table"
sql = "CREATE TABLE IF NOT EXISTS rugby " \
      "(date DATE," \
      " league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " draw_odds FLOAT," \
      " away_odds FLOAT," \
      "PRIMARY KEY (date ,home_team, away_team));"
cursor.execute(sql)

print "create australian football table"
sql = "CREATE TABLE IF NOT EXISTS australian_football " \
      "(date DATE," \
      " league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " away_odds FLOAT," \
      "PRIMARY KEY (date ,home_team, away_team));"
cursor.execute(sql)

print "create basketball table"
sql = "CREATE TABLE IF NOT EXISTS basketball " \
      "(date DATE," \
      " league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " away_odds FLOAT," \
      "PRIMARY KEY (date ,home_team, away_team));"
cursor.execute(sql)

print "create cricket table"
sql = "CREATE TABLE IF NOT EXISTS cricket " \
      "(date DATE," \
      " league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " away_odds FLOAT," \
      "PRIMARY KEY (date ,home_team, away_team));"
cursor.execute(sql)

print "create american football table"
sql = "CREATE TABLE IF NOT EXISTS american_football " \
      "(date DATE," \
      " league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " away_odds FLOAT," \
      "PRIMARY KEY (date ,home_team, away_team));"
cursor.execute(sql)

print "create hockey table"
sql = "CREATE TABLE IF NOT EXISTS hockey " \
      "(date DATE," \
      " league VARCHAR(50)," \
      " home_team VARCHAR(50)," \
      " away_team VARCHAR(50)," \
      " winner CHAR(1)," \
      " home_score INT," \
      " away_score INT," \
      " home_odds FLOAT," \
      " draw_odds FLOAT," \
      " away_odds FLOAT," \
      "PRIMARY KEY (date ,home_team, away_team));"
cursor.execute(sql)

print "create tennis table"
sql = "CREATE TABLE IF NOT EXISTS tennis " \
      "(date DATE," \
      " tournament VARCHAR(50)," \
      " player1 VARCHAR(50)," \
      " player2 VARCHAR(50)," \
      " winner CHAR(1)," \
      " score VARCHAR(50)," \
      " player1_odds FLOAT," \
      " player2_odds FLOAT," \
      "PRIMARY KEY (date ,player1, player2));"
cursor.execute(sql)
