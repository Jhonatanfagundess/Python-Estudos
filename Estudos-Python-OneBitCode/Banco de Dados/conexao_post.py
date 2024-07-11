import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    usuario = 'postgres',
    passoword = '123456',
    host = 'localhost',
    port = '5432'
)
