def affich_morpion(morpion):
    for k in range(len(morpion)):
        for i in range(len(morpion[0])):
            print(morpion[k][i], end=" ")
        print("")
        
def init_game():
    temps = "Voici la façon de jouer, veuillez choisir des coordonnées, par exemple (1 1) sans les parenthéses mais bien l'espace, si vous choissiez cela, alors cela sera pris en compte \nPar exemple \n X _ _ \n _ _ _ \n _ _ _"
    return temps

def selected(j1, j2):
    temps = "Le joueur " + str(j1) + " utilisera X et le joueur " + str(j2) + " utilisera O"
    return temps

def demande(joueur):
    temps = input(joueur +", veuillez choisir des coordonnées : ")
    return temps