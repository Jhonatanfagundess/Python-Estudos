from conexao_post import conn

cursor_obj = conn.cursor(
)

sql = """
    UPDATE game
    SET name = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ('Fifa 24', 5))
conn.commit(
)
conn.close()