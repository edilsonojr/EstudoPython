#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DE SEU AUMENTO
#PARA SALÁRIOS SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%
#PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%
'''
sal = float(input("Digite o seu salário: "))
if sal >1250.00:
    print("Salário antigo R$ {:.2f}, novo salário com 10% de reajuste R$ {:.2f}".format(sal, sal + ((sal*10)/100)).replace(".", ","))
else:
    print("Salário antigo R$ {:.2f}, novo salário com 15% de reajuste R$ {:.2f}".format(sal, sal + ((sal * 15)/100)).replace(".", ","))
'''
### OUTRA FORMA DE RESOLVER ###
salario = float(input("Qual é o salário do funcionário? R$ "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("Quem ganhava R$:{:.2f} passa a ganhar R$:{:.2f} agora".format(salario,novo))