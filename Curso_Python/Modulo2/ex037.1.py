def main():
    nu = str(input("Numero"))
    ba = str(input("Base"))

    if nu == "2":
        print(int(nu,2))
    elif nu == "8":
        print(int(nu, 8))
    elif nu == "16":
        print(int(nu , 16))

main()