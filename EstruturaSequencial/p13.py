# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def calcularImc(sexo,h):
    if(sexo == 'M' or sexo == 'm'):
        pesoIdeal =round ((72.7 * h) - 58,2)
        return pesoIdeal
    elif(sexo == 'F' or sexo == 'f'):
        pesoIdeal =round ((62.1*h) - 44.7,2)
        return pesoIdeal
    else:
        pesoIdeal = print('Sexo inválido!')
        return pesoIdeal

sexo = input("Digite o seu sexo (f) para feminino ou (m) para masculino: ")
h = float(input("Digite a sua altura (ex: 1.90):  "))

pesoIdeal = calcularImc(sexo,h)
print(str(f'{pesoIdeal}'))