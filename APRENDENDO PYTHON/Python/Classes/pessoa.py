class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def cumprimentar(self):  
        print(f'Olá, meu nome é {self.nome}.')  
        print(f'Tenho {self.idade} anos de idade.')
        print(f'Minha altura é {self.altura}')

#Exemplo
pessoa = Pessoa('João', 30, 1.74)
pessoa.cumprimentar()        