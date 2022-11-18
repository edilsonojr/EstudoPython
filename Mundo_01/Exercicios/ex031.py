#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM
#CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS
'''
from math import floor
km = float(input("Digite a distância da viagem: "))
vcurta = 0.50
vlonga = 0.45
if floor(km) > 200.00:
    print("O valor da passagem é R$ {:.2f} ".format(km*vlonga).replace('.', ','))
else:
    print("O valor da passagem é R$ {:.2f} ".format(km*vcurta).replace('.', ','))
'''
### OUTRA FORMA DE RESOLVER ###
distancia = float(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(preco))