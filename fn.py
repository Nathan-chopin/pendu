# fichier fonction du TP pendu
# Nathan Chopin
# 30/09/24
# TODO : tout

mots = ["bite"]
mot = mots[0]
trouver = ["_"] * len(mot)


def lettre_deviner(lettre):
    bool_trouver = False
    for id_mot in range(len(mot)):
        if lettre == mot[id_mot]:
            trouver[id_mot] = lettre
            bool_trouver = True
    return bool_trouver


