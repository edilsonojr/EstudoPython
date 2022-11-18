#Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin, tan, radians

an = float(input("Digite o angulo que deseja: "))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))

print("O ângulo de {:.1f}° tem SENO de {:.2f}°".format(an, se))
print("O ângulo de {:.1f}° tem COSSENO de {:.2f}".format(an, co))
print("O ângulo de {:.1f}° tem TANGENTE de {:.2f}".format(an, ta))
