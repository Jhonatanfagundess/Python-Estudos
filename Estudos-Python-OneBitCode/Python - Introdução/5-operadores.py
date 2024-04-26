num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))

#Aritméticos
som = num1 + num2
sub = num1 - num2 
div = num1 / num2 
mult = num1 * num2
mod = num1 % num2 # resto da divisão
exp = num1 ** num2 # potenciação
print(som)
print(sub)
print(div)
print(mult)

# Comparação

bigger = num1 > num2 
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_eqaul = num1 <= num2

print(f'Os números {num1} e {num2} são iguais? {equal}')
print(bigger_equal)

#Atribuição

num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1
