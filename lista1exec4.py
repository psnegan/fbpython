import math

A = int(input("Digite o valor de A : "))
B = int(input("Digite o valor de B : "))
C = int(input("Digite o valor de C : "))

try:
    A = int(a)
    B = int(b)
    C = int(c)
    
    R = (A+B)**2
    S = math.pow((B+C), 2.0)
    D = (R+S)/2
except:
    print("Você não digitou um valor válido")

R = (A+B)**2
S = math.pow((B+C), 2.0)
D = (R+S)/2

print(f"o valor de D = {D:.2f}")

