import random

def play():

    print("\n\n")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("                Bem-vindo ao jogo da Forca                   ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    frutas = ["banana", "abacate", "cereja", "framboesa", "melancia", "pessego", "laranja", "maca"]
    paises = ["alemanha", "brasil", "espanha", "portugal", "china", "india", "estados unidos", 
              "russia", "chile", "argentina", "venezuela", "paraguai"]
    carros = ["sandero", "prisma", "onix", "gol", "opala", "duster", "hb20", "civic"]

    opcao_valida = False
    enforcou = False
    acertou = False
    erros = 0

    while (not opcao_valida):
        print("(1) Frutas")
        print("(2) Paises")
        print("(3) Carros")
        tema = int(input())

        if (tema == 1):
            numero_aleatorio = random.randrange(0, len(frutas))
            palavra_secreta = frutas[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        elif (tema == 2):
            numero_aleatorio = random.randrange(0, len(paises))
            palavra_secreta = paises[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        elif (tema == 3):
            numero_aleatorio = random.randrange(0, len(carros))
            palavra_secreta = carros[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        else:
            print("Opção inválida: Escolha entre as opções disponíveis!")
            opcao_valida = False

    print(letras_acertadas)
    print("A palavra tem", len(letras_acertadas), "letras\n")

    while (not acertou and not enforcou):
        chute = input("\nQual a letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros += 1
            # TODO funcao desenhar forca
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if (acertou):
        mensagem_ganhou()
    else:
        mensagem_perdeu(palavra_secreta)

def mensagem_ganhou():
    print("\n")
    print(" Parabens, você ganhou! ")
    print("                        ")
    print("     _____________      ")
    print("   '._==_==_==_==_.'    ")
    print("   .-\\:         /-.    ")
    print("  | (|:.        |) |    ")
    print("   ._|:.        |-'     ")
    print("     \\::.      /       ")
    print("      '::.    .'        ")
    print("         )   (          ")
    print("       _.'   '._        ")
    print("     '___________'      ")
    print("                        ")
    print("\n")

def mensagem_perdeu(palavra_secreta):
    print("\n")
    print(" Voce foi enforcado! ")
    print(" A palavra era {}".format(palavra_secreta))

if (__name__ == "__main__"):
    play()
    