import pprint
gamesDict = {
    'Resident evil 4' :{
        'yearlauch ':2023 , 
        'classification' : 9.6 , 
        'genre': ['Ação ' , 'Aventura']
        },
    'mario World' : {
        'yearlauch' : 2017,
        'classification': 10.0 ,
        'genre' : ['Aventura' , 'Livre']
    },
        'donkey kong coutry': {
            'yearlauch' : 1995,
            'classification' : 9.5,
            'genre' : ['aventura' , 'plataforma']
        }
        
        
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

#1 = buscar informações aninhadas
print(gamesDict['mario World']['genre'])

#2 - Adicionar itens
gamesDict['mario World'] ['players'] = 1
print(gamesDict['mario World'])

#3 - Excluir uma informação
del gamesDict['Resident evil4']
pp.pprint(gamesDict)

