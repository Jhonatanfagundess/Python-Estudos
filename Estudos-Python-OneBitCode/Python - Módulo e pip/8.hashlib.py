import hashlib

#1 - Verificar algoritmos disponíveis
print(hashlib.algorithms_available)

#2 -Algoritmos diposníveis pelo OS
print(hashlib.algorithms_guaranteed)

#3 - Utilizando shan256
algo = hashlib.sha256()
print(algo.digest)
msg = 'Eu sou o melhor do mundo'.encode()
algo.update(msg)
print(algo.hexdigest())

#4 - Utilizando MD5
md5 = hashlib.md5()
md5.update(msg)
print(md5.hexdigest())