perguntas = [
    {
        "pergunta": "1. Qual é a capital da França?",
        "opcoes": ["a) Paris", "b) Roma", "c) Berlim", "d) Londres"],
        "resposta": "a"
    },
    {
        "pergunta": "2. Qual é a resposta para a vida, o universo e tudo mais?",
        "opcoes": ["a) 45", "b) 40", "c) 42", "d) 39"],
        "resposta": "c"
    },
    {
        "pergunta": "3. Quem pintou Mona Lisa?",
        "opcoes": ["a) Leonardo da Vinci", "b) Salvador Dalí", "c) Van Gogh", "d) Tarsila do Amaral"],
        "resposta": "a"
    },
    {
        "pergunta": "4. Qual o nome popular do cloreto de sódio?",
        "opcoes": ["a) Vinagre", "b) Água", "c) Sal de cozinha", "d) Fermento"],
        "resposta": "c"
    },
    {
        "pergunta": "5. O que os pandas comem?",
        "opcoes": ["a) Mel", "b) Carnes", "c) Aves, ovos e peixe", "d) Bambu"],
        "resposta": "d"
    },
    {
       "pergunta": "6. Quantos andares tem o maior prédio do mundo?",
       "opcoes": ["a) 100", "b) 200", "c) 163", "d) 70"],
       "resposta": "c"
    },
    {
       "pergunta": "7. Em que ano foi usado um celular pela primeira vez no Brasil?",
       "opcoes": ["a) 1900", "b) 1990", "c)2000", "d) 2020"],
       "resposta": "b"
    },
    {
       "pergunta": "8. Qual era a nacionalidade de Napoleão Bonaparte?",
       "opcoes": ["a) Francesa", "b) Brasileira", "c) Mexicana", "d) Japonesa"],
       "resposta": "a"
    },
    {
       "pergunta": "9. Que grande evento histórico aconteceu em 1822 no Brasil?",
       "opcoes": ["a) Descobrimento do Brasil", "b) Ditadura Militar", "c) Revolução de 1930", "d) Independência do Brasil"],  
       "resposta": "d"    
    }
    # Adicione mais perguntas aqui
]

def fazer_quiz(perguntas):
    pontuacao = 0
    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)
        
        resposta = input("Escolha a opção correta (a, b, c ou d): ")
        
        if resposta == pergunta["resposta"]:
            print("correta!")
            pontuacao += 1
        else:
            print("Resposta incorreta!")
        
        print()  # Adicione uma linha em branco entre as perguntas
        
    print("Pontuação final: {}/{}".format(pontuacao, len(perguntas)))

fazer_quiz(perguntas)


#MODELO 
   #{
   #    "pergunta": "",
   #    "opcoes": ["a) ", "b) ", "c) ", "d) "],
   #    "resposta": ""
   #},
