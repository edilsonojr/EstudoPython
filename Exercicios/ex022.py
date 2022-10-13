#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo(Sem considerar espaços)
#Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))
print("Todas letras em maiúsculas: ", nome.upper())
print("Todas letras em minúsculas: ", nome.lower())
print("Total de letras sem espaços antes e depois: ", len(nome.strip()))
print("Número de letras no primeiro nome: ", len(nome.split()[0]))
