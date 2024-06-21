cursos = []

with open ('cursos.csv', 'r', encoding='utf-8') as f:
    for line in f:
        linguagens, categorias = line.rstrip().split(',')
        cursos.append(f'{linguagens} - {categorias}')
        
for cursos in sorted(cursos):
    print(cursos)        