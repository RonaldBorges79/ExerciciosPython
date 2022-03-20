# Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = float(input("Digite 1° número: "))
num2 = float(input("Digite 2° número: "))
num3 = float(input("Digite 3° número: "))

#-------------------------------------------------- 1° número maior e os 2° e 3° número menor
if(num1 > num2 and num1 > num3 and num2 < num3):
    print(f"O 1° número: {num1} é o maior número.")
    print(f"O 2° número: {num2} é o menor número.")
elif(num1 > num2 and num1 > num3 and num2 > num3):
    print(f"O 1° número: {num1} é o maior número.")
    print(f"O 3° número: {num3} é o menor número.")
#-------------------------------------------------- 2° número maior e os 1° e 3° número menor
elif(num1 < num2 and num2 > num3 and num1 < num3):
    print(f"O 2° número: {num2} é o maior número.")
    print(f"O 2° número: {num1} é o maior número.")
elif(num1 < num2 and num2 < num3 and num1 > num3):
    print(f"O 2° número: {num2} é o maior número.")
    print(f"O 2° número: {num3} é o maior número.")
#-------------------------------------------------- 3° número maior e os 1° e 2° número menor
elif(num1 < num3 and num2 < num3 and num1 < num2):
    print(f"O 3° número: {num3} é o maior número.")
    print(f"O 1° número: {num1} é o maior número.")
elif(num1 < num3 and num2 < num3 and num1 > num2):
    print(f"O 3° número: {num3} é o maior número.")
    print(f"O 2° número: {num2} é o maior número.")