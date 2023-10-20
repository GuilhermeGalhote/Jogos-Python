import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nivel: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5        

    for rodadas in range(1, tentativas +1):
        print("Tentativa {} de {}".format(rodadas,tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute <1 or chute >100):
            print("Digite um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute < numero_secreto
        menor   = chute > numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:

            if (maior):
                print("O numero secreto é maior")

            elif (menor):
                print("O numero secreto é menor")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos        

    print("Fim do jogo")
