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

# Criar tabela Investimento
conn.execute('''
CREATE TABLE IF NOT EXISTS Investimento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    periodo TEXT,
    valor REAL,
    subcategoria INTEGER,
    FOREIGN KEY (periodo) REFERENCES PibBrasil(periodo),
    FOREIGN KEY (subcategoria) REFERENCES Categoria(id)
);
''')

# Criar tabela Usuario
conn.execute('''
CREATE TABLE IF NOT EXISTS Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    token TEXT NOT NULL
);
''')


print("Tables created successfully")
conn.close()
