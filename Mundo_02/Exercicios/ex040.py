#FAÇA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA
#MÉDIA ABAIXO DE 5.0: REPROVADO
#MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
#MÉDIA 7.0 OU SUPERIOR: APROVADO
from time import sleep

cores = {"cyan":"\033[0;36m",
        "verdenegrito":"\033[1;32m",
        "magentanegrito":"\033[1;31m",
        "amarelonegrito":"\033[1;33m",
        "reset":"\033[0;0m"
        }

n1 = float(input(cores["cyan"] + "Digite a primeira nota: " + cores["reset"]))
n2 = float(input(cores["cyan"] + "Digite a segunda nota: " + cores["reset"]))
media = (n1 + n2) / 2
if media < 5:
    print(cores["magentanegrito"] + "REPROVADO!" + cores["reset"])
    sleep(4)
elif media >= 5.0 and media < 7.0:
    print(cores["amarelonegrito"] + "RECUPERAÇÃO!" + cores["reset"])
    sleep(4)
elif media >= 7.0:
    print(cores["verdenegrito"] + "APROVADO!" + cores["reset"])
    sleep(4)
else:
    print("Opção inválida!...")
    sleep(4)

print(cores["cyan"] + "Sua média foi {:.2f}\nSaindo...".format(media) + cores["reset"])
sleep(5)
