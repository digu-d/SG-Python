perguntas = ["Capital do Brasil", "9x5", "Cor do Ceu"]
respostas_certas = ["Brasilia", "45", "Azul"]

acertos = 0

for indice in range(3):
        resposta = input(perguntas[indice] + ": ")
        if resposta == respostas_certas[indice]:
                print("Parabens voce acertou qual a capital do Brasil")
                acertos += 1

        elif resposta == "":
                print("Voce não digitou nada")

        else:
            print("Voce errou")

print("Voce acertou",acertos,"de 3 perguntas")
