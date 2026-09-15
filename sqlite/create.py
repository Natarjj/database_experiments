import sqlite3

conn = sqlite3.connect('database.db')
cursor = connectio.cursor()

cursor.execute("""
INSERT INTO user (u_name, u_email, u_password)
VALUES ('Maria', maria@email.com', 'Senha123')
 """)

 conn.commit()

 conn.close()