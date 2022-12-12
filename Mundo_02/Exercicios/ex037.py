#ESCREVA UM PROGRAMA QUE LEAI UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO
# 01 - BINÁRIO, 02 - OCTAL, 03 - HEXADECIMAL
from time import sleep

cores = {"branco":"\033[0;37m", "branconegrito":"\033[1;37m",
        "verde":"\033[0;32m", "verdenegrito":"\033[1;32m",
        "amarelo":"\033[0;33m", "amarelonegrito":"\033[1;33m",
        "magenta":"\033[0;35m", "magentanegrito":"\033[1;35m",
        "cyan":"\033[0;36m", "cyannegrito":"\033[1;36m",
        "vermelho":"\033[0;31m", "vermelhonegrito":"\033[1;31m",
        "reset":"\033[0;0m"}

print("{:-^40}".format(" CONVERSOR UNIDADE "))
valor = int(input("Digite um número inteiro: "))
print("DIGITE A OPÇÃO DA BASE QUE DESEJA CONVERTER")
opc = int(input(("01 - BINÁRIO\n02 - OCTAL\n03 - HEXADECIMAL\n")))
if opc == 1 :
    print("Base BINÁRIA selecionada!\nCONVERTENDO...")
    sleep(4)
    print(cores["amarelonegrito"] + "O número {} convertido para base Binária é {}".format(valor, bin(valor).replace("0b","")) + cores["reset"])
elif opc == 2:
    print("Base OCTAL selecionada!\nCONVERTENDO...")
    sleep(4)
    print(cores["verdenegrito"] + "O número {} convertido para a base Octal é {}".format(valor, oct(valor).replace("0o", "")) + cores["reset"])
elif opc == 3:
    print("Base HEXADECIMAL selecionada!\nCONVERTENDO...")
    sleep(4)
    print(cores["cyannegrito"] + "O número {} convertido para a base Hexadecimal é {}".format(valor,hex(valor).replace("0x", "")) + cores["reset"])
else:
    print(cores["vermelhonegrito"] + "Opção INVÁLIDA!" + "\033[m")
    sleep(4)
print(cores["branconegrito"] + "ENCERRANDO..." + cores["reset"])
sleep(4)