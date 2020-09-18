def main():
    nome = str(input("Leia seu nome Completo: ")).strip()
    #name = 'Rodrigo Henrique Soares de Oliveira Andrade'
    print('Analisando seu nome...')
    print('Maiusculo', nome.upper())
    print('Minusculo', nome.lower())
    print('O Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
    div = nome.split()
    print('Seu primeiro nome é {} e tem ao todo {} letras'.format(div[0], len(div[0])))
    print('Seu primeiro nome tem {} letras'. format(nome.find(' ')))



main()