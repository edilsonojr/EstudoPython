al = float(input('Digite a altura da área: '))
la = float(input('Digite a largura da área: '))
ar = al * la
lt = ar / 2

print('Área total de {:.1f}x{:.1f} é de {:.1f}m² e serão necessários {:.1f}l de tinta.'.format(al, la, ar, lt))
