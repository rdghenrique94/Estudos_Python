n1 = int(input('numero1: '))
n2 = bool(input('numero2: '))
s = n1 + n2
print('a soma entre {} e {} vale {}'.format(n1, n2, s))

read = input('Digite algo: ')
print(type (read))
print('{} é do tipo alfanumerico?'.format(read), read.isalnum())
print('{} é do tipo numerico?'.format(read), read.isnumeric())
print('{} é do tipo alfabetico?'.format(read), read.isalpha())
print('{} é do tipo maiusculo?'.format(read), read.isupper())


