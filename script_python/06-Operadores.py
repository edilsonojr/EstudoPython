#O comando {:#^20} preenche de cerquilha 20 espaços
#nome = input('Digite seu nome: ')
#print('Prazer te conhecer {:#^20}'.format(nome))

#Exemplo sem variável para armazenar o resultado
#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite outro número: '))
#print('A soma dos valores é {}'.format(n1+n2))

#o comando end='' emenda dois prints

n1 = int(input('Digite um valoer: '))
n2 = int(input('Digite outro valor: '))
ad = n1 + n2
su = n1 - n2
mu = n1 * n2
dv = n1 / n2
di = n1 // n2 #Divisão inteira
po = n1 ** n2 #Potência
print('A soma é {}, a subtração é {}, a multiplicação é {} e a divisão é {:.3f}'.format(ad,su,mu,dv), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di,po))
