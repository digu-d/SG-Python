vida_paladino = 10
vida_monstro = 10
cura_disponivel = 1
raio_disponivel = 1

for _ in range(4):
    acao = input("Ação (espada/cura/raio): ")

    if acao == "espada":
        vida_monstro -=3
    elif acao == "cura" and cura_disponivel:
        vida_paladino +=6
        cura_disponivel=0
    elif acao == "raio" and cura_disponivel:
        vida_monstro -=6
        raio_disponivel=0
    

        if vida_monstro <=0:
            print("Voce venceu")
            break


        print("O monstro atacou")
        vida_paladino -=5
        
        if vida_paladino <=0:
            print("Voce perdeu")
            break

print("Vida Paladino: ",vida_paladino,vida_monstro,"Vida monstro: ")
