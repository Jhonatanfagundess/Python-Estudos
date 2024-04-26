gamesList = ['Resident Evil 4' , 'Elden Ring' , 'Red Dead 2 ' , 'Mario World']


#1- Tamanho da lista
print(len(gamesList))

#2 - Recuperar o item da lista pelo indice
print(gamesList.index('Mario World'))

#3 - Adicionar um jogo mna lista
gamesList.append("GTA V")
print(gamesList)

#4 - Ordenar lista 
gamesList.sort()
print(gamesList)

#5 - copiar Lista
gameReset = gamesList.copy()
gameReset.remove('Red Dead 2 ')
print(gameReset)

#6 - Remove todos os itens na lista
gamesList.clear
print(gamesList)