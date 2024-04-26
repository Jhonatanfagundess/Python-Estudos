gameName = 'Resident Evil 4'
gameDescription = """
fifa 23 é um jogo para ser jogado online,
ou offline para que assim todos os jogadores, façam o 
uso do jogo
"""

print(gameName.upper()) #Maiúsculo
print(gameName.lower()) # Minúsculo
print(gameName.capitalize()) #Apenas primeira letra maiúscula
print(gameName.title()) #Apenas primeira letra maiúscula
print(gameName.center(10, '-')) #Retorna a string centralizada
print(gameName.find("f"))
print(gameDescription.count('a')) #Conta quantos caracteres 
print(gameDescription.count('A')) #Conta quantos caracteres 
print(gameDescription.replace("fifa", "Pes")) #Altera elementos
print(gameDescription.split(','))