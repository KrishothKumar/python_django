import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

select = 'select * from travel_destination'
print(*cursor.execute(select),sep = "\n")
#
att= "ATTACH db.db AS my_db;"
cursor.execute(att)
delete = 'delete from travel_destination'
# cursor.execute(delete)

sel="SELECT * FROM SYSOBJECTS WHERE xtype = 'U';GO"
# show = "show tables from db.sqlite3"
print(cursor.execute(sel))

connection.commit()
connection.close()
