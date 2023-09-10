class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self): 
        return self.largura * self.altura
    
#Exemplo
retangulo = Retangulo(10, 20)
print(f'A área do retângulo é: {retangulo.calcular_area()}m²')
