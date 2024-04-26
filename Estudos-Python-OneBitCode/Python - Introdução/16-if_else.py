name = input('Digite o nome do jogp\n')
yaerLauch = int(input('Digite o ano do lançamento do jogo\n'))
classification = float(input('Digite a nota de Classificação do jogo\n'))

if classification > 8.0 or yaerLauch > 2015 : #and seria se as duas condições fossem true
    print(f' O jogo {name} é bom! Jogue.')
else :
    print(F'O jogo {name} não tem uma boa nota')