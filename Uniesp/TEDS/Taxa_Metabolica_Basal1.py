def formula(peso, grupo):
    categorias = [129, 78, 70, 49, 10]

    for index, k in enumerate(categorias):
        sub = grupo -1
        if index == sub:
            tmb = (peso ** 0.75) * k
            return tmb

def main():
    print("="*40)
    print("CALCULO DA TAXA METABOLICA BASAL")
    print("=" * 40)
    peso = float(input("Quanto pesa o animal?: "))
    print("=" * 40)
    print("""DENTRE AS OPÇÕES SELECIONE O GRUPO AO QUAL O ANIMAL PERTENCE
     [1] PASSERIFORMES
     [2] NÃO PASSERIFORMES
     [3] MAMÍFEROS PLACENTARIOS
     [4] MARSUPIAIS E EDENTATAS
     [5] REPTEIS""")
    categ = float(input("Qual grupo pertence o animal?: "))
    print("=" * 40)

    tmb = formula(peso, categ)

    print("{:.2f} é a Taxa Metabólica Basal do animal".format(tmb))

main()