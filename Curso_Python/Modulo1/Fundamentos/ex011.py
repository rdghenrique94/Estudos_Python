base = int(input('Qual a largura da parede?: '))
altu = int(input('Qual a altura da parede?: '))
area = base * altu
litros = area /3
priceLitros = 80.0
capLitros = 18
latas = litros / capLitros
total = latas * priceLitros
print('A Parede tem {}m² '.format(area))
print('A quantidade de tinta a ser usada será  {:.2f}L. e o Valor será {:.2f}R$.'.format(latas, total))





'''base = float(input('Qual o tamanho da base ? '))
altura = float(input('Qual o Tamanho da Altura? '))
area = base * altura
litrosUsados = area/3

if litrosUsados == int( litrosUsados ):
    custo = litrosUsados * 80
else:
    custo = (int(litrosUsados)+1) * 80



print("Custará R$", float("{0:.2f}".format(custo)), " reais")
'''

'''tamanho = float(input('Tamanho em metros quadrados: '))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else:
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('%d latas' %latas)
print ('R$ %.2f' %preco)
'''