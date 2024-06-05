
class Movie:
    def __init__(self, name , yearLauch, plan , note, duraction ):
        self.name = name
        self.yearLauch = yearLauch
        self.plan = plan
        self.note = note
        self.duraction = duraction
        
    def __str__(self):
         return f'filme : {self.name} || Ano de Lançamento: {self.yearLauch}'  
        
        
movie = Movie('Rush:No Limite da Emoção', 2013 , False , 10.0 , 92 )
movie2 = Movie('Avengers:End Game', 2019 , False , 10.0 , 220)
print(movie)        
print(movie.name)
print(movie2.name)
print(movie2)