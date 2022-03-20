# Faça um Programa que peça a temperatura em graus Celsius,
#  transforme e mostre em graus Fahrenheit.
def converteGraus (c):
    fahre = round((c*9)/5+32,2)
    return fahre

c = float(input('Temperatura em graus Celsius: '))
fahre = converteGraus(c)
print(str(f'{fahre}° graus Fahrenheit'))