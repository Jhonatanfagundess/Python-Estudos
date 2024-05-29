class Movie:
    name = ''
    yearLauch = ''
    IncluidPlan = False
    note = 0
    duration = 0 
    
    
# Primeiro Filme
movie = Movie()
movie.name = 'Oppenheimer'
movie.yearLauch = '2023'
movie.IncluidPlan = False
movie.note = 5.0
movie.duration = 180
print("##Dados do Filme")
print(f'Nome do Filme: {movie.name}\n Ano de Lançamento : {movie.yearLauch}')

#Segundo Filme
movie2 = Movie()
movie2.name = 'O Panda do Kung Fu 4'
movie2.yearLauch = '2024'
movie2.IncluidPlan = True
movie2.note = 2.0
movie2.duration = 94
print('##Dados do Filme##')
print(f'Nome do Filme: {movie2.name}\n Ano de Lançamento: {movie2.yearLauch}')