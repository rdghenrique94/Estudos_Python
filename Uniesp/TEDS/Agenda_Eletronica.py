import sys

friends = ["Ramon","Nayla","Nathalia","Hilma"]
birthday = ["19/09","08/05","29/12","05/03"]

def exibir():

    print("SEUS CONTATOS")
    for i in range(len(friends)):
        print(f"ID {i}\nNome: {friends[i]} | Aniversário: {birthday[i]}\n")
    input("Pressione enter no seu teclado para continuar")


def adicionar():
    print("ADICIONAR NOVO CONTATO")
    nome = str(input("Digite o nome do novo contato: ")).strip().capitalize()
    aniversario = str(input("Digite a data de aniversário do contato (dd/mm): ")).strip()

    friends.append(nome)
    birthday.append(aniversario)

    print("Contato adicionado!")
    input("Pressione enter no seu teclado para continuar...")


def remover():
    print("REMOVER CONTATO")

    for i in range(len(friends)):
        print(f"ID {i}\nNome: {friends[i]} | Aniversário: {birthday[i]}\n")

    position = int(input("Digite o ID do contato que deseja remover: "))
    while position > len(friends)-1 or position < 0:
        position = int(input("O ID não existe, digite novamente: "))

    #friends.remove(position)
    #birthday.remove(position)
    # print("O Contato {} foi removido!".format(friends[position]))

    del(friends[position])
    del(birthday[position])

    print("O Contato foi removido!")
    input("Pressione enter no seu teclado para continuar...")


def main():
    print('''AGENDA ELETRÔNICA ONLINE
        O que deseja fazer?
    [1] Exibir todos os contatos
    [2] Adicionar um contato
    [3] Remover um contato
    [4] Sair''')
    choice = int(input("- "))

    while choice < 1 or choice > 4:
        print("Opção inválida, tente novamente.")
        choice = int(input("- "))

    print("\n")
    if choice == 1:
        exibir()
    elif choice == 2:
        adicionar()
    elif choice == 3:
        remover()
    else:
        sys.exit()

    print("\n" * 5)
    main()


main()
