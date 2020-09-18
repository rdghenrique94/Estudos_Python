def main():
    cod = {}
    cod['123'] = ['sabão, 2.50']
    cod['132'] = ['feijão, 4.00']
    cod['213'] = ['arroz, 3.00']
    cod['231'] = ['macarrão, 2.75']
    cod['321'] = ['carne, 30.00']
    cod['312'] = ['frango, 15.00']
    print('ANTES DAS REMOÇÕES')
    print(cod)
    
    print('REMOVENDO CHAVE')

    cod.pop('123')
    print(cod)
    cod.pop('213')
    print(cod)

    print('REMOVENDO VALOR')
    cod['132'].pop()
    print(cod)
    cod['321'].pop()
    print(cod)


main()