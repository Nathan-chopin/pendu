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


def mot_a_trouver():
    mot = liste_mots[randint(0 , len(liste_mots) - 1)] #choisi un mort aléatoire dans la liste
    mot = supprime_accent(mot) 
    return (mot , ["_"] * (len(mot)-1) )


def est_dans_mot(lettre,trouver,mot):
    '''la lettre donnée par l'utilisateur est-elle dans le mot à trouver ? lettre_deviner(str) = bool'''
    
    def modif_trouver(liste_trouver,lettre,mot):
        '''remplace des _ par la lettre trouvé à l'emplacement correspondant'''
        for id_mot in range(len(mot)):
            if lettre == mot[id_mot]:
                liste_trouver[id_mot] = lettre
        return  liste_trouver

    lettre = lettre.lower().rstrip()            #supprime les MAJ
    lettre = supprime_accent(lettre)    #supprime les accents
    if len(lettre) == 1 and lettre not in ['\'','.',',',':',';','\"',1,-1,'1','-1']: #pas de caractère de ponctuation
        if lettre in mot :      #lettre dans le mot
            trouver = modif_trouver(trouver, lettre, mot)
            if list(mot) == trouver:  # condition de victoire
                return 42
            return True
        else:                   #lettre pas dans le mot
            return False
    else:                                       #cas où la lettre n'est pas une lettre ou est rien du tout ("","je ne suis pas une lettre")
        return -1



def liste_to_str(liste):
    str = ''
    for i in liste:
        str += i
    return str

def affichage(bool_mode_console,text):
    if bool_mode_console:
        print(text)
    else:
        return

def affichage_victoire( bool_mode_console , str_mot , int_vie ):
    affichage(bool_mode_console,'Tu as trouvé le mot !')
    affichage(bool_mode_console,'Le mot est : ' + str_mot)
    affichage(bool_mode_console,'Il te restait ' + str(int_vie) + ' chances.')

def affichage_mot_trouver( bool_mode_console , liste_trouver):
    str_trouver = liste_to_str(liste_trouver)
    affichage(bool_mode_console,'Le mot est : ' + str_trouver)

def affichage_vie( bool_mode_console , int_vie):
    affichage(bool_mode_console,'Les chance restantes sont au nombre de :'+ str(int_vie))