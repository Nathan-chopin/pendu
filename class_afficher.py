# fichier de la classe AFFICHER
# Nathan Chopin
# 03/10/24

class AFFICHER():
    def __init__(self) -> None:
        pass
    def console(self):
        def erreur_lettre_donner(self):
            print("Erreur dans la lettre donnée !")
            return






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
        elif code_message == 'victoire':     # WIN
            print('Tu as trouvé le mot !')
            print('Le mot est : ', mot,'.')
            print('Il te restais ',vie,' chance.')
            return
        elif code_message == 'not_trouver':    # mot pas trouvé
            print('Tu n\'as pas trouvé le mot. :(')
            return
