'''def main():
    ano = int(input("Idade: "))

    if ano < 18:
        tempo = 18 - ano
        print("Ele ainda irá se alistar no serviço militar pois faltam {} anos".format(tempo))
    elif ano == 18:
        print("Ele está no periodo de alistamento")
    else:
        tempo = ano-18
        print("Ele passou do prazo de alistamento pois ja se passaram {} anos do prazo".format(tempo))

main()'''

from _datetime import datetime
def main ():
    now = datetime.now()
    print("="*50)
    print("Nós estamos no ano de",now.year)
    print("=" * 50)
    ano = int(input("Em que ano você nasceu? "))
    print("=" * 50)
    idade = now.year - ano
    print("Você está com {} anos".format(idade))

    if idade < 18:
        tempo = 18 - idade
        print("Você ainda irá se alistar no serviço militar pois faltam {} anos".format(tempo))
    elif idade == 18:
        print("Você está no periodo de alistamento")
    else:
        tempo = idade -18
        print("Você passou do prazo de alistamento pois ja se passaram {} anos".format(tempo))

main()