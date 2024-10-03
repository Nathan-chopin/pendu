# main du TP pendu
# Nathan Chopin
# 30/09/24
# TODO : tout

import fn_pendu as fn

vie = fn.vie

while(vie != 0):
    fn.afficher('cons_mot_a_trouver')
    lettre = input("Devine une lettre, si tu penses avoir trouvé le mot tape 'mot deviner'(en cas d'érreur 2 vie seront perdu !) \n Tape ici : ")
    if lettre == 'mot deviner':
        lettre = input("Quelle est le mot ? :")
        if lettre == fn.mot:
            fn.afficher("cons_trouver")
            break
        else:
            vie -= 2
            fn.afficher("cons_not_trouver")
    if fn.lettre_deviner(lettre) == -1:
        fn.afficher("cons_erreur_lettre_donner")
    elif fn.lettre_deviner(lettre):
        fn.afficher("cons_inmot")
    else:
        fn.afficher("cons_notinmot")

