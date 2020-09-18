def main():
    dici = {}
    #dici = {'58301520' :'rua são paulo', '58301580':'rua pará'}
    print(dici)

    for i in range(1):
        keys = input("Digite o Cep:")
        values = input('Endereços:')
        dici[keys] = values

        print(keys)

    '''for i in dici.keys():
        print(i)'''


main()    