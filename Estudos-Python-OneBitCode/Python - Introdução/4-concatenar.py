#Utilizando o Input e pra fazer comentário é #
name = input('Digite o nome do seu jogo Favorito?\n')
yearLauch = int(input('Qual o ano de lançamento?\n'))
gamePrice = float(input('Qual o preço do jogo?\n'))
planIncluid = bool(input('Está incluído no plano mensal?\n'))


print("###Dados do Jogo###")
print("---------------------")
#Alternativa 1
# print("Nome do Jogo:", name)
# print('Ano do jogo:', yearLauch)
# print('Preço do jogo', gamePrice)
# print('Incluido no plano',planIncluid)

#alternativa 2

# print('Nome do jogo:' , name, 'Ano do lançamento'  , yearLauch , 
#       '\n Preço do jogo:', gamePrice , 'Está incluso no plano?', planIncluid)

#Alternativa 3

print(f"Nome do jogo: {name} \n Ano de lançamento {yearLauch} \nPreço do jogo: {gamePrice} \nEstá incluso no plano? {planIncluid}")

