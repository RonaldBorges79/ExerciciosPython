# Faça um Programa que leia três números e mostre-os em ordem decrescente.

#------------------------------------------------------ Valor números.
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))
#------------------------------------------------------ Ordem: 1° , 2°, 3°.
#------------------------------------------------------ Ordem: 1° , 3°, 2°.
if(n1>n2>n3):
    print(f"Ordem decrescente: {n1} - {n2} - {n3}")
elif(n1>n3>n2):
    print(f"Ordem decrescente: {n1} - {n3} - {n2}")
#------------------------------------------------------ Ordem: 2° , 1°, 3°.
#------------------------------------------------------ Ordem: 2° , 3°, 1°.
elif(n2>n1>n3):
    print(f"Ordem decrescente: {n2} - {n1} - {n3}")
elif(n2>n2>n1):
    print(f"Ordem decrescente: {n2} - {n3} - {n1}")
#------------------------------------------------------ Ordem: 3° , 1°, 2°.
#------------------------------------------------------ Ordem: 3° , 2°, 1°.
elif(n3>n1>n2):
    print(f"Ordem decrescente: {n3} - {n1} - {n2}")
elif(n3>n2>n1):
    print(f"Ordem decrescente: {n3} - {n2} - {n1}")