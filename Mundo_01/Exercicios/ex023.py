#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separadados.
#Ex.: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

numero = int(input("Digite um número entre 0 e 9999: "))
uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print("Unidade--> {}".format(uni))
print("Dezena---> {}".format(dez))
print("Centena--> {}".format(cen))
print("Milhar---> {}".format(mil))