from random import shuffle #shuffle tem a função de "embaralhar"

p1 = str(input("Digite o nome do primeiro aluno: "))
p2 = str(input("Digite o nome do segundo aluno: "))
p3 = str(input("Digite o nome do terceiro aluno: "))
p4 = str(input("Digite o nome do quarto aluno: "))
lista = [p1, p2, p3, p4]
shuffle(lista)
print("A ordem de apresentação será: {}".format(lista))