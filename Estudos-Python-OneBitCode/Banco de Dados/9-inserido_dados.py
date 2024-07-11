from conexao_post import conn

cursos_obj = conn.cursor()

games = [
    ('Resident Evil 4' , 2023 , 9.0),
    ('The Last Of Us' , 2013 , 10)
]

for game in games:
    cursos_obj.execute("""
       INSERT into game(name , year , score)
       VALUES (%s , %s , %s)                                        
                       """, game)
conn.commit()
print('Dados Atualziados')
conn.close()