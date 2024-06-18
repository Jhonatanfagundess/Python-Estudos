from ex03 import Trip

trip0 = Trip('Alemanha')
trip1 = Trip('Portugal')
trip2 = Trip('Canadá')
trip3 = Trip('Fraça')
trip4 = Trip('Inglaterra')

print('Ofertas de viagens:')
name = input('Digite seu nome:\n')
print(f'{name} temos esse destinos que Combinam com você')
print(' 0-Alemanha \n 1-Portugal\n 2-Canadá\n 3-Fraça\n 4-Inglaterra')
choice = int(input('Qual escolhe?'))
lista = [trip0, trip1 , trip2 , trip3 , trip4]

for option in lista:
    if choice >= 5:
        print('Inválida')
        break
    else:
        print(f'{name} sua viagem para {lista[choice].destiny} está marcada! ')
        break