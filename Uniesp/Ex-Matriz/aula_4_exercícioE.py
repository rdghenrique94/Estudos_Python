def main():

    c = int(input('Digite a dimensão c da matriz: '))
    l = int(input('Digite a dimensão l da matriz: '))
    matriz = []
    for i in range(c):
        linha = []
        for j in range(l):
            linha.append(int(input("valores")))
        matriz.append(linha)
    print(matriz)

    cont = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                cont = cont +1
    print("a matriz tem ",cont, "elemento(s) maior(es) do que 10!")
main()