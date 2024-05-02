

#6. Construa um programa que, tendo como dados de entrada dois pontos
#quaisquer no plano, P(x1, y1) e P(x2, y2), escreva a distância entre eles. A fórmula
# que efetua tal cálculo é:
import math as mat
x1=int(input("Digite o x1 : "))
y1=int(input("Digite o y1 : "))
x2=int(input("Digite o x2 : "))
y2=int(input("Digite o y2 : "))


d1=mat.pow((x2-x1),2.+mat.pow((x2-x1),2.))
d=mat.sqrt((x2-x1)**2+(y2-y1)**2)




print(f"d é igual a : {d}d")