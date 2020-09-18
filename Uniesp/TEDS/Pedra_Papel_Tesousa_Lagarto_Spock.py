############## The Lizard-Spock Expansion #################
####################    TED 04   #######################

print("\nBEM VINDO AO PEDRA-PAPEL-TESOURA-LAGARTO-SPOCK\n")

def main():
    t = int(input("Digite a quantidade de Casos:"))
    if t < 100:
        for i in range(t):
            i += 1
            opt = input("""Digite as opções de Sheldon e Raj separadas por 1 espaço em branco  EX: PEDRA SPOCK.
Opções: >pedra 
        >papel
        >tesoura
        >lagarto 
        >spock 
        =""" )
            bazinga = {'papel pedra', 'tesoura papel', 'papel pedra', 'pedra lagarto', 'lagarto spock', 'spock tesoura',
                       'tesoura lagarto', 'lagarto papel', 'papel spock', 'spock pedra', 'pedra tesoura'}
            trap = {'pedra papel', 'papel tesoura', 'pedra papel', 'lagarto rocha', 'spock lagarto', 'tesoura spock',
                    'lagarto tesoura', 'papel lagarto', 'spock papel', 'pedra spock', 'tesoura pedra'}
            same = {'papel papel', 'pedra pedra', 'tesoura tesoura', 'lagarto lagarto', 'spock spock'}
            if opt in bazinga:
                print("Caso #{}: Bazinga!".format(i))
            elif opt in trap:
                print("Caso #{}: Raj trapaceou!".format(i))
            elif opt in same:
                print("Caso #{}: De novo!".format(i))
            else:
                print("Caso #{}: Opção inválida, tente novamente.".format(i))
    else:
        return main()


main()

#CODIGO ABAIXO INCOMPLETO ESTAVA TENTANDO INCREMENTAR POREM NÃO ESTÁ FUNCIONANDO CORRETAMENTE
"""def plays():
    shel, ra = input("Digite a Jogada do Sheldon: ") .split()
    #ra = input("Digite a Jogada do Raj: ")
    return shel, ra

def rules(sheldon, raj, cont, jog):
    cont += 1
    v = 1
    if sheldon == 'tesoura' and raj == 'papel':
        v = sheldon
    if sheldon == 'papel' and raj == 'pedra':
        v = sheldon
    if sheldon == 'pedra' and raj == 'lagarto':
        v = sheldon
    if sheldon == 'lagarto' and raj == 'Spock':
        v = sheldon
    if sheldon == 'Spock' and raj == 'tesoura':
        v = sheldon
    if sheldon == 'tesoura' and raj == 'lagarto':
        v = sheldon
    if sheldon == 'lagarto' and raj == 'papel':
        v = sheldon
    if sheldon == 'papel' and raj == 'Spock':
        v = sheldon
    if sheldon == 'Spock' and raj == 'pedra':
        v = sheldon
    if sheldon == 'pedra' and raj == 'tesoura':
        v = sheldon
    if v == sheldon:
        if jog == 'she':
            print('Caso #{}: Bazinga!'.format(cont))
        if jog == 'raj':
            print('Caso #{}: Raj trapaceou!'.format(cont))
    return v

def main():
    t = int(input("quantidade de casos"))
    cont = 1
    for i in range(t):
        sheldon, raj = plays()
        v = rules(sheldon, raj, cont, 'shed')
        if v != 1:
            cont += 1
            continue

        v = rules(raj, sheldon, cont, 'raj')
        if v != 1:
            cont += 1
            continue

        if v == 1:
            print('Caso #{}: De novo!'.format(cont))
        cont += 1
        
main()"""
