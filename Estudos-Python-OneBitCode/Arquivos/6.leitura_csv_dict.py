cursos = []

with open('cursos.csv','r',encoding='utf-8')as f:
    for line in f:
        linguagens, categorias = line.rstrip().split(',')
        cursos = {}
        cursos['linguagens'] = linguagens
        cursos['categoria'] = categorias
        cursos.append(cursos)
print(cursos)