def affich_morpion(morpion):
    for k in range(len(morpion)):
        for i in range(len(morpion[0])):
            print(morpion[k][i], end=" ")
        print("")