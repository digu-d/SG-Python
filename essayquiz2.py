nome = "Diogo"
palavra = input("Digite uma ou letra: ")

for letra in palavra:
    if letra in nome:
        print(letra, "Esta letra esta no meu nome")
    else:
        print(letra , "Essa letra não está no meu nome")
    
