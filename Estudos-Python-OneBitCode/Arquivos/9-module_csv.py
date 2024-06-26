import csv

cursos = []
with open('cursos.csv','r',encoding='utf-8')as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursos.append({"name": row["linguagens"], "category": row["category"]})
        
for course in sorted(cursos, key=lambda course: course["linguagens"], reverse=True):
    print(f"{cursos['name']} -{cursos['category']}")