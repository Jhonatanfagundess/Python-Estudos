#1 - Função de potência
power = lambda num: num**2

#2 - número par 
pair = lambda x : x % 2 == 0

#3 - divide número por outro
divNum = lambda x,y : x / y 

#4 - função que inverte a string
reverse = lambda s: s[::-1]


print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10 ,2))
print(divNum(6,2))
print(reverse('Python'))
print(reverse('Ruby'))