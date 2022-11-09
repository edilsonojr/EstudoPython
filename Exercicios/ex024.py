#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input("Digite o nome da cidade: ")).strip()#strip remove espaço antes e depois
cidade = cidade.upper().split()[0]
#print(cidade)
verificador = 'SANTO' in cidade #variável verificador receberá um valor boleano
if verificador == True:
    print("A cidade começa com SANTO")
else:
    print("A cidade não começa com SANTO e sim com {}".format(cidade))

### OUTRA FORMA DE RESOLVER ###
#cid = str(input("Em que cidade você nasceu? ")).strip()
#print(cid[:5].upper() == "SANTO")