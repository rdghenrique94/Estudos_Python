#RODRIGO HENRIQUE SOARES DE OLIVEIRA ANDRADE
#TED DICIONARIO



register = {'rodrigo': ['Rodrigo', '88340865',' Rua São Paulo', '250']}
def cadastro():
    op = int(input("QUANTOS CADASTROS DESEJA REALIZAR? "))
    for i in range(0,op):
        cliente = input("Nome: ")
        telefone = int(input("Telefone: "))
        endereço= input("Endereço: ")
        divida = float(input("Dívida: "))
        register[cliente.lower()] = [cliente.lower(), telefone, endereço, divida]
        print('CADASTRO REALIZADO COM SUCESSO')

def delclient():
    for i in register.keys():
        print(i)
    delet = input("QUAL CLIENTE DESEJA REMOVER? :\n")
    register.pop(delet.lower())
    print(register) 

def newvalue():
    for i in register.keys():
        print(i)
    cl = input("ESCOLHA UM CLIENTE:\n")
    novovalor = int(input("DIGITE UM NOVO VALOR:\n"))
    register[cl.lower()][3] = novovalor
    print(register[cl.lower()])
            

def main():
    print("AGENDA DE DIVIDAS BODEGA DA DONA CHICA")
    
    opc = 1

    while opc != 5:
        print('''DIGITE O NUMERO DA OPÇÃO QUE DESEJA SELECIONAR
        1 - Cadastrar Clientes
        2 - Atualizar Valores da Dívida
        3 - Remover Cliente
        4 - Buscar Cliente
        5 - Sair''')

        opc = int(input("\nOpção: "))

        if opc == 1:
            cadastro()
        if opc ==2:
            newvalue()
        if opc == 3:
            delclient()
        if opc == 4:
            client = input("\nDIGITE O NOME DO CLIENTE\n")
            for i in register.keys():
                if(i == client.lower()):
                    print(register[i])


main()