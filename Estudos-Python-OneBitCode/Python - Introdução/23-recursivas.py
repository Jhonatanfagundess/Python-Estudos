#Fatorial de um número 
# 3  - 3 * 2 *1 
#


#1 - Fatorial de um número
def factorial(num):
    if num == 1 :
        return 1
    else:
        return(num * factorial(num-1))
    
number = int(input('Digite um número para fatorial'))
print(f'Fatorial de {number} é {factorial(number)}')

# 2 - somar um total de um número    

def total_sum(num):
    if num == 1:
        return 1
    else:
        return(num + total_sum(num - 1))


num = int(input('Digite um número para a soma:'))
print(f'A soma total de {num} é : {total_sum(num)}')    