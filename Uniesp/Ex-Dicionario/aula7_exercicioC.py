def main():
    cod = {}

    for i in range(3):
        key = input("Chave: ")
        valor = input("valor: ")
        cod[key]=valor
        print(cod)

    if '12345' in cod.keys():
        print('CEP OK')
        print(key)
    else:
        print("CEP doesnt found")
    
    for i in cod.values():
        if 'rua 1' in i:
            print("RUA OK")
            print(valor)
        else:
            ('rua doenst found')

main()    