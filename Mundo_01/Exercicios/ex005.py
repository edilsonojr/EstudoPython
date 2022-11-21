cores = {"preto":"\033[1;35m",
        "vermelho":"\033[1;31m"}

n = int(input(cores["preto"] + 'Digite um número inteiro: '))
print(cores["vermelho"] + 'O número digitado é {}, seu antecessor é {} e seu sucessor é {}'.format(n, n-1, n+1))
