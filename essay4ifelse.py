chave_secreta = 7
soma_base = 3
dica = chave_secreta + soma_base

print("Bem vindo ao jogo da adivinhação misteriosa")
print("Eu tenho um número secreto. Será que voce consegue descobrir")

palpite = int(input("Digite um número: "))

if palpite == chave_secreta:
    print("Parabens! Voce adivinhou o número secreto")
else:
    if palpite == dica:
        print("Voce não adivinhou o número secreto, mas encontrou a dica escondida")
    else:
        if palpite > chave_secreta:
            print("Passou do número secreto... tente um número menor da próxima vez")
        else:
            print("Ainda não conseguiu... tente um número maior")
