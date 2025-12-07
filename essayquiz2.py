nome = "Diogo"
palavra = input("Digite uma ou letra: ")

for letra in palavra:
    if letra in nome:
        print(letra, "Voce conseguiu adivinhar uma das letras")
    else:
        print(letra , "Não foi dessa vez, talvez na proxima")
