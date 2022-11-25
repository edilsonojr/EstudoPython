#ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA,
#O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO
cores = {"vermelho":"\033[0;31m,", "vermelhonegrito":"\033[1;31m",
        "verde":"\033[0;32m", "verdenegrito":"\033[1;32m",
        "azul":"\033[0;34m", "azulnegrito":"\033[1;34m",}

vcasa = float(input(cores["azul"] + "Informe o valor da casa, R$: " + "\033[m"))
sal = float(input(cores["azul"] + "Informe o seu salário, R$: " + "\033[m"))
qtdmeses = int(input(cores["azul"] + "Informe a quantidade de anos que deseja pagar o imóvel: " + "\033[m")) * 12

condparc = sal * 25 / 100
prest = vcasa / qtdmeses
if condparc >= prest:
    print(cores["verdenegrito"] + "EMPRÉSTIMO APROVADO!\nINFORMAÇÕES DO EMPRÉSTIMO" + "\033[m")
    print("Quantidade Parcelas: {}\nValor das Parcelas R$ {:.3f}".format(qtdmeses, prest))
else:
    print(cores["vermelhonegrito"] + "EMPRÉSTIMO NÃO APROVADO!" + "\033[m")
    print("O valor mínimo da parcela baseada no seu salário é R$ {:.3f}, o valor da parcela mínima calculada foi de R$ {:.3f}".format(condparc,prest))

