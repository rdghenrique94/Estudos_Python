def main():

    matriz = [[1,2,3,4],
             [5,6,7,8,]]

    for linha in matriz:
        linha.append(int(input("Novo Valor: ")))
        print(matriz)

main()