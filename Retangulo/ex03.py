class Retangulo():

    def __init__(self, ladoA, ladoB):

        self.ladoA = ladoA
        self.ladoB = ladoB

    def troca_valor(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def calculo_area(self):
        area = self.ladoA * self.ladoB
        return area

    def calculo_perimetro(self):
        perimetro = 2 * (self.ladoA + self.ladoB)
        return perimetro

    def resultado(self):
        return f"Area: {self.calculo_area}, Perimetro: {self.calculo_perimetro}"


retangulo1 = Retangulo(2, 2)
retangulo1.troca_valor(4, 4)
print(retangulo1.resultado())
