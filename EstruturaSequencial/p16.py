# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
# de latas de tinta a serem compradas e o preço total.

def quantidadeDeLatas(mquadrado):
    qtdtinta = mquadrado / 3
    qtdlatas = int(qtdtinta/18)
    if(qtdtinta % 18 !=0):
        qtdlatas += 1
        return qtdlatas

def calcularPreco (qtdlatas):
    precoTotal =80 * qtdlatas
    return precoTotal

mquadrado = float(input("Digite tamanho em metros quadrados da área a ser pintada: "))
qtdlatas = quantidadeDeLatas(mquadrado)
precoTotal = calcularPreco(qtdlatas)

print(f'''
    Quantidade de latas de tinta: {qtdlatas}
    Preço total: R${precoTotal}''')