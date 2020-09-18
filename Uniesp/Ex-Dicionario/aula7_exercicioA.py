def main():
    dici = {}
    print(dici)

    for i in range(6):
        chaves = input('Nome das pessoas: ')
        datadenasc = input('Data de nascimento: ')
        address = input("Endereço: ")
        dici[chaves] = datadenasc,address
        print(dici)

main()