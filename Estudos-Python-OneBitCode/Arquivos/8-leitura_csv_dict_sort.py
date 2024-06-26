courses = []
with open("cursos.csv", encoding="utf-8") as file:
    for line in file:
        linguagens, categoria = line.rstrip().split(",")
        course = {}
        course["linguagens"] = linguagens
        course["categoria"] = categoria
        courses.append(course)
print(courses)

for course in sorted(courses, key=lambda course: course["linguagens"], reverse=True):
    print(f"{course['linguagens']} -{course['categoria']}")