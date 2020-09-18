days = int(input('Quantos dias de Aluguel?: '))
km = float(input('Quantos km Rodados?: '))
pay = (days*60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(pay))