class Bola():

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return f"Cor da bola: {self.cor}, circunferencia {self.circunferencia}, material {self.material}"


bola1 = Bola("Branca", "68cm", "Couro")
bola1.trocaCor("Azul")
print(bola1.mostraCor())
