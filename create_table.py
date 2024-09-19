import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

# Criar tabela PibBrasil
conn.execute('''
CREATE TABLE IF NOT EXISTS PibBrasil (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    periodo TEXT UNIQUE NOT NULL,
    valor REAL NOT NULL
);
''')


print("Tables created successfully")
conn.close()
