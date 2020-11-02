
import tkinter
from tkinter import *
import tkinter.font as font
from tkinter.filedialog import *

import os
import sys

sys.path.append(os.path.abspath(".")+'\\Metier')

from FiguresNavon import *


#fenetrePrincipale
maFenetre = tkinter.Tk()
maFenetre.title("générateur de Navon")
maFenetre.geometry("800x800")

#typographie
f=font.Font(family="Verdana",size=15)
f_titre=font.Font(family="Verdana",size=20,weight="bold")


#apercu les fichiers png
def generer():
    res_LettreGlobale=s_lGlobale.get()
    res_LettreLocale=s_lLocale.get()
    res_hauteur=nb_hauteurGX.get()
    res_densite=nb_densite.get()
    print("appel de FigureNavon:")

    maFigureNavon=FigureNavon(res_LettreGlobale,res_LettreLocale,res_hauteur, res_densite)
    maFigureNavon.creerFigureNavon()
    
#sauvergarder fichier png
def sauvegarde(): 

    filepath = asksaveasfilename(initialdir="/",title="Enregistrer sous",filetypes=[('png files','*.png'),('jpeg files','*.jpg'),('all files','.*')])
    print(filepath) 



#--------------------------------------------------------------------- TITRE
f_titre= tkinter.Frame(maFenetre, borderwidth=2, relief=GROOVE)
f_titre.pack(side=TOP,padx=1,pady=30)
Label(f_titre,text="------ Navon Generator  ------",font=f_titre).pack(padx=10,pady=10)


#--------------------------------------------------------------------- PARAMETRE DES LETTRES
#------------------------------------------------------FORME LETTRES
lf_formeLettres= tkinter.LabelFrame(maFenetre, text="Settings",padx=5,pady=1)
lf_formeLettres.pack(fill="both",padx="10",pady="10",ipady="20",ipadx="10")

f_formeLettres = tkinter.Frame(lf_formeLettres,width=300, height=300,bd=10)

    #Label lettre Globale et champs de saisie
s_lGlobale=tkinter.StringVar()
s_lGlobale.set("A")
Label(f_formeLettres,text="Global Letter : ").pack(side=LEFT)
champ_lettreGlobale = tkinter.Entry(f_formeLettres,textvariable=s_lGlobale, bg="white", width="10")
champ_lettreGlobale.pack(side=LEFT)

    #Label lettre locale et champ de saisie
s_lLocale=tkinter.StringVar()
s_lLocale.set("B")
Label(f_formeLettres,text="Local Letter : ").pack(side=LEFT)
champ_lettreLocale = tkinter.Entry(f_formeLettres,textvariable=s_lLocale, bg="white", width="10")
champ_lettreLocale.pack(side=LEFT)

f_formeLettres.pack()

#------------------------------------------------------HAUTEUR ET LARGEUR

f_tailleLG = tkinter.Frame(lf_formeLettres,width=300, height=300, bd=10)
   
nb_hauteurGX = tkinter.IntVar()
nb_hauteurGX.set(400)
Label(f_tailleLG,text="Size Global Letter : ").pack(side=LEFT)
champ_tailleGX = tkinter.Entry(f_tailleLG,textvariable=nb_hauteurGX, bg="white", width="10")
champ_tailleGX.pack(side=LEFT)
Label(f_tailleLG,text=" px").pack(side=LEFT)

f_tailleLG.pack()

#------------------------------------------------------DENSITE 
f_densite = tkinter.Frame(lf_formeLettres,width=300, height=300, bd=10)

nb_densite = tkinter.DoubleVar()
nb_densite.set(0.5)
Label(f_densite,text="Density : ").pack(side=LEFT)
champ_densite = tkinter.Entry(f_densite,textvariable=nb_densite, bg="white", width="10")
champ_densite.pack(side=LEFT)
Label(f_densite,text=" (Between 0 and 1)").pack(side=LEFT)

f_densite.pack()


#--------------------------------------------------------------------- BOUTON APERCU
f_BOUTON = tkinter.Frame(lf_formeLettres,width=300, height=300, bd=10)

bt_Apercu=tkinter.Button(f_BOUTON, relief=RAISED, bg="#32CD32", fg="WHITE",text="Preview",command=generer)
bt_Apercu['font']=f
bt_Apercu.pack()


f_BOUTON.pack()


#--------------------------------------------------------------------- BOUTON GENERER LE FICHIER
lf_sauvegardeForme= tkinter.LabelFrame(maFenetre, text="Save",padx=5,pady=1)
lf_sauvegardeForme.pack(fill="both",padx="10",pady="10",ipady="20",ipadx="10")



    #Bouton générer
bt_Generer = tkinter.Button(lf_sauvegardeForme, relief=RAISED, bg="#32CD32", fg="WHITE",text="Generate",command=sauvegarde)
bt_Generer['font']=f
bt_Generer.pack()


#--------------------------------------------------------------------- GENERATION FENETRE

    #CREATION FENETRE
def lancerAppli():
    maFenetre.mainloop()


