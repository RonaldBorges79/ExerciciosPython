#Faça um Programa que pergunte quanto você ganha por hora e
#o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

salHora = float(input('Quanto você ganha por hora: '))
horaMes = float(input('Quantas horas trabalhadas no mês: '))
minMes = int(input('Quantidade de minutos trabalhados no mês: '))
min = round((minMes/60),2)
salMes = round((horaMes + min)*salHora,2)
print(f'Salário referente ao mês: R${salMes}')
