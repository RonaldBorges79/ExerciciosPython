#Faça um Programa que peça o raio de um círculo,
#calcule e mostre sua área.
import math
raio  = float(input('Digite o raio do círculo: '))
area = round(math.pi*math.pow(raio,2),1)
print(f'{area} cm²')
