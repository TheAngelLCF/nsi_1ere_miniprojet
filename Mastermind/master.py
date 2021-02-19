import modele as md
import vue as vu

def main1(nb_props_max, nb_couleurs, longueur) :
    ''' Jeu de mastermind à un seul joueur.
    param nb_props_max : nombre maximal de propositions acceptées
    param nb_couleurs : nombre de couleurs (de valeurs) avec lesquels on joue.
    param longueur : longueur du code secret 
    '''
    print("Le mastermind est un jeu de société qui se joue à deux. Les joueurs disposent de pions colorés (nous considérerons les couleurs violet, jaune, rouge, orange, rose, bleu foncé, bleu clair, vert et le vide). Un joueur choisit un code secret de quatre pions parmi ces couleurs. Le second joueur va essayer de trouver le code. Il a droit à dix essais. À chaque proposition qu'il fait, le premier joueur lui donne deux indications : source Wikipedia")
    fin = 0
    tours_actu = 1
    secret = md.generer_code(longueur, nb_couleurs)
    while tours_actu != nb_props_max + 1:
        rep = vu.lire_proposition(tours_actu, longueur)
        if(rep == secret):
            fin = 1
            break
        bp = md.calculer_bp1(secret, rep)
        mp = md.calculer_mp1(secret, rep, bp)
        vu.afficher_mpandbp(mp, bp)
        tours_actu += 1
        
        
    if(fin):
        vu.afficher_gagnant(tours_actu - 1, secret)
    else:
        vu.afficher_perdant(tours_actu - 1,secret)
    
    
if __name__ == '__main__':
    from doctest import testmod
    testmod()
