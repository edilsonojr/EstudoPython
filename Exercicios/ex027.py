#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiroe o e último nome separadamente

nome = str(input("Digite seu nome completo: ")).strip()
print("O seu primeiro nome é: {}".format(nome.split()[0]))
print("O seu último nome é: {}".format(nome.split()[-1]))


### OUTRA FORMA DE RESOLVER ###
#n = str(input("Digite seu nome completo: ")).strip()
#nome = n.split()
#print("Muito prazer em te conhecer! ")
#print("Seu primeiro nome é {}".format(nome[0]))
#print("Seu último nome é {}".format(nome[len(nome)-1]))