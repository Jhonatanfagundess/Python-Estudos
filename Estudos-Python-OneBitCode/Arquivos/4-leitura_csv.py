with open('cursos.csv', 'r', encoding='utf-8') as f:
    for line in f:
    #    row = line.rstrip().split(',')
    #    print(f'{row[0]} - {row[1]}')
        linguagens, categoria = line.rstrip().split(',')
        print(f'{linguagens} - {categoria}')
    