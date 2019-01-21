import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
# cursor.execute("CREATE TABLE usuarios(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
# cursor.execute("INSERT INTO usuarios VALUES ('matia bd',27,'elgato@gmail.com')")
cursor.execute("SELECT *FROM usuarios")
# print(cursor)
usuario = cursor.fetchone()
print(len(usuario))

print(usuario[2])
# usuario = [( "juan",45,"hikla"),
#     ("rand",34,"jkjdkjd")
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuario)

# print(usuario)
conn.commit()
conn.close()