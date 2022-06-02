#este código contém erro de sintaxe na operação
#é realizado uma concatenação e não uma soma

# n1 = input('Digite um número: ')
# n2 = input('Digite mais um número: ')
# s = n1 + n2
# print('A soma vale: ', s)


#Aqui é realizado uma conversão do tipo para inteiro
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))