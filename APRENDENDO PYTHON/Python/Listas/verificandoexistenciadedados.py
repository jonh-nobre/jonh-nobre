notas = ['4,0', '5,0', '2,5', '7,0,','9,0','8,5']
print('8,0' in notas)
print('5,0' in notas)
print('2,5' in notas)
print('10,0' in notas)

print('-'*100)

valores_inteiros = [430,693,219,835,1000]
print(1000 in valores_inteiros)
print(430 in valores_inteiros)
print(3002 in valores_inteiros)

partes_do_corpo = ['Cabeça','Braços','Joelhos','Nariz','Umbigo']

if 'Nariz' in partes_do_corpo:
    print('Dado existente!')
else:
    print('Dado inexistente!')