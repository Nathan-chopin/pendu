# main du TP pendu
# Nathan Chopin
# 04/10/24
# TODO : intégration tkinter

import fn_pendu as fn



vie = 8
le_mot , mot_incomplet = fn.mot_a_trouver()
mode_console = False



while(vie != 0):
    fn.affichage_mot_incomplet(mode_console , mot_incomplet) #affiche le mot incomplet
    lettre = input("Devine une lettre, si tu penses avoir trouvé le mot tape 'mot deviner'(en cas d'érreur 2 vie seront perdues !) \n Tape ici : ")
    
    if lettre == 'mot deviner': # cas où le joueur pense avoir trouvé le mot
        lettre = input("Quel est le mot ? :")
        if lettre == le_mot: #s'il a bon
            fn.affichage_victoire(mode_console,le_mot,vie)
            break
        else:           #s'il n'a pas bon
            vie -= 2            
            fn.affichage(mode_console,'Tu n\'as pas trouvé le mot. :(')
    
    elif lettre == ' cheatcodedev':          #cheat code pour moi
        print('mode_console',mode_console)
        print('le mot',le_mot)
        print('mot incomplet',mot_incomplet)
        print('list to str (mot incomplet)',fn.liste_to_str(mot_incomplet))
    
    elif lettre == ' exit': #cheat code pour moi
        break
    
    else :
        if fn.est_dans_mot(lettre,mot_incomplet,le_mot) == -1: #erreur dans se qu'a taper le joueur
            fn.affichage(mode_console,"Erreur dans la lettre donnée !")
    
        elif fn.liste_to_str(mot_incomplet) == le_mot :    #mot trouvé
            fn.affichage_victoire(mode_console,le_mot,vie)
            break

        elif fn.est_dans_mot(lettre,mot_incomplet,le_mot):  # lettre dans le mot
            fn.affichage(mode_console,"La lettre était en effet dans le mot à trouver. :)")
            if fn.liste_to_str(mot_incomplet) == le_mot:
                fn.affichage_victoire(mode_console,le_mot,vie)
                break
        
        else:                       #lettre pas dans le mot
            vie -= 1
            fn.affichage(mode_console,"La lettre n'est pas dans le mot.")
        
    fn.affichage_vie(mode_console,vie) #affiche les vies restentes
    fn.affichage(mode_console,"\n")

    if vie == 0:    #game over
        fn.affichage_game_over(mode_console,le_mot)

