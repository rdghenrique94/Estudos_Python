import time

def Area(t):
	t = int(input('Digite a Area em Metros Quadrados: '))
	Area = t / 3
	if t % 54 == 0:
		l = t / 54
	else:
		l = int(t / 54) + 1
	#Calcualo do preço
	p = l * 80
	print('Será necessario: %d Latas' %l)
	print('O valor a ser pago é de R$: %.2f' %p)

Area(0)
time.sleep(3.0)