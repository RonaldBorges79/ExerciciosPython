# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite 1° número: "))
num2 = float(input("Digite 2° número: "))
num3 = float(input("Digite 3° número: "))

if(num1 > num2 and num1 > num3):
    print(f"O 1° número: {num1} é o maior número.")
elif(num1 < num2 and num2 > num3):
    print(f"O 2° número: {num2} é o maior número.")
elif(num1 < num3 and num2 < num3):
    print(f"O 3° número: {num3} é o maior número.")