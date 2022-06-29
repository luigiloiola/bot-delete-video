import mysql.connector
from os import listdir
from datetime import datetime

print(len('os cria, so bandido mal'))

db = mysql.connector.connect(user='luigi', password='qpzm7797',
                              host='localhost',
                              auth_plugin='mysql_native_password',database='testdatabase')
mycursor = db.cursor()
# mycursor.execute("INSERT INTO membros VALUES('547905866255433758', 'bot musica');")

string = ''
for i in str(datetime.now()):
    string += i
print(string)
dia = string[8:10]
print(dia)



# db.commit()



#mycursor.execute("INSERT INTO test (nome, hora) VALUES (%s,%s)", ("bruno", datetime.now()))
#mycursor.execute('')
#db.commit()

