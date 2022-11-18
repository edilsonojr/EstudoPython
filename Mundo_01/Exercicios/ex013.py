sal = float(input('Digite seu salário: '))
aj = sal * 0.15

print('#' * 20)
print('Seu salário atual é R$:{:.2f} e o seu novo salário com ajuste de 15% será de R$:{:.2f}'.format(sal, sal + aj).replace('.', ','))
