#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂGULO
r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print("As retas formam um triângulo!")
else:
    print("As retas não formam um triângulo!")