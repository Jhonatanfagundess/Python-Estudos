from openpyxl import workbook
#Criando o workbook
wb = workbook
name = 'files/test.xlsx'


#Criando o worksheet
ws1 = wb.ative
ws1.title = 'Planilha 1'

#ADD DADOS
data = [
    ['Ano','Lucro','Custos']
    [2021, '25%', '40%']
    [2022, '10%', '10%']
    [2023,'5%','15%']
]

for line in data:
    ws1.append(line)
    
wb.save(filename=name)    