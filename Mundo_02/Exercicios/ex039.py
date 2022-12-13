#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
#SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
#SE É A HORA DE SE ALISTAR
#SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
#O PROGRAMA DEVERÁ MOSTRAR O TEMPO QUE FALTOU OU QUE PASSOU DO PRAZO.
from datetime import date
from time import sleep

cores = {"cyan":"\033[0;34m","cyannegrito":"\033[1;34m",
        "amarelo":"\033[0;33m","amarelonegrito":"\033[1;33m",
        "magenta":"\033[0;31m","magentanegrito":"\033[1;31m",
        "verde":"\033[0;32","verdenegrito":"\033[1;32m",
        "reset":"\033[0;0m"
        }

nasc = int(input(cores["cyan"] + "Digite o ano que você nasceu: " + cores["reset"]))
idade = date.today().year - nasc
if nasc < 1901:
    print(cores["amarelonegrito"] + "VOCÊ NÃO É TÃO VELHO(A) ASSIM, DIGITE UM ANO VÁLIDO. EX.: 2004" + cores["reset"])
elif nasc >= date.today().year:
    print(cores["amarelonegrito"] + "NÃO É PERMITIDO DIGITAR ANO SUPERIOR OU IGUAL AO ATUAL..." + cores["reset"])
elif idade == 18:
    print(cores["verdenegrito"] + "É A HORA DE SE ALISTAR!!!" + cores["reset"])
elif idade < 18:
    print(cores["amarelonegrito"] + "AINDA NÃO É TEMPO DE SE ALISTAR!" + cores["reset"])
    sleep(4)
    if (18 - idade) == 1:
        print(cores["amarelo"] + "Necessário aguardar {} ano".format(18 - idade) + cores["reset"])
    else:
        print(cores["amarelo"] + "Necessário aguardar {} anos".format(18 - idade) + cores["reset"])
elif idade > 18 and idade < 45:
    print(cores["magentanegrito"] + "JÁ PASSOU DO TEMPO DE ALISTAMENTO" + cores["reset"])
    sleep(4)
    if (idade - 18) == 1:
        print(cores["magenta"] + "Já passou {} ano do tempo de se alistar...".format(idade - 18) + cores["reset"])
    else:
        print(cores["magenta"] + "Já se passaram {} anos do tempo de se alistar...".format(idade - 18) + cores["reset"])
else:
    print(cores["magentanegrito"] + "IDADE SUPERIOR A 45 ANOS, NÃO É POSSÍVEL MAIS SE ALISTAR..." + cores["reset"])
print("\033[1;37m" + "Encerrando...")
sleep(5)