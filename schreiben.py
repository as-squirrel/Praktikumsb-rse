import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('noten.db')

# cursor object
cursor_obj = connection_obj.cursor()


connection_obj.execute(
	"""INSERT INTO DATA (Lehrer,Fach,Score) VALUES ("Micha","Mathe",9)""")


connection_obj.commit()

# Close the connection
connection_obj.close()
