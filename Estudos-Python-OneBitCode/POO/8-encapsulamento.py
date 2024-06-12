class Employee:
    def __init__(self, name, salario):
        self.name = name
        self.__salario = salario
        
        def show(self):
            print(f'Nome: {self.name} Seu salário {self.__salario}')
            
         
fulano = Employee('Fulano', 4000)
sicrano = Employee('Sicrano' , 5000)
fulano.show()
sicrano.show()

           
        