#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO
#SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE
from math import floor
vel = float(input("Digite a sua velocidade: "))
if floor(vel) > 80.00:
    print("Você foi multado, estava dirigindo à {:.0f}Km/h. Ultrapassou em {:.0f}Km/h do permitido, ".format(vel,vel-80), end='')
    print("o valor da multa é R$:{:.2f}".format((vel - 80.00)*7).replace('.', ','))
else:
    print("Velocidade dentro do limite da via")