#Aluno: Rodrigo Henrique Soares de Oliveira Andrade
#TED LISTA ENCADEADA

from ted_listenc1 import Cidades

def changeCity(city, new):
    cont = 0
    while city:
        cont +=1
        if cont == 2:
            city.setFcity(new)
        city = city.getLcity()

def imprimir(city):
    while city:
        print(city.getFcity())
        city = city.getLcity()

def main():

    cid1 = Cidades()
    cid2 = Cidades()
    cid3 = Cidades()
    cid4 = Cidades()

    cid1.setFcity("Santa Rita")
    cid2.setFcity("Campina")
    cid3.setFcity("Cajazeiras")
    cid4.setFcity("Bayeux")

    cid1.setLcity(cid2)
    cid2.setLcity(cid3)
    cid3.setLcity(cid4)
    cid4.setLcity(None)

    imprimir(cid1)
    print("="*50)
    print("Adicione uma Cidade no Lugar de Campina")
    print("="*50)
    addcity = str(input("Digite o nome da Cidade que deseja Adicionar:\n"))

    changeCity(cid1, addcity)
    imprimir(cid1)


main()