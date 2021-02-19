def est_chiffre(car):
    """
    >>> est_chiffre('2 3 5 1')
    True
    """
    return car <= '9999'

def split_int(car):
    """
    >>> split_int('2 3 5 1')
    [2, 3, 5, 1]
    """
    split_list = []
    for k in range(7):
        if(k % 2 == 0):
            split_list.append(int(car[k]))
    return split_list

def lire_proposition(nb_prop, longueur):
    print("Tour n°" + str(nb_prop))
    rep = input("Votre proposition (4 entiers entre 0 et 8 séparés par des espaces) ? ")
    if(est_chiffre(rep)):
        return split_int(rep)
    else:
        lire_proposition(nb_prop, longueur)
    
def afficher_mpandbp(mp, bp):
    print("Vous avez", bp,"bon(s) nombre(s) de bien placé(s) et", mp, "de mal placé(s)")
    
def afficher_gagnant(nbprop, secret):
    print("Bravo, le code secret était", secret, ", vous l'avez résolu en", nbprop, "tour(s)")
    
def afficher_perdant(nbprop,secret):
    print("Malheuresement, vous n'avez pas trouvé le code en", nbprop, " tours, le code était", secret)
    

if __name__ == '__main__':
    from doctest import testmod
    testmod()