from collections import Counter, namedtuple,deque
from operator import itemgetter

#1 - Contar itens de uma lista
frutas = ["Maça", "Banana" , "Laranja" ,"Uva" , "Pêra" , "Abacaxi" ,"Uva", "Maça" ,"Uva" , "Tangerina" , "Pêra", "Banana"]
print(frutas)
print(Counter(frutas))

#2 - Tupla nomeada
game = namedtuple('game', ['name', 'price' , 'note'])
g1 = game("Fifa 24" , 90.5 , 5.0)
g2 = game("Resident Evil 4" , 120.00, 10)
print(g1)
print(g2)

#3 - Ordenando dicionário
estudantes = {'Pedro':23, 'Ana':22, 'Ronaldo':30, 'Julia':25}
a = sorted(estudantes.items(), key=itemgetter(0))
print(estudantes)
print(a)

#4 - Utilizando fila de ambas extremidades
deq = deque([20,40,60,80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)