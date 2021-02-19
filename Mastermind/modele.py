from random import randint

def generer_code(max_nbr, max_gen):
    code = []
    for _ in range(max_nbr):
        code.append(randint(0, max_gen - 1))
    return code

def generer_code2(max_nbr, max_gen):
    return [randint(0, max_gen - 1)for _ in range(max_nbr)]

def calculer_bp1(liste_sys, liste_user):
    """
    >>> calculer_bp1([1,2,2,4],[2,1,2,4])
    2
    >>> calculer_bp1([1,2,2,4],[3,1,3,4])
    1
    """
    assert(len(liste_sys) == len(liste_user)), "Taille incorrect"
    taille = len(liste_sys)
    good_nbr = 0
    for k in range(taille):
        if(liste_sys[k] == liste_user[k]):
            good_nbr += 1
    return good_nbr

def distribution(propo, max_val):
    """
    >>> distribution([1,2,2,4],9)
    [0, 1, 2, 0, 1, 0, 0, 0, 0]
    >>> distribution([3,1,3,4],9)
    [0, 1, 0, 2, 1, 0, 0, 0, 0]
    >>> distribution([8,8,6,8],9)
    [0, 0, 0, 0, 0, 0, 1, 0, 3]

    """
    liste_distrib = []
    init_distrib = 0
    for val in range(max_val):
        for k in range(len(propo)):
            if(val == propo[k]):
                init_distrib += 1
        liste_distrib.append(init_distrib)
        init_distrib = 0
    return liste_distrib
    
    
def calculer_mp1(code, propo, good_place):
    """
    >>> calculer_mp1([1,2,2,4],[2,1,2,4],2)
    2
    >>> calculer_mp1([1,2,2,4],[2,1,3,4],1)
    2
    >>> calculer_mp1([4,3,2,2],[2,2,1,5],0)
    2
    >>> calculer_mp1([1,2,3,4],[4,3,2,1],0)
    4
    >>> calculer_mp1([1,2,3,4],[4,3,3,1],1)
    2
    """
    code_distrib = distribution(code, 9)
    propo_distrib = distribution(propo, 9)
    alpha = 0
    for k in range(9):
        alpha += min(code_distrib[k], propo_distrib[k])
    return alpha - good_place

def reponses(code, propo):
    """
    >>> reponses([1,2,2,4],[2,1,2,4])
    [2, 2]
    >>> reponses([1,2,2,4],[3,1,3,4])
    [1, 1]
    """
    bp = calculer_bp1(code, propo)
    mp = calculer_mp1(code, propo, bp)
    return [bp, mp]
    
    
    

if __name__ == '__main__':
    from doctest import testmod
    testmod()