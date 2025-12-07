jogos = ["Deepwoken" , "Fortnite" , "Elden Ring" , "ApexLegends"]

favorito = "Deepwoken"
odeio = "ApexLegends"

for jogo in jogos:
    if jogo == favorito:
        print(jogo, "Parabens Voce descobriu meu jogo favorito")
    elif jogo == odeio:
        print(jogo, "Essa não, voce descobriu o jogo que odeio")
    else:
        print(jogo,  "Esse jogo e legal porém não e meu favorito")
        
