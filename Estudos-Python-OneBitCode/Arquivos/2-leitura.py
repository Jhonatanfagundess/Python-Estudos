 
# r - leitura
# w - escrita
# a - append

with open('name.txt' ,'r',encoding='utf-8') as file:
    for line in file:
        print(f'Olá, {line.rstrip()}')