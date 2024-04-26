# 1 - liste valores de 0 a 10 que sejam menor do que 4

for i in range(10):
    if i < 4:
        print(i)
        

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)        


gameList = ['Mario World' , 'Resident evil' , 'Mario Kart' , 'Resident evil 2']

# 2 - jogos que possuam a letra a 
newList = [x for x in gameList if 'a' in x]
print(newList)


# 3 - jogos que eu zerei
gameFinished = [x for x in gameList if x != 'Mario Kart']
print(gameFinished)
