# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def calcularDownload(mbps, mb):
    seg = mb / mbps
    tempDownload = round((seg // 60),2)
    return tempDownload

mb = float(input("Qual a quantidade de MB: "))
mbps = float(input("A velocidade de um link de Internet (em Mbps): "))

tempDownlaod = calcularDownload(mbps, mb)

print(f'Levará {tempDownlaod} minutos para terminar esse download.')