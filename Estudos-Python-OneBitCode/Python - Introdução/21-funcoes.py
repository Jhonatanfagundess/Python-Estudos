def wellcome():
    print('Hello world')
    
      
wellcome()

# 2 - para somar dois números

def sum():
    return 5 + 4

print(sum())

# 3 - cadastrar nome de um jogo
def create_game():
    name = input('Qual o nome do jogo?\n')
    yearLauch = int(input('Qual o ano de lançamento?\n'))
    gamePrice = float(input('Qual o valor do jogo?\n'))
    note = float(input('Qual a nota do jogo?\n'))
    
    print(f'{name} - R$ {gamePrice} - Ano de lançamento: {yearLauch} e sua nota: {note}')
    
create_game()    



