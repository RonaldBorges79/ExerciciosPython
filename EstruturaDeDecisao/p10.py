# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
# ou "Valor Inválido!", conforme o caso.

#------------------------------------------------------ Tipo Turno.
turno = input("Digite o turno que você estuda: (m)Matutino, (v)Vespertino ou (n)Noturno. ")
#------------------------------------------------------ Matutino.
if(turno == "m" or  turno == "M"):
    print("Bom dia!")
#------------------------------------------------------ Vespetino.
elif(turno == "v" or turno == "V"):
    print("Boa Tarde!")
#------------------------------------------------------ Noturno.
elif(turno == "n" or turno == "N"):
    print("Boa Noite!")
#------------------------------------------------------ Valor inválido.
else:
    print("Valor inválido!")