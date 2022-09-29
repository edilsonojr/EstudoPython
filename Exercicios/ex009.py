n = int(input("Digite um número para ver sua tabuada: "))
print("-" * 12)
i = 0
while i < 11:
    print('{} x {:2} = {}'.format(n, i, n * i))
    i = i + 1
print("-" * 12)
