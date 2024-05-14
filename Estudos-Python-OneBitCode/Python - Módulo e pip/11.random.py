import random

#1 - Selecionar valor aleatório 
lista = [1,5,6,7,8,42,2,11]
print(random.choice(lista))

#2 - Gerar um número aleatório em um intervalo de valores
r1 = random.randint(5,15)
print(r1)

#3 - Selecionar caractere aleatório
name = 'Curso de Python feito por mim'
r2 = random.choice(name)
print(r2)

#4 - Selecionar mais de um valor aleatório
#sintaxe: random.sample(sequencia,tamanho)
print(random.sample(lista,2))
s = 'Hello world'
print(random.sample(s,2))