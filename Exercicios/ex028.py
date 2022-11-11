#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE "0" E" 5 E PEÇA
#PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR

#O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.
from random import choice

n = int(input("Digite um número entre 0 e 5: "))
lista = [0,1,2,3,4,5]
selecionado = choice(lista)
#print(type(n))
#print(type(selecionado))
if n == selecionado:
    print("Você venceu!!! O número que você digitou foi {} e número selecionado pelo computador foi {}".format(n, selecionado))
else:
    print("O computador venceu! O número que você digitou foi {} e o selecionado pelo computador foi {}".format(n, selecionado))