def main():
    id = int(input("Digite sua Idade"))

    if id > 0 and id <= 9:
        print("O atleta se encaixa na categoria Mirim")
    elif id >9 and id <=14:
        print("O atleta se encaixa na categoria Infantil")
    elif id > 14 and id <= 19:
        print("O atleta se encaixa na categoria Junior")
    elif id == 20:
        print("O atleta se encaixa na categoria Sênior")
    elif id > 20:
        print("O atleta se encaixa na categoria Master")

main()