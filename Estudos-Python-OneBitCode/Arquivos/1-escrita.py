name = input('Digite seu nome:\n')
 
# r - leitura
# w - escrita
# a - append
 
 
#1  
# file = open('name.txt','a')
# file.write(f'{name}\n')
# file.close()

#2 
with open('names.txt', 'a') as file:
    file.write(f'{name}\n')