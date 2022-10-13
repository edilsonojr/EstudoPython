#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input("Digite seu nome completo: "))
nome = nome.upper().find("SILVA")
#print(nome)
if nome == -1:
    print("O nome não tem SILVA")
else:
    print("o nome tem SILVA")
