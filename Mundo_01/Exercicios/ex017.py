from math import hypot

co = float(input("Digite o valor do cateto oposto do triângulo: "))
ca = float(input("Digite o valor do cateto adjacente do triângulo: "))
hi = hypot(co, ca)
print("O valor do cateto opostos é {:.1f} do cateto adjacente é {:.1f} e sua hipotenusa é {:.1f}".format(co, ca, hi).replace('.', ','))
