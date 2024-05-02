while True:
    try:
            idade = int(input("Digite a idade : "))

            if idade < 5:
                print("Não atendemos nesta faixa etaria!!!")
            
        
            elif idade < 8:
             print('infantil A')


            elif idade < 12:
                print('Infantil B')
            elif idade < 14:
                print('JUVENIL A')
            elif idade<18:
                print('Juvenil B')
            else:
                print("Adulto")
    except:
         print('Você digitou errado')
         op= input('Continua S/N :').upper()
         if op =='N': 
            print('Fim de programa')
    