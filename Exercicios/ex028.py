#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE "0" E" 5 E PEÇA
#PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR

#O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.
'''
from random import choice

n = int(input("Digite um número entre 0 e 5: "))
lista = [0,1,2,3,4,5]
selecionado = choice(lista)
if n == selecionado:
    print("Você venceu!!! O número que você digitou foi {} e número selecionado pelo computador foi {}".format(n, selecionado))
else:
    print("O computador venceu! O número que você digitou foi {} e o selecionado pelo computador foi {}".format(n, selecionado))
'''
### OUTRA FORMA DE RESOLVER ###
from random import randint
from time import sleep

RED = "\033[1;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[1;34m"
PYNK = "\033[0;35m"
CYAN = "\033[1;36m"

BOLD = "\033[;1m"
RESET = "\033[0;0m"

computador = randint(0, 5) #gera um número inteiro aleatório entre 0 e 5
print(YELLOW + "-=-" * 20 + RESET)
print(BLUE + "Vou pensar em um número entre 0 e 5, tente advinhar..." + RESET)
print(YELLOW + "-=-" * 20 + RESET)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(4)
if jogador == computador:
    print(GREEN + "PARABÉNS! Você conseguiu me vencer" + RESET)
else:
    print(GREEN + "GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador) + RESET)