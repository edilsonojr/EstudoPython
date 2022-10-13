#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiroe o e último nome separadamente

nome = str(input("Digite seu nome completo: "))
print("O seu primeiro nome é: {}".format(nome.split()[0]))
print("O seu último nome é: {}".format(nome.split()[-1]))