#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR
'''
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

#VERIFICACAO MAIOR VALOR
if n1 > n2 and n1 > n3:
    print("O primeiro valor digitado é o maior -> {:.2f}".format(n1))
elif n2 > n1 and n2 > n3:
    print("O segundo valor digitado é o maior -> {:.2f}".format(n2))
else:
    print("O terceiro valor digita é o maior -> {:.2f}".format(n3))

#VERIFICACAO MENOR VALOR
if n1 < n2 and n1 < n3:
    print("O primeiro valor digitado é o menor -> {:.2f}".format(n1))
elif n2 < n1 and n2 < n3:
    print("O segundo valor digitado é o menor -> {:.2f}".format(n2))
else:
    print("O terceiro valor digitado é o menor -> {:.2f}".format(n3))
'''
### OUTRA FORMA DE RESOLVER ###
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))