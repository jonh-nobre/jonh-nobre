#SOMA 1
numeros_1 = (1, 2, 3)
numeros_2 = (4, 5, 6)
numeros_3 = (7, 8, 9)

soma = (numeros_1 + numeros_2 + numeros_3)

print(soma)

print("\n")

#SOMA 2
valor_oculto = (100)

operador_1 = int(input('Entre com o número primeiro que será usado na soma: '))
operador_2 = int(input('Agora, entre com o segundo: '))
operador_3 = int(input('O terceiro número agora: '))
operador_4 = int(input('Por fim, entre com o quarto: '))

resultado_soma = operador_1 + operador_2 + operador_3 + operador_4

if operador_1 + operador_2 + operador_3 + operador_4 == valor_oculto:
    print('Parabéns! Acertou!')
    print(f'Você digitou {operador_1} + {operador_2} + {operador_3} + {operador_4} + {resultado_soma}')
    print(f'O valor oculto foi {valor_oculto}')

elif operador_1 + operador_2 + operador_3 + operador_4 == (99 or 101): 
    print('Chegou perto!')
    print(f'Você digitou {operador_1} + {operador_2} + {operador_3} + {operador_4} = {resultado_soma}')

else:
    print('Você errou!')
    print(f'Você digitou {operador_1} + {operador_2} + {operador_3} + {operador_4} = {resultado_soma}')
    print('Mais sorte na próxima vez!')
