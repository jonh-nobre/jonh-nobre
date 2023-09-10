

class Paises:
    def __init__(self, capital, continente):
        self.capital = capital
        self.continente = continente

    def informacoes(self):
       # print(f'Pais {self.pais')
        print(f'Capital: {self.capital}')
        print(f'Continente: {self.continente}')

pais_1 = Paises('Brasília', 'América do Sul') 
pais_2 = Paises('Washington, D.C.', 'América do Norte')
pais_3 = Paises('Madri', 'Europa')

print('BRASIL')
pais_1.informacoes()

print('-'*30)

print('ESTADOS UNIDOS')
pais_2.informacoes()

print('-'*30)

print('ESPANHA')
pais_3.informacoes()


