evento=int((input("Digite os segundos do evento")))
horas = evento//3600
minutos = (evento%3600)//60
segundos=(evento%3600)//60
print(f"evento é {horas}horas,{minutos} minutos, {segundos} segundos")