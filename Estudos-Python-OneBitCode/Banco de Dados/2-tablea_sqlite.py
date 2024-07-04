import sqlite3
#1 Criando BD
connection = sqlite3.connect('title.db')

#2 Criando um Cursor

cursor = connection.cursor()

#3 Criando TABELA
cursor.execute("""
    CREATE TABLE movies(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,  
            score REAL NOT NULL
        );       
               """)


# 4 Fechando conexão
print('Tabela Feita')
connection.close()