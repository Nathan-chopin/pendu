# fichier incluant des fonction pour le mode graphique
# Nathan Chopin
# 04/10/24
# TODO : tout

from tkinter import Tk , Label , Button, Entry, messagebox


page = Tk()


def affichage_fenetre(bool_mode_console,fenetre):
    if not bool_mode_console:
        fenetre.mainloop()


def affichage_erreur(text):
    messagebox.showwarning(text)

def affichage_info(text):
    messagebox.showinfo(text)


