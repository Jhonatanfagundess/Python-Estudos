class Phone:
    def __init__(self, brande, model_name,price):
        self._brande = brande
        self._model_name = model_name
        self._price = price
        
        
    def __str__(self):
        return f'{self._brande} {self._model_name}'
    
    
    @staticmethod
    def make_a_call(phone_num):
        print(F'Ligando para: {phone_num}')
        
    def discount(self):
        return self._price * 0.10
        
        
class SmartPhone(Phone):
    def __init__(self, brande, model_name, price, ram , memory , back_camera):
        super().__init__(brande, model_name, price)      
        self.ram = ram
        self.memory = memory
        self.back_camera = back_camera
        
    def discount(self):
        return self._price * 0.15  
        



Moto = Phone('Moto', 'G7' , 2000)
print(Moto)
Moto.make_a_call(25568867)
print(f'Valor do {Moto._brande} {Moto._model_name} é {Moto._price}')
print(vars(Moto))
print(Moto.discount())
        
        
Iphone = SmartPhone('Iphone','13',7000,'4GB','128GB','25MP')
print(Iphone)
Iphone.make_a_call(11995134979)
print(f'O valor do {Iphone._brande}{Iphone._model_name} é {Iphone._price} com {Iphone.ram} de memória ram e espaço de {Iphone.memory} e com qualidade de câmera {Iphone.back_camera} ')   
print(Iphone.discount())  