#Contagem foguete
import winsound
x = 10
while x >= 0 :
    print(x)
    x -= 1 
    winsound.Beep(2500, 500)
    

#Tabuada
number = int(input('Tabuada de :'))
begin = int(input('De: '))
end = int(input('Até:'))
x = begin
while x <= end :
    print(f'{number} x {x} = {number * x}')
    x += 1


