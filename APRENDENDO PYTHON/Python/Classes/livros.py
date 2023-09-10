class SerieLivros:
    def __init__(self, nome, livros, volumes):
        self.nome = nome
        self.livros = livros
        self.volumes = volumes

    def dados(self):
        print(f'Nome: {self.nome}')
        print(f'Quantidade de livros: {self.livros}')
        print(f'Volumes em ordem: {self.volumes}')
    
books_ds = ('Mau Começo', 'A Sala dos Répteis', 'O Lago das Sanguessugas',
            'Serraria Baixo-Astral', 'Inferno no Colégio Interno', 'O Elevador Ersatz', 
            'A Cidade Sinistra dos Corvos', 'O Hospital Hostil', 'O Espetáculo Carnívoro', 
            'O Escorregador de Gelo', 'A Gruta Gorgônea', 'O Penúltimo Perigo',
            'O Fim')

books_hp = ('Pedra Filosofal', 'Câmara Secreta', 'Prisioneiro de Azkaban',
            'Cálice de Fogo', 'Ordem da Fênix', 'Enigma do Príncipe',
            'Relíquias da Morte')

books_jv = ('Jogos Vorazes', 'Em Chamas', 'A Esperança', 
            'A Cantiga dos Pássaros e das Serpentes')

books_di = ('Divergente', 'Insurgente', 'Convergente', 'Quatro')

books_sa = ('A Sociedade do Anel', 'As Duas Torres', ' O Retorno do Rei')

serie_1 = SerieLivros('Desventuras em Série', 13, books_ds)
serie_2 = SerieLivros('Harry Potter', 7, books_hp)
serie_3 = SerieLivros('Jogos Vorazes', 4, books_jv)
serie_4 = SerieLivros('Divergente', 4, books_di)
serie_5 = SerieLivros('O Senhor dos Anéis', 3, books_sa)

serie_1.dados()
print("="*150)
serie_2.dados()
print("="*150)
serie_3.dados()
print("="*150)
serie_4.dados()
print("="*150)
serie_5.dados()
print("="*150)