import sqlite3
#1 - Criando banco de dados
conexao = sqlite3.connect('title.db')

#2 - Verificar se houve alteraçaões na base de dados
print(conexao.total_changes)