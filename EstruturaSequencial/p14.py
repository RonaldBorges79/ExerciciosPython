# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá
# pagar. Imprima os dados do programa com as mensagens adequadas.

def calcularKL(peso_de_peixes):
    multa = (peso_de_peixes - 50) * 4
    return multa

peso_de_peixes = float(input("Digite a quantadade de KL do peixe: "))
if(peso_de_peixes >50):
    multa = calcularKL(peso_de_peixes)
    print(f"Terá que pagar R${multa}.")
else:
    print('Não ultrapassou o limite!')