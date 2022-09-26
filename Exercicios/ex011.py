import math

al = float(input('Digite a altura da área: '))
la = math.ceil(float(input('Digite a largura da área: ')))
ar = al * la
lt = ar / 2

print('Área total é de {:.2f} metros e serão necessário {:.0f}l de tinta.'.format(ar, lt))
