import os
os.system
lista = []
letras= list("EPAMINONDAS")
numeros = list(range(10))

print(lista)
print(letras)
print(numeros)

print("Ultimo caractere da lista letras",numeros[-1])
listanova= letras+numeros
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova.pop()
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
del listanova[10]
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova.append("EXEMPLO")
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova.insert(10,"s")
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova[10]="S"
print(listanova)
print("Tamanho da lista nova é ",len(listanova))

for indice, item in enumerate (listanova):
    print(indice,item)
    