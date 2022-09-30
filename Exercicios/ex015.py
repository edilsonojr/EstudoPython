km = float(input("Informe a quantidade de km rodados: "))
dia = float(input("Informe quantos dias o carro ficou alugado: "))
tkm = km * 0.15
tdia = dia * 60.00
print("{:-^35}".format("RESUMO"))
print("Percorrido {}km ----> R${:.2f}".format(km, tkm))
print("Dias alugado {:.0f} -------> R${:.2f}".format(dia, tdia))
print("-" * 35)
print("TOTAL ---> R${:.2f}".format(tkm + tdia))
print("-" * 35)
