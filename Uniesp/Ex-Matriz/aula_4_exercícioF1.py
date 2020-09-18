def main():

    cadastro = []

    for i in range(0,3):
        linha = []
        for j in range(0,1):
            nome = input("nome: ")
            matricula = input("matricula: ")
            datan = input("data de nascimento: ")
            linha.append(nome)
            linha.append(matricula)
            linha.append(datan)
    print(cadastro)

main()