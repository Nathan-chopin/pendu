# fichier fonction du TP pendu
# Nathan Chopin
# 30/09/24
# TODO : tout

from random import randint

def creation_liste(nom_fichier):
    '''permet la lecteur d'un fichier txt'''
    fichier = open(nom_fichier,"r")
    liste = []
    for ligne in fichier.readlines():
        liste.append(ligne.lower())     #ajoute les mot du fichier à la liste sans les MAJ
    fichier.close()
    return liste

#source de la liste de mots : http://www.idees-gages.com/mots-jeu-pendu.php#google_vignette
liste_mots = creation_liste('liste_de_mot.txt')


def supprime_accent(ligne):
    """ supprime les accents du texte source """
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    i = 0
    while i < len(accent):
        ligne = ligne.replace(accent[i], sans_accent[i])
        i += 1
    return ligne

mot = liste_mots[randint(0 , len(liste_mots) - 1)] #choisi un mort aléatoire dans la liste
mot = supprime_accent(mot)

trouver = ["_"] * len(mot)
vie = 8



def est_dans_mot(lettre):
    '''la lettre donnée par l'utilisateur est-elle dans le mot à trouver ? lettre_deviner(str) = bool'''
    lettre = lettre.lower()             #supprime les MAJ
    lettre = supprime_accent(lettre)    #supprime les accents
    
    if len(lettre) == 1 and lettre not in ['\'','.',',',':',';','\"']: #pas de caractère de ponctuation
        if lettre in mot :      #lettre dans le mot
            trouver = modif_trouver(trouver,lettre)
            if list(mot) == trouver:  # condition de victoire
                return 1
            return True
        else:                   #lettre pas dans le mot
            vie -= 1
            return False
    else:                                       #cas où la lettre n'est pas une lettre ou est rien du tout ("","je ne suis pas une lettre")
        afficher("cons_erreur_lettre_donner")
        return -1

def modif_trouver(trouver,lettre):
    '''remplace des _ par la lettre trouvé à l'emplacement correspondant'''
    for id_mot in range(len(mot)):
        if lettre == mot[id_mot]:
            trouver[id_mot] = lettre
    return trouver
