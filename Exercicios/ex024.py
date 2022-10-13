#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input("Digite o nome da cidade: "))
cidade = cidade.upper().split()[0]
#print(cidade)
verificador = 'SANTO' in cidade
if verificador == True:
    print("A cidade começa com SANTO")
else:
    print("A cidade não começa com SANTO e sim com {}".format(cidade))