# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

def calcularDobro (num1,num2):
    result = (num1*2) * (num2/2)
    return result
def calcularSomaTriplo(num1, num3):
    somaTri =  (num1*3)+ num3 
    return somaTri

def calcularElevadoaoCubo(num3):
    eleCubo = num3 ** 3
    return eleCubo

num1 = int(input('Digite 1° número: '))
num2 = int(input('Digite 2° número: '))
num3 = float(input('Digite 3° número: '))

result = calcularDobro(num1,num2)
somaTri = calcularSomaTriplo(num1,num3)
eleCubo = calcularElevadoaoCubo(num3)

print(str(f'''
        A) o produto do dobro do primeiro com metade do segundo: {result}
        B) A soma do triplo do primeiro com o terceiro: {somaTri}
        C) O terceiro elevado ao cubo: {eleCubo}'''))