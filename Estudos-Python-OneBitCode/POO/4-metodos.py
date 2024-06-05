class Movie:
    def __init__(self, name , yearLauch, plan , note, duraction ):
        self.name = name
        self.yearLauch = yearLauch
        self.plan = plan
        self.note = note
        self.duraction = duraction
        
    def __str__(self):
         return f'filme : {self.name} || Ano de Lançamento: {self.yearLauch}'  
     
     
    def tech_sheet(self): 
        print("##Dados do Filme")
        print(f'Nome do Filme: {self.name}\n')
        print(f'Ano de Lançamento : {self.yearLauch}\n')
        print(f'Está no plano? {self.plan}\n')
        print(f'Nota: {self.note}\n')
        print(f'Duração: {self.duraction}\n')
        
        
        
avengers = Movie('Vingadores' , 2012 , False , 9.0 , 120)     
annabelle = Movie('Anabelle', 2015, True , 4.0 , 125)
avengers.tech_sheet()
annabelle.tech_sheet()     
