import re


text = 'Me chamo Jhonatan Fagundes e quero ser um programador! Minha base na escola foi pessíma e por conta disso estou correndo atrás de tudo que eu perdi! Começei a estudar em 2023 sendo mais exatamento no mês 12(dezembro) e estarei pronta para uma vada no fim de 2024!'
pq = '[a-z]'
gg = '[A-Z]'
number = '[0-9]'
resultadop  = re.findall(pq,text)
resultadog = re.findall(gg,text)
resultadonumber = re.findall(number,text)
print(f'Letras pequenas: {resultadop}\n Letras grandes: {resultadog}\n Números:{resultadonumber}')


def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("ABCDEFabcdef123450")) 
print(check_character("*&%@#!}{"))