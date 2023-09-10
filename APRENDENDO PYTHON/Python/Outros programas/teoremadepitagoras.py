# O teorema de Pitágoras é uma expressão matemática 
# que relaciona os lados de um triângulo retângulo, conhecidos como hipotenusa e catetos. 
# Esse teorema não é válido para triângulos acutângulos ou obtusângulos, apenas para os retângulos.
# a2 = b2 + c2 # a = x
import math

b = 6
c = 8
x = b**2 + c**2

print("x =", x)

x = math.pow(x , 1/2)

print("O valor da hipotenusa é:" , int(x))

