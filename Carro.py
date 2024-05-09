class Carro:
    def __init__(self,marca,cor,motor,velocidade=0,ligado=False):
        self.marca = marca
        self.cor = cor 
        self.motor = motor
        self.velocidade = velocidade
        self.ligado = ligado
    def ligar(self):
        self.ligado= True
        print("Carro ligado")

    def acelerar(self):
        if self.ligado:
            if self.velocidade<=190:
                print("velocidade atual :",self.velocidade)
                print("Acelerando...")
                self.velocidade=self.velocidade+10
                print("velocidade atual :",self.velocidade)
            else:
                    print("primeiro ligue o carro.")

    def freiar(self):
            if self.ligado:
                if self.velocidade>=10:
                    print("velocidade atual :",self.velocidade)
                    print("freando...")
                    self.velocidade = self.velocidade-10
                    print("velocidade atual :",self.velocidade)
                else:
                    print("Carro parado")
            else:
                print("Carro Desligado")



    class Moto:
            ...

            class CarroGrande:
                def __init__(self,marca,cor,motor,eixos,velocidade=0,ligado=False):
                    self.marca = marca
                    self.cor= cor
                    self.motor=motor
                    self.eixos = eixos
                    self.velocidade= velocidade
                    self.ligado = ligado