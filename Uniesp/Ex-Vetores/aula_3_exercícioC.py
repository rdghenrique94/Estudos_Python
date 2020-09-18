def main():
    registro = []
    cont = int(input("Digite de forma numerica a quantidade limite de valores a serem inseridos : "))
    registro.append(input("Digite o primeiro valor de forma numerica ou escrita: "))

    for item in registro:
        registro.append(input("Digite os Valores restantes de forma numerica ou escrita: "))

        if len(registro) >= cont:
            print("Esses Foram os Valores inseridos:", registro)
            print("Você chegou ao limite de valores ")
            break


main()