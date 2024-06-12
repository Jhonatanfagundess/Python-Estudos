class Movie:
    platform = 'Jhow.filmes'
    def __init__(self, name , yearLauch, plan , duraction ):
        self.name = name
        self.yearLauch = yearLauch
        self.plan = plan
        self.notas = 0
        self.duraction = duraction
        self.avaliadores = 0 
        
    def __str__(self):
        return f'Filme: {self.name}'
        
    def ficha_tecnica(self):
        print(f'Plataforma: {Movie.platform}')
        print(f'Nome do filme: {self.name}')
        print(f'Ano de lançamento: {self.yearLauch}')   
        print(f'Está no plano : {self.plan}')
        print(f'Duração: {self.duraction}')
        print(f'Total de avaliadores: {self.avaliadores}')
        
    def av(self , note):
        self.notas += note
        self.avaliadores += 1
        
    def average(self):
        print(f'Média do Filme: {self.name} : {self.notas / self.avaliadores}')    
                    
        
        
        
avengers = Movie('Vingadores' , 2012 , False , 120)     
avengers.av(9.5)
avengers.av(10.0)
avengers.ficha_tecnica()
avengers.average()
#Modificando a plataforma
annabelle = Movie('Anabelle', 2015, True , 125)
Movie.platform = 'OnebitCodePRO'
annabelle.av(9.5)
annabelle.av(10.0)
annabelle.ficha_tecnica()
annabelle.average()
