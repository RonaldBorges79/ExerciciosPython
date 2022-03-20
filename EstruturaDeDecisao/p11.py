# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste 
# segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

#------------------------------------------------------ Salario.
salario = float(input("Digite o salário do coloborador: R$"))
#------------------------------------------------------ Aumento de 20%.
if(salario <= 280):
    aumento = 1.20
    novoSalario=salario * aumento
    valorAumento = novoSalario - salario
    percentual = round((valorAumento * 100) / salario,2)
    print(f'''
        Salario Antigo: R${salario}
        Percentual de aumento: {percentual}%
        Valor do aumento: R${valorAumento}
        Novo salalario: {novoSalario}''')
#------------------------------------------------------ Aumento de 15%.
elif(salario > 280 and salario <= 700):
    aumento = 1.15
    novoSalario=salario * aumento
    valorAumento = novoSalario - salario
    percentual = round((valorAumento * 100) / salario,2)
    print(f'''
        Salario Antigo: R${salario}
        Percentual de aumento: {percentual}%
        Valor do aumento: R${valorAumento}
        Novo salalario: {novoSalario}''')
#------------------------------------------------------ Aumento de 10%.
elif(salario > 700 and salario <= 1500):
    aumento = 1.10
    novoSalario=salario * aumento
    valorAumento = novoSalario - salario
    percentual = round((valorAumento * 100) / salario,2)
    print(f'''
        Salario Antigo: R${salario}
        Percentual de aumento: {percentual}%
        Valor do aumento: R${valorAumento}
        Novo salalario: {novoSalario}''')
#------------------------------------------------------ Aumento de 5%.
elif(salario > 1500):
    aumento = 1.05
    novoSalario=salario * aumento
    valorAumento = novoSalario - salario
    percentual = round((valorAumento * 100) / salario,2)
    print(f'''
        Salario Antigo: R${salario}
        Percentual de aumento: {percentual}%
        Valor do aumento: R${valorAumento}
        Novo salalario: {novoSalario}''')