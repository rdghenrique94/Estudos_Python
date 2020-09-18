def main():
    registro = []
    i = 5
    for item in range(0,5):
        registro.append(input("Digite os nomes que deseja adicionar: "))
    print("=" * 50)
    print(registro)
    print("=" * 50)
    if i == len(registro):
        registro.append(input("Adicione outro nome no final: "))
    print("=" * 50)
    print(registro)
    print("=" * 50)
    if i < len(registro):
        registro.insert(1, input("Adicione outro nome após o primeiro"))
    print("=" * 50)
    print(registro)
    print("=" * 50)


main()