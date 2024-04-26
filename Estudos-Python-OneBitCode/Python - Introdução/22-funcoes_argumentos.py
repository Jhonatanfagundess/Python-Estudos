#1 - Crie uma função que recebe dois argumentos
def full_name(fname, Lname):
    print(f'Nome Completo: {fname} {Lname}') 
    

full_name('Jhonatan', 'Fagundes')

#2 - uma função que soma dois números
def soma(a,b):
    return a + b

print(soma(10,50))
  
  
# 3 - argumentos default 
def address(country = 'Brasil'):
    print(f'Eu moro no {country}')
    
address()     

#4 - avaliação de jogo
def ranking(qtd):
    name = input('Digite o nome do jogo:\n')
    sum = 0
    for i in range(qtd):
        nota = float(input('Digite a nota do jogo:\n'))
        sum += nota
    print(f'Média de avaliação do jogo {name} é: {sum / qtd}')    
    
ranking(2)  
rank = int(input('Digite quantas avaliações vai fazer do jogo:\n'))
ranking(rank)  

#Teste para calcular média
#x = int(input('Quantas matéria vai calcular hoje?'))
def notas_media(x):
    soma = 0
    for i in range(x):
        nota = int(input('Qual foi sua nota na matéria?'))
        soma += nota
    print(f'Somando as matérias sua nota final foi : {soma / x}')
    
    
x = int(input('Quantas matéria vai calcular hoje?')) 
notas_media(x)        