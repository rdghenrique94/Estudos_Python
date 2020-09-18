import time
def formula(peso, grupo):
    categorias = [129, 78, 70, 49, 10]

    for index, k in enumerate(categorias):
        sub = grupo -1
        if index == sub:
            tmb = (peso ** 0.75) * k
            return tmb

def formula2(peso, grupo):
    categorias = [129, 78, 70, 49, 10]

    for index, k in enumerate(categorias):
        sub = grupo -1
        if index == sub:
            tmb = (peso ** 0.25) * k
            return tmb


def main():
    print("=" * 40)
    print("\33[1;100mCALCULO DA TAXA METABÓLICA BASAL e da TAXA METABÓLICA ESPECÍFICA\33[m")
    print("=" * 40)
    print("\33[1:46mINICIANDO PROGRAMA\33[m")
    time.sleep(2)
    peso = float(input("Quanto pesa o animal?: Kg "))
    print("\033[1;42mPESO RECEBIDO COM SUCESSO\33[m")
    print("=" * 40)
    time.sleep(2)
    print("""\33[1;100mDENTRE AS OPÇÕES SELECIONE O GRUPO AO QUAL O ANIMAL PERTENCE
         [1] PASSERIFORMES
         [2] NÃO PASSERIFORMES
         [3] MAMÍFEROS PLACENTARIOS
         [4] MARSUPIAIS E EDENTATAS
         [5] REPTEIS\33[m""")
    print("=" * 40)
    categ = float(input("Qual grupo pertence o animal?: "))
    print("=" * 40)
    print("\033[1;42mGRUPO DO ANIMAL RECEBIDO COM SUCESSO\33[m")
    print("=" * 40)
    time.sleep(2)
    print("""\33[1;100mDIGITE O COMANDO PARA CALCULAR A TMB OU TME DO ANIMAL
        [b] para TAXA METABÓLICA BASAL
        [e] para TAXA METABÓLICA ESPECÍFICA\33[m""")
    print("=" * 40)

    flag = input("Qual calculo deseja realizar?: ")
    print("=" * 40)
    time.sleep(2)
    print("\033[1;42mINFORMAÇÕES RECEBIDAS...\33[m")
    time.sleep(2)
    print("\033[1;42mPREPARANDO CALCULO\33[m")
    time.sleep(2)
    if flag.lower() == "b" or flag.upper() == "B":
        tmb = formula(peso, categ)
        print("=" * 40)
        print("\33[1;41m{:.2f} é a Taxa Metabólica Basal do animal\33[m".format(tmb))
    elif flag.lower() == "e" or flag.upper() == "E":
        tmb = formula2(peso, categ)
        print("=" * 40)
        print("\33[1;41m{:.2f} é a Taxa Metabólica Específica do animal\33[m".format(tmb))
    else:
        print("\33[1:41mCOMANDOS INVALIDOS TENTE NOVAMENTE\33[m")
        print("=" * 40)
        time.sleep(5)
        print("\33[1;46mREINICIANDO PROGRAMA\33[m")
        return main()


main()