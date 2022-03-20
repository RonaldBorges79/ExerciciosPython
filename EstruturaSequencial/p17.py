# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta 
# é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# ------------------------------------------- Carácteristicas.
coberturaTinta = 6
capacLata = 18
precoLata = 80
capacGalao = 3.6
precoGalao = 25
# ------------------------------------------- Litros necessários.
def calcularL (m):
    litro = round((m/6),2)
    return litro
# ------------------------------------------- opcão 1.
def calcularOpcao1 (litro):
    lata = int(litro / capacLata)
    if (litro % capacLata !=0):
        lata += 1
        return lata

def calcularPrecoOpcao1 (lata):
    precoTotalLata = lata * precoLata
    return precoTotalLata
# ------------------------------------------- opção 2.
def calcularOpcao2 (litro):
    galao = int(litro / capacGalao)
    if (litro % capacGalao !=0):
        galao += 1
        return galao

def calcularPrecoOpcao2 (galao):
    precoTotalGalao = galao * precoGalao
    return precoTotalGalao
# ------------------------------------------- opção 3.
def calcularLataOpcao3(litro):
    lata3 = int(litro/ capacLata)
    if (lata3 != 0):
        lata3 += 1
        return lata3
    else:
        lata3 = 0
        return lata3

def calcularGalaoOpcao3 (lata3):
    galao3= int(lata3 / capacGalao)
    if (galao3 != 0):
        galao3 += 1
        return galao3
    else:
        galao3 = 0
        return galao3

def calcularOpcao3(lata3, galao3):
    opcao3 = round((lata3 * precoLata) + (galao3 * precoGalao),2)
    return opcao3

m  = float(input("Digite quantos metros quadrados deseja pintar: "))

litro = calcularL (m)
lata = calcularOpcao1 (litro)
precoTotalLata = calcularPrecoOpcao1 (lata)
galao = calcularOpcao2(litro)
precoTotalGalao = calcularPrecoOpcao2 (galao)
lata3 = calcularLataOpcao3 (litro)
galao3 = calcularGalaoOpcao3(lata3)
opcao3 = calcularOpcao3(lata3, galao3)

print(f'''
        Litros necessários: {litro} L
------------------------------------------------
        Quantidade de latas de Tinta: {lata}
        Preço: R${precoTotalLata}
------------------------------------------------
        Quantidade de Galões de tinta: {galao}
        Preço: R${precoTotalGalao}
------------------------------------------------
        Quantidade de latas e galões de tinta: 
        Latas:{lata3}
        Galões: {galao3}
        Preço: R${opcao3}
''')
