#FATIAMENTO

frase1 =      'aprenda python'
frase = 'teste de fatiamento'
print('{}'.format(frase[:10]))
print('{}'.format(frase[3:10]))
print('{}'.format(frase[1:10:2]))
print('{}'.format(frase[::2]))
print('''PRINTAR TEXTO GRANDE''')                                                       #3 ASPAS PARA PRINTAR ALGO GRANDE
#ANALISE

print('A frase tem :{} caracteres'.format(len(frase)))                                  #quantidade de Caracteres
print('A quantidade do mesmo caractere: {}'.format(frase.count('e')))                   #quantidade de um mesmo caractere
print('Quantidade de um caractere fatiado: {}'.format(frase.count('e', 0, 13)))         #quantidade de um mesmo caractere com fatiamento
print('Qual posição o caractere está: {}'.format(frase.find('est')))                    #procurar a posição do caractere
print("Posição da palavra na string: {}".format(frase.find('Android')))                 #valor negativo quando não é encontrado o caractere
print("O caractere é True or False: {}".format('curso' in frase))                       #dizer se o valor é true or false

#TRANSFORMAÇÃO

print('MAIUSCULA',frase.upper())                                                        #transformar tudo em maiusculo
print('MINUSCULA',frase.lower())                                                        #transformar tudo em minusculo
print(frase.capitalize())                                                               #transforma tudo pra minusculo e o primeiro caractere em maiusculo
print(frase.title())                                                                    #analisar quantas palavras existem na string
print(frase1.strip())                                                                   #remover caracteres (espaços)inuteis
print(frase1.rstrip())                                                                  #remove os ultimos espaços da string (direita)
print(frase1.lstrip())                                                                  #remove os primeiros espaços (esquerda)
frase = frase.replace('fatiamento', 'transformação')                                    #subistituir uma string por outra
print(frase)

#DIVISÃO
dividido = frase.split()                                                                #gera uma lista com todas as cadeias de caracteres
print(dividido[0])                                                                      #pode-se imprimir apenas uma palavra da lista
print(dividido[0][3])                                                                   #pode-se imprimir apenas uma letra da palavra selecionada da lista

#JUNÇÃO

print('-'.join(frase))