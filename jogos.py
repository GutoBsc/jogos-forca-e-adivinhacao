import forca
import adivinhacao

def escolhe__jogo():
    print("*****************************")
    print("*****Escolha o seu jogo!*****")
    print("*****************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe__jogo()