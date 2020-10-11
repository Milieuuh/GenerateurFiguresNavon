
import tkinter
from tkinter import *
import tkinter.font as font

import os
import sys

sys.path.append(os.path.abspath(".")+'\\Metier')

from FiguresNavon import *



#generer les fichiers png
def generer():
    res_LettreGlobale=s_lGlobale.get()
    res_LettreLocale=s_lLocale.get()
    print("appel de FigureNavon : ")

    maFigureNavon=FigureNavon(res_LettreGlobale,res_LettreLocale)
    maFigureNavon.creerFigureNavon()
    


#fenetrePrincipale
maFenetre = tkinter.Tk()
maFenetre.title("générateur de Navon")
maFenetre.geometry("700x800")

#typographie
f=font.Font(family="Verdana",size=15)
f_titre=font.Font(family="Verdana",size=20,weight="bold")

#--------------------------------------------------------------------- TITRE
f_titre= tkinter.Frame(maFenetre, borderwidth=2, relief=GROOVE)
f_titre.pack(side=TOP,padx=1,pady=30)
Label(f_titre,text="------ Générateur de Navon  ------",font=f_titre).pack(padx=10,pady=10)


#--------------------------------------------------------------------- PARAMETRE DES LETTRES
lf_formeLettres= tkinter.LabelFrame(maFenetre, text="Paramètres de la figure de Navon",padx=5,pady=1)
lf_formeLettres.pack(fill="both",padx="10",pady="10",ipady="20",ipadx="10")

    #Label lettre Globale et champs de saisie
s_lGlobale=tkinter.StringVar()
s_lGlobale.set("A")
Label(lf_formeLettres,text="Lettre Globale : ").pack(side=LEFT)
champ_lettreGlobale = tkinter.Entry(lf_formeLettres,textvariable=s_lGlobale, bg="white", width="10")
champ_lettreGlobale.pack(side=LEFT)

    #Label lettre locale et champ de saisie
s_lLocale=tkinter.StringVar()
s_lLocale.set("B")
Label(lf_formeLettres,text="Lettre Locale : ").pack(side=LEFT)
champ_lettreLocale = tkinter.Entry(lf_formeLettres,textvariable=s_lLocale, bg="white", width="10")
champ_lettreLocale.pack(side=LEFT)

    #Taille lettre globale
nb_tailleGX = tkinter.IntVar()
nb_tailleGX.set(800)
Label(lf_formeLettres,text="Taille lettre globale : ").pack(side=LEFT)
champ_tailleGX = tkinter.Entry(lf_formeLettres,textvariable=nb_tailleGX, bg="white", width="10")
champ_tailleGX.pack(side=LEFT)
Label(lf_formeLettres,text=" px").pack(side=LEFT)


    #--------------------------------------------------------------------- BOUTON GENERER
lf_sauvegardeForme= tkinter.LabelFrame(maFenetre, text="Sauvegarder la/les figures de Navon",padx=5,pady=1)
lf_sauvegardeForme.pack(fill="both",padx="10",pady="10",ipady="20",ipadx="10")
    #Bouton générer
bt_Generer = tkinter.Button(lf_sauvegardeForme, relief=RAISED, bg="#32CD32", fg="WHITE",text="Générer",command=generer)
bt_Generer['font']=f
bt_Generer.pack()


    #--------------------------------------------------------------------- GENERATION FENETRE

    #CREATION FENETRE
def lancerAppli():
    maFenetre.mainloop()


