class Usuario():
    # as propriedades
    primeiroNome = ""
    ultimoNome = ""

    # método que diz Olá ao usuário
    def hello(self):
        return "Olá, " + self.primeiroNome + self.ultimoNome


usuario1 = Usuario()
usuario1.primeiroNome = "Jonnie"
usuario1.ultimoNome = " Bravo"

# Imprime a mensagem de saudação
print(usuario1.hello())
