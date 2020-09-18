def main():
    info = []
    infor = {}
    
    for i in range(3):
        infor['names'] = input("Digite os NOMES: ")
        infor['address'] = input('Digite os ENDEREÇOS')
        infor['CPF'] = input('Digite o CPF: ')

        info.append(infor.copy())

        print(info)

main()