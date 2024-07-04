import sqlite3
#1 Criando BD
connection = sqlite3.connect('title.db')

#2 Criando um Cursor

cursor = connection.cursor()

# 3 Solicitando dados do US por input
name = input('Qual o nome do filme?\n')
year = int(input('Qual ano de lançamento?\n'))
score = float(input('Qual a nota?\n'))

# 4 Inseridos dados
cursor.execute("""
        INSERT INTO movies(name,year,score)
        VALUES(?,?,?) 
               """,(name,year,score))

#5 Gravando dados no BD
connection.commit()
print('Dados inseridos')

# 6Fechando conexão
connection.close()