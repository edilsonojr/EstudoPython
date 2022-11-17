#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR
'''
valor = int(input("Digite um número inteiro: "))
result = valor % 2
if result == 0:
    print("O valor digitado é PAR!")
else:
    print("O valor digitado é ÍMPAR!")
'''
### OUTRA FORMA DE RESOLVER ###
numero = int(input("Me diga um número qualquer "))
resultado = numero % 2
if resultado == 0:
    print("O número {} é PAR".format(numero))
else:
    print("O número {} é ÍMPAR".format(numero))