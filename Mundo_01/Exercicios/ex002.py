cores = {"azul":"\033[34m",
        "amarelo":"\033[33m",
        "amarelonegrito":"\033[1;33m"}

nome = input(cores["azul"] + 'Digite seu nome: '+ "\033[m")
print(cores["amarelo"] + 'É um prazer te conhecer, {}{}!'.format(cores["amarelonegrito"],nome))