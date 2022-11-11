#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO
ano = float(input("Digite o ano que deseja verificar se é bissexto: "))
vano = ano % 4
if vano == 0.0:
    print("O ano digitado é bissexto!")
else:
    print("O ano digitado não é bissexto!")