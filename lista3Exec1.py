#1- A prefeitura de uma cidade fez uma pesquisa entre 3 de seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:   
#a) média do salário da população; 
#b) média do número de filhos; 
#c) maior salário; 
#d) percentual de pessoas com salário até R$100,00.  
qtde = int(input("Digite o numero de habitantes"))
habitantes= range(1,qtde)
salario=0.00
numero_filhos = 0
total_filhos= 0
media_salarial= 0.00
total_salario= 0.00
maior_salario= 0.00
percentual_salario_1000 = 0.00
contador_salario_1000 = 0



for pessoa in habitantes:
    print("habitante",pessoa+1)
    salario = int(input("Digite o salario : "))
    numero_filhos = int(input("Digite o numero de filhos : "))
    
    total_salario= total_salario+ salario
    total_filhos = total_filhos + numero_filhos

    if salario> maior_salario:
        maior_salario= salario
        if salario<=100:
            contador_salario_1000= contador_salario_1000+1

    media_salarial= total_salario/qtde
    media_filhos = total_filhos/qtde
    percentual_salario_1000=(percentual_salario_1000/qtde)*100


    print(f"total de salarios R$ : {total_salario}")
    print(f"maior salario é R$: {maior_salario}")
    print(f"media salaraial R$ : {media_salarial}")
    print(f"media de filhos : {media_filhos}")
    print(f"Percentual de pessoas com salario até 100{percentual_salario_1000}")

    print("Fim de programa")
