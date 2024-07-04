import sqlite3
#1 Criando BD
connection = sqlite3.connect('title.db')

#2 Criando um Cursor

cursor = connection.cursor()

#3 Inserindo dados
cursor.execute("""
        INSERT INTO MOVIES(name,year,score)
        VALUES('Dragon Ball Evolution',2005,2)               
               """)

cursor.execute("""
        INSERT INTO MOVIES(name,year,score)
        VALUES('Dead Note',2017,4)              
               """)

cursor.execute("""
        INSERT INTO MOVIES(name,year,score)
        VALUES('Divertidamente 2',2024,10)               
               """)

#4 Gravando dados no BD
connection.commit()
print('Dados inseridos')

#5 Fechando conexão
connection.close()