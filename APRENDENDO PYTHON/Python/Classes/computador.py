class Computador:
    def __init__(self, tamanho, armazenamento):
        self.tamanho = tamanho
        self.armazenamento = armazenamento

    def mostrar_especificacoes(self):
        print("Tamanho da tela: " + self.tamanho)
        print("Armazenamento: " + self.armazenamento)    

menor_especificacao = Computador("13", "256GB")
maior_especificacao = Computador("27", "1TB")

print("Menor especificação de computador")
menor_especificacao.mostrar_especificacoes()

print("Maior especificação de computador")
maior_especificacao.mostrar_especificacoes()
