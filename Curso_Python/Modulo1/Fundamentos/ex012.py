price = float(input('Preço do produto: '))
desc = price - (price*5/100)
print('O produto que custava {} com desconto de 5% vai custar {}'.format(price, desc))
