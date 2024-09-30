# fichier fonction du TP pendu
# Nathan Chopin
# 30/09/24
# TODO : tout

mots = ["bite"]
mot = mots[0]
trouver = ["_"] * len(mot)
vie = 8


def lettre_deviner(lettre):
    bool_trouver = False
    if len(lettre) == 1:
        for id_mot in range(len(mot)):
            if lettre == mot[id_mot]:
                trouver[id_mot] = lettre
                bool_trouver = True
    else:
        print("erreur dans la lettre donner")
        vie += 1
    return bool_trouver

def afficher_mot(liste):
    phrase = ""
    for i in liste:
        phrase += i
    return phrase
