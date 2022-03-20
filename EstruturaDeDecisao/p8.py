# Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#------------------------------------------------------ Preços dos produtos.
prod1 = float(input("Digite do 1° preço do produto: "))
prod2 = float(input("Digite do 2° preço do produto: "))
prod3 = float(input("Digite do 3° preço do produto: "))
#------------------------------------------------------ 1° Produto com menor valor.
if(prod1 < prod2 and prod1 < prod3):
    print(f"O produto que você deve comprar é a 1° Opção: R${prod1}")
#------------------------------------------------------ 2° Produto com menor valor.
elif(prod1 > prod2 and prod2 < prod3):
    print(f"O produto que você deve comprar é a 2° Opção: R${prod2}")
#------------------------------------------------------ 3° Produto com menor valor.
elif(prod1> prod3 and prod2 > prod3):
    print(f"O produto que você deve comprar é a 3° Opção: R${prod3}")
