teams = {}
done = False
#lista times
def print_teams():
    print('Times Listados')
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")
        
 #Lista jogadores de um time       
def print_team_players(team):
    print(f"Jogadores do {team['name']}:")
    for i , player in enumerate(team['players']):
        print(f'{i+1}. {player}')      

while not done:
    print('O que você deseja fazer?')
    print('1- Adicionar um time')
    print('2- Remover um time')
    print('3- Lista times')
    print('4- Adicionar jogador em um time')
    print('5- Remover jogador de um time')
    print('6- Lista de jogadores de um time')
    print('7- Sair')
    
    choice = input('>')
    if choice == '1':
       team_name = input('Digite o nome do time:\n')
       teams[team_name] = {'name': team_name, 'players': []}
       print('Time Adicionado')
    elif choice =='2':
        print_teams()
        team_num = int(input('Informe o número do time que seja remover:\n'))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print('Time Removido')
        else:
            print('Número inválido')    
    elif choice == '3':
       print_teams()
    elif choice == '4':
        print_teams()
        team_num = int(input("Informe o número do time que deseja adicionar jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            player_name = input("Informe o nome do jogador: ")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time.")
        else:
            print("Número do time inválido") 
    elif choice == '5':
        print_teams()
        team_num = int(input('Informe o número que deseja remover o jogador:'))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            print_team_players(teams[team_name])
            player_num = int(input('Informe o número do jogador que deseja remover:'))
            if player_num < len(teams[team_name] ['players']):
                del teams[team_name]['players'][player_num - 1]
                print('Jogador removido')
            else:
                print('Número do jogador inválido')
        else:
            print('Número inválido')            
    elif choice =='6':
       print_teams()
       team_num = int(input('Informe o número do time que deseja listar os jogadores\n'))      
       if team_num <= len(teams):
           team_name = list(teams.key())[team_num - 1]
           print_team_players(teams[team_name])
       else:
           print('Número inválido')   
    elif choice == '7':
        done = True
    else:
        print('Opção inválida')    