def main():
    colors1 = ["Preto","Açafrão","Amarelo","Azul","Branco","Bronze","Chocolate","Ciano","Cinza"]
    colors2 = ["Dourado",",Marrom","Mostarda","Vermelho","Prata","Púrpura","Rosa""Roxo","Verde"]

    colors = colors1 + colors2
    pos = colors.index("Vermelho")
    print("Essas são as cores completas")
    print(colors)
    print("=" * 200)
    colors.remove("Vermelho")
    print("Todas as cores sem a cor Vermelha")
    print(colors)
    print("=" * 200)
    print("A cor vermelha estava na posição {}, entre Mostarda e Prata".format(pos))

main()

