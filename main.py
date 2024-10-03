# main du TP pendu
# Nathan Chopin
# 30/09/24
# TODO : tout

import fn_pendu as fn

#from class_afficher import AFFICHER

vie = 8
le_mot , mot_devine = fn.mot_a_trouver()
mode_console = True



while(vie != 0):
    fn.affichage_mot_trouver(mode_console , mot_devine)
    lettre = input("Devine une lettre, si tu penses avoir trouvé le mot tape 'mot deviner'(en cas d'érreur 2 vie seront perdues !) \n Tape ici : ")
    if lettre == 'mot deviner':
        lettre = input("Quelle est le mot ? :")
        if lettre == le_mot:
            fn.affichage_victoire(mode_console,le_mot,vie)
            break
        else:
            vie -= 2            
            fn.affichage(mode_console,'Tu n\'as pas trouvé le mot. :(')
    if fn.est_dans_mot(lettre,mot_devine,le_mot) == -1:
        fn.affichage(mode_console,"Erreur dans la lettre donnée !")
    
    elif fn.est_dans_mot(lettre,mot_devine) == 42:    
        fn.affichage_victoire(mode_console,le_mot,vie)
        break

    elif fn.est_dans_mot(lettre,mot_devine):
        fn.affichage(mode_console,"La lettre était en effet dans le mot à trouver. :)")
        
    else:
        vie -= 1
        fn.affichage(mode_console,"La lettre n'est pas dans le mot.")
        
    fn.affichage_vie(mode_console,vie)

