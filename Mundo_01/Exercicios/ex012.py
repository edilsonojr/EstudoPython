pro = input("Digite a descrição do produto: ")
prc = float(input("Digite o valor do produto: R$ "))
des = prc * 0.05
print("#" * 30)
print("Produto: {}".format(pro))
print("O valor original é R$:{:.2f} e o valor com desconto de 5% é R$:{:.2f}".format(prc,prc - des))
