#Faça um Programa que calcule a área de um quadrado,
#em seguida mostre o dobro desta área para o usuário.
print('------Dobro da Área------')
base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))
area = round((base*altura)*2,2)
print(f'O dobro da área é {area} cm')
