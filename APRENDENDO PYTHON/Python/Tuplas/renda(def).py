renda = (5000, 3000, 2500)

def salario():
    salario = float(input('Qual o seu salário? '))
    if salario in renda:
        print('Muito bem!')
    else:
        print('Que pena!')    
       
salario()    

