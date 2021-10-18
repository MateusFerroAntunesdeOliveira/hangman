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
        print("\nEscolha um tema para o jogo!")
        print("(1) Frutas")
        print("(2) Paises")
        print("(3) Carros")
        print("Digite uma das opções: ")
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
        chute = input("Qual a letra que você quer: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print("\n")
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
    print("   .-\:          /-.    ")
    print("  | (|:.         |) |   ")
    print("   ._|:.         |_.    ")
    print("     \::.       /       ")
    print("      '::.    .'        ")
    print("        )    (          ")
    print("      _.'    '._        ")
    print("     '__________'       ")
    print("                        ")

def mensagem_perdeu(palavra_secreta):
    print("Voce foi enforcado! ")
    print("A palavra era {}".format(palavra_secreta))
    print("\n")

def desenha_forca(erros):
    print("  ________      ")
    print(" |/       |     ")
    
    if (erros == 1):
        print(" |      ('_')   ")
        print(" |              ")
        print(" |              ")
        print(" |              ")

    if (erros == 2):
        print(" |      ('_')   ")
        print(" |        |     ")
        print(" |              ")
        print(" |              ")

    if (erros == 3):
        print(" |      ('_')   ")
        print(" |        |     ")
        print(" |        |     ")
        print(" |              ")

    if (erros == 4):
        print(" |      ('_')   ")
        print(" |       \|     ")
        print(" |        |     ")
        print(" |              ")

    if (erros == 5):
        print(" |      ('_')   ")
        print(" |       \|/    ")
        print(" |        |     ")
        print(" |              ")

    if (erros == 6):
        print(" |      ('_')   ")
        print(" |       \|/    ")
        print(" |        |     ")
        print(" |       /      ")

    if (erros == 7):
        print(" |      ('_')   ")
        print(" |       \|/    ")
        print(" |        |     ")
        print(" |       / \    ")
    
    print(" |              ")
    print("_|___           ")

if (__name__ == "__main__"):
    play()
    