import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

params_list = [(1, "Antonio", "Tancredi"), (2, "Massimo", "Galliani")]

cursor.execute("drop table if exists persone")
cursor.execute("create table persone(id int, nome varchar(30), cognome varchar(30), primary key(id))")

cursor.executemany("insert into persone (id, nome, cognome) values(?,?,?)", params_list)

# forma allungata dell'executemany
#for params in params_list:
	#cursor.execute("insert into persone (id, nome, cognome) values(?,?,?)", params)

# utilizzo alternativo
cursor.execute("insert into persone (id, nome, cognome) values(:id, :name, :surname)",
	{"id":3, "name":"Aldo", "surname":"Biscardi"})

connection.commit()

## FETCH DEI DATI ##	

cursor.execute("select nome,cognome from persone")

for row in cursor:
	nome,cognome = row
	print("Nome = " + nome)
	print("Cognome = " + cognome + "\n")

print("\n--------------\n")

# metodo piu' pulito per il fetch dei dati
cursor.execute("select * from persone")
cursor.row_factory = sqlite3.Row
rows = cursor.fetchall()
for row in rows:
	for key in row.keys():
		print("%s = %s" % (key, row[key]))
	print("\n"),

connection.rollback() #annulla i cambiamenti

cursor.close()
connection.close()
