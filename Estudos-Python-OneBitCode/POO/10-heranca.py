class Animal:
     name = ''
     size = ''
     color = ''
     
     def eat (self):
         print('Animal Alimentado')
         
        
class Horse (Animal):
    race = ''
    
    def escape(self):
        print('Cavalo Fugindo')   
        
        
class Lion(Animal):
    mane = True
    
    def hunt(self):
        print('Leão Caçando')         
        
    
    
    
h = Horse()
h.name = 'Castanho'
h.color = 'Preto'
h.escape()
h.eat()                
l = Lion()
l.name = 'Simba'
l.color = 'Marrom'
l.hunt()
l.eat()
