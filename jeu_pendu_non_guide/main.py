import preinit as pi
import demande as dm

def pendu(liste_tmot, tours):
    lettres_utilises = []
    vrai_mot = pi.mothasard(liste_tmot)
    mot_cachee = pi.etoilemot(vrai_mot)
    print("Le mot est : " + mot_cachee + ", à toi de le retrouver avant la fin des tours")
    for tour_actu in range(1, tours + 1):
        print(dm.tours(tour_actu, tours))
        lettre = dm.demande_lettre()
        util = pi.utilise(lettres_utilises, lettre)
        if(not(util)):
            lettres_utilises.append(lettre)
            content = pi.est_dansmot(vrai_mot ,lettre)
            if(content):
                mot_cachee = pi.testmots(mot_cachee, vrai_mot, lettre)
                print(dm.nbr_fois(lettre, content, mot_cachee))
                if(pi.total(mot_cachee, vrai_mot)):
                    break
            else:
                print(dm.pas_contenu(lettre, mot_cachee))
    if(pi.total(mot_cachee, vrai_mot)):
        print(dm.bravo(vrai_mot, tour_actu))
    else:
        print(dm.predu(vrai_mot, tours))
            
            
            
            