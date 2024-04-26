gameList = ['Fifa' , 'God of War', 'Red dead 2' , 'Pes 2019']
#1 - Iterando valores de uma letra
for game in gameList:
    print(game)
    
    
# 2 - Quando a condição é atentida o loop acaba
for game in gameList:
    if game == 'Red dead 2':
         break   
    print(game)
    
# 3 - Quando a condição for atentida o loop vai para a proxima iteração
for game in gameList:
    if game == 'Red dead 2':
        continue
    print(game)    
    
# 4 - Avaliação do jogo
for i in range(5):
    print('Hello World')    
    
gameName = input('Digite o Nome do jogo: \n')
gameRaking = int(input('Quantas avaliações deseja fazer no jogo?\n'))        
sum = 0
for i in range(gameRaking):
    note = float(input('Digite a nota para o jogo: \n'))
    sum += note
print(f'A média de avaliação do jogo é {gameName} é {sum/gameRaking :.2f}')    