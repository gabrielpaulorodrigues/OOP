class Quadrado():

    def __init__(self, tamanho):
        self.tamanho = tamanho

    def trocaValor(self, novo_valor):
        self.tamanho = novo_valor

    def calculoArea(self):
        return f"{self.tamanho * 2}"


quadrado1 = Quadrado(2)
quadrado1.trocaValor(5)
print(quadrado1.calculoArea())
