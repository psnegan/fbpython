DT=int(input("Digite os dias"))
meses = int((DT%365)/30)
dias = int((DT%365)%30)
anos=(DT//365)

print(f"Você viveu {dias} dias, {meses} meses, {anos} anos")