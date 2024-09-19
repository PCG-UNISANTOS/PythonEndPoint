import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS PibBrasil (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    periodo TEXT UNIQUE NOT NULL,
    valor REAL NOT NULL
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS Categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    periodo TEXT,
    FOREIGN KEY (periodo) REFERENCES PibBrasil(periodo)
);
''')


print("Tables created successfully")
conn.close()
