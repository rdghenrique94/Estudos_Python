def main():
    registro = []
    i = 5
    for item in range(0,5):
        registro.append(input("Digite os nomes que deseja adicionar: "))
    print("=" * 50)
    print(registro)
    print("=" * 50)
    if i == len(registro):
        pos = registro.index("Rodrigo")
        registro[pos] = "Henrique"
    print(registro)


main()