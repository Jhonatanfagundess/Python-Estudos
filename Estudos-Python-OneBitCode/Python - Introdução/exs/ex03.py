distancia = float(input('Quantos kms deu a sua viagem ?\n'))
if distancia > 200 :
    km = 0.35
    result = distancia * km
    print(f'O valor da sua viagem é {result}')
else :
    km = 0.50
    result = distancia * km
    print(f'O valor da sua viagen é {result}')
    
  
salario = float(input('Qual o valor do seu salário ?'))
if salario > 1250.00 :
    aumento = 0.10
    result = salario * aumento
    print(f'O seu salário vai para :{result}')
else: 
    aumento = 0.15
    result = salario * aumento
    print(f'O seu salário vai para: {result}')    
    