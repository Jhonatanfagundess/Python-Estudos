gameFifa = {
    'name': 'Fifa 23',
    'YearLauch' : 2022,
    'gamePrice': 90.50,
    'Classification':8.5,
    'genre': ['esporte','familia']
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

#1 - Recuperar valores
print(gameFifa['genre'])
print(gameFifa['Classification'])

#2 - Buscar as chaves do dicionários
print(gameFifa.keys())

#3 - Buscar por valores
print(gameFifa.values())

#4 - buscar com chave e valores
print(gameFifa.items())

#5 - Adicionar items
gameFifa['player'] = 2
print(gameFifa)

#6 - atualziar itens no dicionário
gameFifa.update({'player':1})
print(gameFifa)
