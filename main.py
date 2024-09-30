# main du TP pendu
# Nathan Chopin
# 30/09/24
# TODO : tout

import fn_pendu as fn

vie = fn.vie

while(vie != 0):
    fn.afficher_mot(fn.trouver)
    lettre = input("devine une lettre : ")
    fn.lettre_deviner(lettre)
    print(fn.trouver)
