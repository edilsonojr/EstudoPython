n = int(input("Digite um número inteiro: "))
msg = "TABUADA"
print('{:#^20}'.format(msg))
i = 0
while i < 11:
    print('{} x {} = {}'.format(n, i, n * i))
    i = i + 1
