import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
# cursor.execute('''
#         CREATE TABLE usuarios(
#             dni VARCHAR(9) PRIMARY KEY,
#             nombre VARCHAR(100),
#             edad INTEGER,
#             email VARCHAR(100)
#         )

# ''')
# cursor.execute("SELECT *FROM usuarios")

# usuario = cursor.fetchone()
# print(usuario[1])

# usuarios = [
#     ('1124','radior',24,'yo@gmail.com'),
#     ('2345','mario',32, 'mari@alv.com')
# ]
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

# cursor.execute('''
#     CREATE TABLE products(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )

# ''')
# productos = [
#     ('teclado','longitech',19.95),
#     ('pantalla','lg', 83.04)
# ]
# cursor.executemany("INSERT INTO products VALUES (null,?,?,?)", productos)
# cursor.execute("SELECT *FROM usuarios WHERE edad = 24")
# cursor.execute("UPDATE usuarios SET nombre='Hugo' WHERE dni='1124'")
usuario = cursor.fetchall()
for i in usuario:
    print(i)

conn.commit()
conn.close()