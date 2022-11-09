#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input("Digite seu nome completo: "))
nome = nome.upper().find("SILVA")
#print(nome)
if nome == -1:
    print("O nome não tem SILVA")
else:
    print("o nome tem SILVA")


### OUTRA FORMA DE RESOLVER ###
#nome = str(input("Qual é seu nome completo? ")).strip()
#print("Seu nome tem Silva? {}".format("silva" in nome.lower()))