import demande as dm

def mothasard(liste_mot):
    from random import randint
    return liste_mot[randint(0, len(liste_mot) - 1)]

def etoilemot(mot):
    """
    >>> etoilemot('hey')
    '***'
    >>> etoilemot('salut')
    '*****'
    >>> etoilemot('coucou')
    '******'
    """
    return '*' * len(mot) #

def testmots(mot_cachee, vrai_mot, lettre):
    """
    >>> testmots('t**t', 'test', 'e')
    'te*t'
    >>> testmots('t**t', 'test', 'v')
    't**t'
    """
    mot_cache = ''
    for k in range(len(vrai_mot)): #mot_cache et vrai_mot on l'a même taille
        if(mot_cachee[k] == '*'):
            if(vrai_mot[k] == lettre):
                mot_cache += lettre
            else:
                mot_cache += '*'
        else:
            mot_cache += mot_cachee[k]
    return mot_cache


def est_dansmot(vrai_mot ,lettre):
    """
    >>> est_dansmot('test', 't')
    2
    >>> est_dansmot('test', 'v')
    0
    """
    count = 0
    for k in range(len(vrai_mot)):
        if(vrai_mot[k] == lettre):
            count += 1
    return count

def utilise(lettres_utilise, lettre):
    for k in range(len(lettres_utilise)):
        if(lettres_utilise[k] == lettre):
            alpha = 0
            while alpha != 1:
                lettre = dm.demande_lettre()
                if(not(utilise(lettres_utilise, lettre))):
                    break
    return False


def total(mot_cachee, vrai_mot):
    """
    >>> total('test', 'test')
    True
    >>> total('te*t', 'test')
    False
    """
    return mot_cachee == vrai_mot



if __name__ == '__main__':
    from doctest import testmod
    testmod()
    
