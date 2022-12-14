#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA
#E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
#ATÉ 9 ANOS: MIRIM
#ATÉ 14 ANOS: INFANTIL
#ATÉ 19 ANOS: JUNIOR
#ATÉ 20 ANOS: SÊNIOR
#ACIMA: MASTER

from time import sleep
from datetime import date

cores = {"amarelo":"\033[0;33m",
        "amarelonegrito":"\033[1;33m",
        "cyan":"\033[0;34m",
        "cyannegrito":"\033[1;34m",
        "reset":"\033[0;0m"
        }

nasc = int(input(cores["cyan"] + "Digite seu ano de nascimento: " + cores["reset"]))
idade = date.today().year - nasc

if idade < 10 and idade > 1:
    print(cores["cyan"] + "Sua idade é {} anos, categoria: ".format(idade) + cores["cyannegrito"] + "MIRIM" + cores["reset"])
    sleep(4)
elif idade > 9 and idade < 15:
    print(cores["cyan"] + "Sua idade é {} anos, categoria: ".format(idade) + cores["cyannegrito"] + "INFANTIL" + cores["reset"])
    sleep(4)
elif idade > 14 and idade < 20:
    print(cores["cyan"] + "Sua idade é {} anos, categoria: ".format(idade) + cores["cyannegrito"] + "JUNIOR" + cores["reset"])
    sleep(4)
elif idade == 20:
    print(cores["cyan"] + "Sua idade é {} anos, categoria: ".format(idade) + cores["cyannegrito"] + "SÊNIOR" + cores["reset"])
    sleep(4)
elif idade > 20 and idade < 100:
    print(cores["cyan"] + "Sua idade é {} anos, categoria: ".format(idade) + cores["cyannegrito"] + "MASTER" + cores["reset"])
    sleep(4)
elif idade > 99 and idade < 120:
    print(cores["amarelonegrito"] + "{} ANOS, VOCÊ NÃO É TÃO VELHO ASSIM...".format(idade) + cores["amarelo"] + "\nInforme outra data de nascimento..." + cores["reset"])
    sleep(4)
else:
    print(cores["amarelonegrito"] + "DATA INVÁLIDA" + cores["reset"])
    sleep(4)

print(cores["cyan"] + "Saindo..." + cores["reset"])
sleep(5)