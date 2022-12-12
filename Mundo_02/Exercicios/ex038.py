#ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
#O PRIMEIRO VALOR É MAIOR
#O SEGUNDO VALOR É O MAIOR
#NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
from time import sleep

cores = {"cyan":"\033[0;33m","cyannegrito":"\033[1;33m",
        "verde":"\033[0;32m","verdenegrito":"\033[1;32m",
        "reset":"\033[0;0m"}

num1 = int(input(cores["cyan"] + "Digite um número inteiro: " + cores["reset"]))
num2 = int(input(cores["cyan"] + "Digite outro número inteiro: " + cores["reset"]))
print(cores["verdenegrito"] + "Primeiro valor digitado {}, Segundo valor digitado {}.".format(num1,num2))
if num1 > num2:
    print("O PRIMEIRO VALOR É MAIOR!")
elif num2 > num1:
    print("O SEGUNDO VALOR É O MAIOR!")
else:
    print("NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS!")
print("ENCERRANDO...")
sleep(5)