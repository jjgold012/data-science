import pymysql

connection = pymysql.connect(host="localhost", user="root", charset='utf8')
cursor = connection.cursor()
sql = 'DROP DATABASE project'
cursor.execute(sql)

