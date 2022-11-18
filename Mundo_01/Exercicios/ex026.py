#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: ")).strip()
conta = frase.upper().count("A")
print("A seguinta quantidade de A foi encontrada: {}".format(conta))
ini = frase.upper().index("A")
print("A primeira letra A foi encontrada na posição {}".format(ini+1))
ini = frase.upper().rindex("A")
print("A última letra A foi encotnrada na posição {}".format(ini+1))