gamesSet = {
    'Fifa 23' , 'red dead 2 ' , 'Star wars' , 'Mario World' , 'Resdient evil 4'
}

#1 - Tamanho do set
print(len(gamesSet))

#2 -True e 1 são o mesmo valor 
exampleSet = {'Fifa 23' , True , 1 , 90.50}
print(exampleSet)

#3 - Adicionar Item de outro set
gamesSet.update(exampleSet)
print (gamesSet)

#4 - remover itens
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)