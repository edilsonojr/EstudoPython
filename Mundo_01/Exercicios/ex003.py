#este código contém erro de sintaxe na operação
#é realizado uma concatenação e não uma soma

# n1 = input('Digite um número: ')
# n2 = input('Digite mais um número: ')
# s = n1 + n2
# print('A soma vale: ', s)
cores = {"verde":"\033[32m",
        "verdenegrito":"\033[1;32m"}

#Aqui é realizado uma conversão do tipo para inteiro
n1 = int(input(cores["verde"] + 'Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}{}'.format(n1, n2,cores["verdenegrito"] ,s))