def main():
    matriz = []
    matriz1 = []
    matrizTransposta = []


    nlinha = int(input("NÚMERO DE LINHAS DA MATRIZ(máx. 10): "))
    while nlinha < 1 or nlinha > 10:
        print("Valor incorreto...!")
        nlinha = int(input("Digite novamente o número de LINHAS da matriz(máx. 10): "))

    ncolunas = int(input("\nNÚMERO DE COLUNAS DA MATRIZ(máx. 10): "))
    while ncolunas < 1 or ncolunas > 10:
        print("Valor incorreto...!")
        ncolunas = int(input("Digite novamente o número de COLUNAS da matriz(máx. 10): "))

    print()


    for linha in range(nlinha):
        for coluna in range(ncolunas):
            valor = int(input(f"Digite o {coluna+1}° valor da {linha+1}° linha: "))
            matriz1.append(valor)
        matriz.append(matriz1)
        matriz1 = []



    print(f"\nMatriz Criada\n")
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(f"[{matriz[linha][coluna]}]", end = '')
        print()


    for coluna in range(ncolunas):
        for valor in range(nlinha):
            matriz1.append(matriz[valor][coluna])
        matrizTransposta.append(matriz1)
        matriz1 = []


    print(f"\nMatriz Transposta\n")
    for linha in range(len(matrizTransposta)):
        for coluna in range(len(matrizTransposta[linha])):
            print(f"[{matrizTransposta[linha][coluna]}]", end = '')
        print()


main()
