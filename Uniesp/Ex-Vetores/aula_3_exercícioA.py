def mult(lista):
    for item in lista:
        print(item * 4)

def main():
    list = [0, 1, 2, 3, 4]
    print("Confira os resultados dos valores {} abaixo multiplicado por 4 sequencialmente".format(list))
    mult(list)


main()