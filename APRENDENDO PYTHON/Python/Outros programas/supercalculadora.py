import time
import sys
   
print("ESSA É A SUPER CALCULADORA!")
 
time_duration = 2.0
time.sleep(time_duration)

print("A SUPER CALCULADORA VAI CALCULAR OS NÚMEROS QUE VOCÊ DIGITAR!")

time_duration = 2.0
time.sleep(time_duration)

print("MAS ANTES, ESCOLHA QUAL A OPERAÇÃO QUE DESEJA REALIZAR DE ACORDO COM A PRÓXIMA INSTRUÇÃO...")

time_duration = 2.0
time.sleep(time_duration)

operation = input('DIGITE "A" PARA ADIÇÃO, "S" PARA SUBTRAÇÃO, "M" PARA MULTIPLICAÇÃO OU  "D" PARA DIVISÃO: ')

if operation == "A":
    print('AGORA, DIGITE OS VALORES PARA SEREM SOMADOS...')
    
    x = int(input('DIGITE O PRIMEIRO VALOR: '))

    time_duration = 2.0
    time.sleep(time_duration)
    
    y = int(input('DIGITE O SEGUNDO NÚMERO: '))
    
    z = x + y

    print('O RESULTADO DA SOMA É:', z)   

elif operation == "S":
     
     print('AGORA, DIGITE OS VALORES PARA SEREM SUBTRAIDOS...')

     x = int(input('DIGITE O PRIMEIRO VALOR: '))

     time_duration = 2.0
     time.sleep(time_duration)

     y = int(input('DIGITE O SEGUNDO NÚMERO: '))
     
     z = x - y

     print('O RESULTADO DA SUBTRAÇÃO É:', z)   

elif operation == "M":
     
     print('AGORA, DIGITE OS VALORES PARA SEREM MULTIPLICADOS...')

     x = int(input('DIGITE O PRIMEIRO VALOR: '))
     
     time_duration = 2.0
     time.sleep(time_duration)

     y = int(input('DIGITE O SEGUNDO NÚMERO: '))
     
     z = x * y

     print('O RESULTADO DA MULTIPLICAÇÃO É:', z)   

elif operation == "D":
     
     print('AGORA, DIGITE OS VALORES PARA SEREM DIVIDIDOS...')

     x = int(input('DIGITE O PRIMEIRO VALOR: '))
     
     time_duration = 2.0
     time.sleep(time_duration)

     y = int(input('DIGITE O SEGUNDO NÚMERO: '))
     
     z = x / y

     print('O RESULTADO DA DIVISÃO É:', z)   

else:
    print('LETRA INCORRETA')    