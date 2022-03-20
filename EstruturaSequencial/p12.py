# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

def calcularImc (altura):
    pesoIdeal = round((72.7*altura) - 58,2)
    return pesoIdeal

altura=float(input('Digite a sua Altura (ex: 1.90): '))
pesoIdeal = calcularImc(altura)
print(f'Seu peso ideal é {pesoIdeal}.')