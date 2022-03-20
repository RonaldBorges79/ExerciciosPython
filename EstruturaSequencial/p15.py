# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

def calcularSalario(min, hora, salHora):
    minsalario = round((min/60),2)
    salario = round((hora+minsalario)*salHora,2)
    return salario

def calcularImposto(salario):
    imposto = round((salario*0.11),2)
    return imposto

def calcularINSS (salario):
    inss = round((salario*0.08),2)
    return inss

def calcularSindicato (salario):
    sindicato = round((salario * 0.05),2)
    return sindicato

def calcularSalarioLi (salario, sindicato, inss, imposto):
    desconto = sindicato + inss + imposto
    salarioLi = round((salario - desconto),2)
    return salarioLi

print           ("------------ Calcular Salário ------------")
hora = int(input("Digite a quantidade de horas trabalhadas: "))
min = int(input("Digite a quantidade de minutos trabalhados: "))
salHora = float(input("Digite quanto ganha por hora: "))

salario = calcularSalario(min, hora, salHora)
imposto = calcularImposto(salario)
inss = calcularINSS(salario)
sindicato = calcularSindicato(salario)
salarioLi = calcularSalarioLi(salario, sindicato, inss, imposto)

print(f'''
    Salário bruto: R${salario}.
    Imposto: R${imposto}.
    Quanto pagou ao INSS: R${inss}.
    Quanto pagou ao sindicato: R${sindicato}.
    O salário líquido: R${salarioLi}.
    ''')