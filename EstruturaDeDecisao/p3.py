# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o sexo (F) feminino ou (M) masculino: ")
if(sexo == "f" or sexo == "F"):
    print("F - Feminino")
elif(sexo == "m" or sexo == "M"):
    print("M - Masculino")
else:
    print("Sexo inválido!")