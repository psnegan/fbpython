contador = 0
total = 0
numero = int (input("Digite um numero entre 2 e 9 :"))

while true:
    print(contador,sep="+",end="")
    contador=contador+1
    if contador > numero:
        break

    print('fim de programa')