"""
1 - O método estático não possui o parâmetro self.
2 - O método de classe pode acessar mas não pode modificar o estado da classe 
3 - Usamos o decorator @staticmethod em python para criar um método estático
""" 

class linguagem:
    def __init__(self,name, trail):
        self.name = name
        self.trail = trail
    
    
    @staticmethod    
    def cursos(trail):    
        if trail == 'Python Fundamentos':
            trilha = ['Dominando Python' , 'Módulos e Pip' , 'POO']
        elif trail == 'Automação com Python':
            trilha = ['Automação de tarefas' , 'Web Scraping' , 'IA']
        else :
            trilha = ['A definir']        
        return trilha    
            
print(linguagem.cursos('Python Fundamentos'))        
print(linguagem.cursos('Automação com Python'))           
print(linguagem.cursos('Análise de dados'))               
            