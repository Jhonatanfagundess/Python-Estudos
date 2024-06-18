class Animal:
    def __init__(self,name,categoria) :
        self.name = name
        self.categoria = categoria
        
    
    
    
class Fish(Animal):
        race = ''
        
class Parrots(Animal):
        color = ''     
        
        
class Zoo():
    def __init__(self):
        self.animals_dict = {}
        
    def add_animal(self,animal):
        self.animals_dict[animal.name] = animal.categoria
        
    def total_of_categoria(self,categoria):
        result = 0 
        for animal in self.animals_dict.values():
            if animal == categoria:
                result += 1 
        return f'No nosso zoológico temos {result} e quantidade de {categoria}' 
    
    
zoo = Zoo()
peixe = Fish('Nemo', 'Mamífero')     
peixe2 = Fish('Dory', 'Mamífero')
papagaio = Parrots('Louro', 'Aves')
papagaio2 = Parrots('Gavião' , 'Aves')
zoo.add_animal(papagaio)
zoo.add_animal(papagaio2)
zoo.add_animal(peixe)
zoo.add_animal(peixe2)
print(zoo.total_of_categoria('Aves'))
print(zoo.total_of_categoria('Mamífero'))      
                     
        