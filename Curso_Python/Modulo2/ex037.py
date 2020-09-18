def main():
    num = int(input("Digite um numero: "))
    print("""Escolha uma das Bases para Convesão
    [2] Converter para Binario
    [8] Converter para Octal
    [16] Converter para Hexadecimal""")
    opc = int(input("Sua opção: "))

    if opc == 2:
        print("{} convertido para Binario é igual a {} ".format(num, bin(num)[2:]))
    elif opc == 8:
        print("{} convertido para Octal é igual a {} ".format(num, oct(num)[2:]))
    elif opc == 16:
        print("{} convertido para Hexadecimal é igual a {} ".format(num, hex(num)[2:]))
    else:
        print("Opção invalida digite novamente")
        return main()

main()
