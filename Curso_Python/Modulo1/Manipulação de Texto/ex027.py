def main():
    name = str(input("digite seu nome completo:")).strip()
    n = name.split()
    print('Analisando o nome', n)
    print("O primeiro nome é {}".format(n[0]))
    print("o ultimo nome é {}".format(n[len(n)-1]))

main()