#5 Faça um programa que leia as 3 notas de um aluno e calcule a média final
#deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2,3 e
#5, respectivamente.
import math
nota1= int(input("Digite a primeira nota : "))
nota2= int(input("Digite a segunda nota : "))
nota3= int(input("Digite a terceira nota : "))

nota1=(nota1)*0.2
nota2=(nota2)*0.3
nota3=(nota3)*0.5
media= (nota1+nota2+nota3)

print(f"o valor final é {media:.2f}media")

