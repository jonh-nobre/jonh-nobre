class Filmes:
    def __init__(self, nome, ano, duração):
        self.nome = nome
        self.ano = ano
        self.duração = duração

    def detalhes(self):
        print(f'Nome do filme: {self.nome}')   
        print(f'Ano de lançamento: {self.ano}')
        print(f'Tempo de duração: {self.duração}')

trilogia_original = ('Episódio IV - Uma Nova Esperança', 
                     'Episódio V - O Império Contra-Ataca', 
                     'Episódio VI - O Retorno do Jedi')         

trilogia_prequela = ('Episódio I - A Ameaça Fantasma',
                     'Episódio II - A Guerra dos Clones',
                     'Episódio III - A Vingança dos Sith')

trilogia_sequela = ('Episódio VII - O Despertar da Força',
                    'Episódio VIII - Os Últimos Jedi',
                    'Episódio IX - A Ascensão Skywalker')


filme_01 = Filmes(trilogia_original[0], '1977', '2 horas')
filme_02 = Filmes(trilogia_original[1], '1980', '2 horas')
filme_03 = Filmes(trilogia_original[2], '1983', '2 horas')

filme_04 = Filmes(trilogia_prequela[0], '1999', '2 horas')
filme_05 = Filmes(trilogia_prequela[1], '2002', '2 horas')
filme_06 = Filmes(trilogia_prequela[2], '2005', '2 horas')

filme_07 = Filmes(trilogia_sequela[0],  '2015', '2 horas')
filme_08 = Filmes(trilogia_sequela[1],  '2017', '2 horas')
filme_09 = Filmes(trilogia_sequela[2],  '2019', '2 horas')



filme_01.detalhes()
print('-'*150)
filme_02.detalhes()
print('-'*150)
filme_03.detalhes()
print('-'*150)
filme_04.detalhes()
print('-'*150)
filme_05.detalhes()
print('-'*150)
filme_06.detalhes()
print('-'*150)
filme_07.detalhes()
print('-'*150)
filme_08.detalhes()
print('-'*150)
filme_09.detalhes()


