sal = float(input('Digite seu salário: '))
aj = sal * 0.15

print('##############################')
print('Seu salário é R$:{:.3f}, o seu novo salário com ajuste de 15% é R$:{:.3f}'.format(sal, sal + aj).replace('.', ','))
