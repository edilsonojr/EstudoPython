cores = {"cian":"\033[36m",
        "vermelho":"\033[1;31m"}


valor = input(cores["cian"] + 'Digite algo: ')
print('O valor digitado é do tipo: ')
print(cores['vermelho'],type(valor))
print(valor.isalnum())
print(valor.isupper())