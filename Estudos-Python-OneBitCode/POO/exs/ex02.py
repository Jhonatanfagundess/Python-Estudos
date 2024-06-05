#Produtos
class Produto:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
        
    def __str__(self):
        return f'Nome do produto: {self.name} - R$ {self.price}'  
    
    
    def ficha_do_produto(self):
        print(f'Nome do produto: {self.name}')
        print(f'Preço do produto: {self.price}')
        
    def des(self,percentual):    
        desconto = (self.price/100) * percentual
        final = self.price - desconto
        return int(final)
        
                
        
pc = Produto('PC Gamer' , 4000)
cel = Produto('Iphone 15', 15000)
print(cel)
print(cel.des(20))
print(pc)
print(pc.des(20))