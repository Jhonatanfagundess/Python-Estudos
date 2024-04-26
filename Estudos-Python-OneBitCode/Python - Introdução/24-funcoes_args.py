# 1 - soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f'A soma é {sum_total}')    
        
               
sum(7)        
sum(7,9)
sum(7,9,10,11)
sum(7,10,9,8,7,6)

# 2 - apresentação de cursos
def apresentação(**data):
    for key,value in data.items():
        print(f'{key} - {value}')


apresentação(name='python', categoria='backend' , level='inciante')
apresentação(name='Jss', categoria='backend' , level='inciante')
apresentação(name= 'ruby' , categoria='backend' , level='inciante')