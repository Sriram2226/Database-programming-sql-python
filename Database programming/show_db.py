import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

'''Output :  

('demo',)
('information_schema',)
('mydatabase',)
('mysql',)
('performance_schema',)
('pharmacy',)
('sem',)
('studentdb',)
('sys',)

'''