import json

#1 - Strings para dicionários
person =  '{"name": "Rodrigo", "languagens": ["Python", "Javascript"]}' 
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

#2 - Dicionário para Json
person_json = json.dumps(person_dict)
print(person_json)

#3 - Formatando um Json
print(json.dumps(person_dict , indent=4, sort_keys=True))

#4 - Salvando Json em TXT
with open("person.txt","w") as json_file:
    json.dump(person_dict,json_file)
    
    
#5 - Lendo um Json Externo
with open("iris.json","r") as f:
    data = json.load(f) 
print(data)    
#Arquivos Iris com problemas