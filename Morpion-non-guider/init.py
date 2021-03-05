def init_morpion():
    return [['_' for _ in range(3)] for _ in range(3)]

def change(morpion, x_o, pos1, pos2):
    ligne = len(morpion)
    colonne = len(morpion[0])
    morpion_change = []
    temps = []
    for k in range(ligne):
        for i in range(colonne):
            if(k == pos1) and (i == pos2):
                temps.append(x_o)
            else:
                temps.append(morpion[k][i])
        morpion_change.append(temps)
        temps = []
    return morpion_change

def verif_ligne(matrice):
    for k in range(len(matrice)):
        if(matrice[k][0] == 'X') and (matrice[k][1] == 'X') and (matrice[k][2] == 'X'):
            return True
        elif(matrice[k][0] == 'O') and (matrice[k][1] == 'O') and (matrice[k][2] == 'O'):
            return True
        else:
            return False
        
def verif_colonne(matrice):
    for k in range(len(matrice)):
        if(matrice[0][k] == 'X') and (matrice[1][k] == 'X') and (matrice[2][k] == 'X'):
            return True
        elif(matrice[0][k] == 'O') and (matrice[1][k] == 'O') and (matrice[2][k] == 'O'):
            return True
        else:
            return False
        
