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

def afficher(code_message):                       # exemples : erreur à afficher dans le terminal : cons_erreur
    '''renvois un message en fonction du code rentré  afficher(str) = str '''     #: erreur à afficher en graphique     : grap_erreur
    if "cons_" in code_message:     #message dans le terminal
        code_message = code_message[5:]
        if code_message == "erreur_lettre_donner": #code pour une erreur syntaxique dans la lettre donné par le user
            print("Erreur dans la lettre donnée !")
            return
        elif code_message == 'notinmot':
            print("La lettre n'est pas dans le mot.") # code pour une lettre donné qui n'est pas dans le mot
            return
        elif code_message == 'inmot':
            print("La lettre était en effet dans le mot à trouver. :)") # code pour une lettre dans le mot
            return
        elif code_message == 'mot_a_trouver':  # affiche le mot à trouvé
            mot_trouver = ''
            for i in trouver:
                mot_trouver += i
            print('Quelle est le mot ? : ', mot_trouver)
            return
        elif code_message == 'vie_reste':   # affiche les vie restantes
            print('Les chance restantes sont au nombre de :',vie)
            return
        elif code_message == 'trouver':     # WIN
            print('Tu as trouvé le mot !')
            print('Le mot est : ', mot,'.')
            print('Il te restais ',vie,' chance.')
            return
        elif code_message == 'not_trouver':    # mot pas trouvé
            print('Tu n\'as pas trouvé le mot. :(')
            return


def lettre_deviner(lettre):
    '''la lettre donnée par l'utilisateur est-elle dans le mot à trouver ? lettre_deviner(str) = bool'''
    lettre = lettre.lower()             #supprime les MAJ
    lettre = supprime_accent(lettre)    #supprime les accents
    if len(lettre) == 1 and lettre not in ['\'','.',',',':',';','\"']: #pas de caractère de ponctuation
        if lettre in mot :      #lettre dans le mot
            for id_mot in range(len(mot)):
                if lettre == mot[id_mot]:
                    trouver[id_mot] = lettre
            if list(mot) == trouver:  # condition de victoire
                
            
            
            return True
        else:                   #lettre pas dans le mot
            vie -= 1
            return False
    else:                                       #cas où la lettre n'est pas une lettre ou est rien du tout ("","je ne suis pas une lettre")
        afficher("cons_erreur_lettre_donner")
        return -1
