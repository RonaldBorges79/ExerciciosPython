# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
def converteGraus (f):
    celsius = round(5*(f-32)/9,2)
    return celsius

f = float(input('Temperatura em graus Fahrenheit: '))
celsius = converteGraus(f)
print(str(f'{celsius}°graus Celsius.'))