# Conta letras
def check_char(text):
    type = {'Uppercase': 0 , 'Lowercase':0}
    for char in text:
        if char.isupper():
            type['Uppercase'] += 1
        elif char.islower():
            type['Lowercase'] += 1
    print('Texto original:', text) 
    print('Número de maiúsculas?:', type['Uppercase'])
    print('Número de letras minúsculas:', type['Lowercase'])
           
check_char('A Melhor Forma De Prever o Futuro é Criá-lo')



# Verificar par e impar
def check_numbers(numbers):
    par = []
    impar = []
    for number in  numbers:
        if number % 2 == 0:
            par.append(number)
        else:
            impar.append(number)
    return par , impar        
print(check_numbers([1,2,3,4,5,6,7,8,9,10]))

