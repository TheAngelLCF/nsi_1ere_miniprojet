import init as ini
import affichage as af

def main():
    j1 = input("Veuillez entrer le nom du premier joueur : ")
    j2 = input("Veuillez entrer le nom du second joueur : ")
    fini = 0
    j1_play = True
    j2_play = False
    print(af.init_game())
    while not(fini):
        if(j1_play):
            choix = af.demande(j1)
            
            # A faire
            # verif diagonale 
            # systeme de winner dans affichage
            # systeme de verification si la syntaxe du joueur est bon
            # systeme de verification si le joueur dépasse pas 3 (pour la matrice faire un -1 :))
            
            
            
            j1_play = False
            j2_play = True
        else:
            choix = af.demande(j2)
            
            
            
            
            
            
            j1_play = True
            j2_play = False
            
if __name__ == "__main__":
    main()