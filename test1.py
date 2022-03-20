def somar (a,b):
    soma= round((a + b),2)
    return soma
def subtrair (a,b):
    subtrai = round((a - b),2)
    return subtrai
def divisao (a,b):
    dividi = round((a / b),2)
    return dividi
def multiplicar (a,b):
    multiplica = round ((a * b),2)
    return multiplica
def restoDaDivisao (a,b):
    resto = round((a % b),2)
    return resto
def inteiroDivisao (a,b):
    intDividi = round((a // b),2)
    return intDividi
resp = True
while resp:
    print("""
    ------- Operações Matemática -------
            1.Somar.
            2.Subtrair.
            3.Divisão.
            4.Multiplicação.
            5.Resto da Divisão.
            6.Inteiro da Divisão.
            7.Sair/Exit
          """)
    print("\n")
    opcao = int(input("Digite a opcão desejada: "))

    if opcao ==1:
        print('------- Soma -------')
        a = float(input('Digite o 1. número: '))
        b = float(input('Digite o 2. número: '))
        soma = somar(a,b)
        print(str(f'{soma}'))

    elif opcao == 2:
        print('----- Subtrair -----')
        a = float(input('Digite o 1. número: '))
        b = float(input('Digite o 2. número: '))
        subtrai = subtrair(a,b)
        print(str(f'{subtrai}'))

    elif opcao == 3:
        print('------ Divisão ------')
        a = float(input('Digite o 1. número: '))
        b = float(input('Digite o 2. número: '))
        dividi = divisao(a,b)
        print(str(f'{dividi}'))

    elif opcao == 4:
        print('--- Multiplicação ---')
        a = float(input('Digite o 1. número: '))
        b = float(input('Digite o 2. número: '))
        multiplica = multiplicar(a,b)
        print(str(f'{multiplica}'))

    elif opcao == 5:
        print('--- Resto Divisão ---')
        a = float(input('Digite o 1. número: '))
        b = float(input('Digite o 2. número: '))
        resto = restoDaDivisao(a,b)
        print(str(f'{resto}'))
        
    elif opcao == 6:
        print('-- Inteiro Divisão --')
        a = float(input('Digite o 1. número: '))
        b = float(input('Digite o 2. número: '))
        intDividi = inteiroDivisao(a,b)
        print(str(f'{intDividi}'))

    else:
        resp=False
        print('Fim do Programa')
