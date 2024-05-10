import re

text = 'Eu quero ser programador e nada vai me parar!'
# 1 - Indíce inicial e final de palavras
# O r = uma string bruta(row string)

match = re.search(r'ser programador',text)
print('índice inicial', match.start())
print('índice final', match.end() )

#2 - Buscando o indice que possui ponto
site = 'https://onebitcode.com'
match = re.search(r'\.',site)
print(match)

#3 - Buscando uma lista de caracteres dentro de uma frase
padrao = '[a-m]'
result = re.findall(padrao,text)
print(text)
print(result)

#4 - Verificar o ínicio de uma string
rule = r'^A'
ph = ['A casa está suja' ,'Quero sair', 'Vamos dar um role']
for f in ph:
    if re.match(rule,f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde:{f}')    
        
#5 - Final de uma string
rule_end = r'!$'
ph2 = 'O dia tá lindooo!'
match = re.search(rule_end,ph2)
if match:
    print('Sim, tá no jeito')
else:
    print('Não, fora da rima')           