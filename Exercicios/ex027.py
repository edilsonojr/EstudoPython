#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiroe o e último nome separadamente

nome = str(input("Digite seu nome completo: "))
print("O seu primeiro nome é: {}".format(nome.split()[0]))
print("O seu último nome é: {}".format(nome.split()[-1]))


### OUTRA FORMA DE RESOLVER ###
#frase = str(input("Digite uma frase: ")).upper().strip()
#print("A letra A aparece {} vezes na frase".format((frase.count("A"))))
#print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
#print("A última letra A apareceu na posição {}".format(frase.rfind("A"+1)))