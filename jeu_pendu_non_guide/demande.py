def demande_lettre():
    rep = input("Quelle lettre choissiez-vous ? : ")
    return rep

def lettre_dejafait(lettre):
    """
    >>> lettre_dejafait('d')
    'Désolé, mais vous avez déjà mis la lettre d'
    """
    dejafait = "Désolé, mais vous avez déjà mis la lettre " + lettre
    return dejafait
    
def tours(tours_actu, nbr_tours):
    """
    >>> tours(5, 10)
    'Tour n° : 5 sur 10'
    >>> tours(10, 10)
    'Tour n° : 10 sur 10'
    """
    tour = "Tour n° : " + str(tours_actu) + " sur " + str(nbr_tours)
    return tour

def bravo(vrai_mot, nbr_tours):
    """
    >>> bravo('test', 5)
    'Bravo ! Vous avez trouvez le mot : test en 5 tour(s).'
    >>> bravo('hey', 7)
    'Bravo ! Vous avez trouvez le mot : hey en 7 tour(s).'
    """
    gg = 'Bravo ! Vous avez trouvez le mot : ' + vrai_mot + ' en ' + str(nbr_tours) + ' tour(s).'
    return gg
    
def perdu(vrai_mot, max_tours):
    """
    >>> perdu('test', 10)
    'Perdu, le mot était test, vous avez dépassé la limite de tour(s) de 10'
    >>> perdu('hey', 7)
    'Perdu, le mot était hey, vous avez dépassé la limite de tour(s) de 7'
    """
    lose = 'Perdu, le mot était ' + vrai_mot + ', vous avez dépassé la limite de tour(s) de ' + str(max_tours)
    return lose

def nbr_fois(lettre, nb_fois, mot_cachee):
    """
    >>> nbr_fois('d', 2, 'd*d*')
    'La lettre d est compris 2 ==> donc : d*d*'
    >>> nbr_fois('a', 2, 'dada')
    'La lettre a est compris 2 ==> donc : dada'
    """
    fois = 'La lettre ' + lettre + ' est compris ' + str(nb_fois) + ' ==> donc : ' + mot_cachee
    return fois

def pas_contenu(lettre, mot_cachee):
    """
    >>> pas_contenu('t', 'dada')
    "La lettre t n'est pas contenu dans le mot ==> donc : dada"
    >>> pas_contenu('v', 'test')
    "La lettre v n'est pas contenu dans le mot ==> donc : test"
    """
    temps = 'La lettre ' + lettre + ' n\'est pas contenu dans le mot ==> donc : '  + mot_cachee
    return temps

if __name__ == '__main__':
    from doctest import testmod
    testmod()