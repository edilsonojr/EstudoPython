#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO
'''
ano = float(input("Digite o ano que deseja verificar se é bissexto: "))
vano = ano % 4
if vano == 0.0:
    print("O ano digitado é bissexto!")
else:
    print("O ano digitado não é bissexto!")
'''
### OUTRA FORMA DE RESOLVER ###
from datetime import date

ano = int(input("Que ano quer analisar? Digite 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO!".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO!".format(ano))