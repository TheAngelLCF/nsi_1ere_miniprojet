def demande_lettre():
    rep = input("Quelle lettre choissiez-vous ? : ")
    return rep

def lettre_dejafait(lettre):
    dejafait = "Désolé, mais vous avez déjà mis la lettre " + lettre 
    
def tours(tours_actu, nbr_tours):
    tour = "Tour n° : " + str(tours_actu) + " sur " + str(nbr_tours)
    return tour

def bravo(vrai_mot, nbr_tours):
    gg = 'Bravo ! Vous avez trouvez le mot : ' + vrai_mot + ' en ' + str(nbr_tours) + ' tour(s).'
    return gg
    
def predu(vrai_mot, max_tours):
    lose = 'Perdu, le mot était ' + vrai_mot + ', vous avez dépassé la limite de tour(s) de ' + str(max_tours)
    return lose

def nbr_fois(lettre, nb_fois, mot_cachee):
    fois = 'La lettre ' + lettre + ' est compris ' + str(nb_fois) + ' ==> donc : ' + mot_cachee
    return fois

def pas_contenu(lettre, mot_cachee):
    temps = 'La lettre ' + lettre + ' n\'est pas contenu dans le mot ==> donc : '  + mot_cachee
    return temps