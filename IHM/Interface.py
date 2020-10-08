
import tkinter
from tkinter import *
import aider
import aPropos



#generer les fichiers png
def generer():
    res_LettreGlobale=lettreGlobale.get()
    res_LettreLocale=lettreLocale.get()
    print("generer à faire : ")
        


  
#fenetrePrincipale
maFenetre = tkinter.Tk()

maFenetre.title("générateur de Navon")
maFenetre.geometry("700x800")

#--------------------------------------------------------------------- TITRE
f_titre= tkinter.Frame(maFenetre, borderwidth=2, relief=GROOVE)
f_titre.pack(side=TOP,padx=1,pady=30)
Label(f_titre,text="------ Générateur de Navon  ------").pack(padx=10,pady=10)


#--------------------------------------------------------------------- PARAMETRE DES LETTRES
lf_formeLettres= tkinter.LabelFrame(maFenetre, text="Paramètres de la figure de Navon",padx=5,pady=1)
lf_formeLettres.pack(fill="both",expand="yes")

#Label lettre Globale et champs de saisie
s_lGlobale=tkinter.StringVar()
s_lGlobale.set("A")
Label(lf_formeLettres,text="Lettre Globale : ").pack()
champ_lettreGlobale = tkinter.Entry(lf_formeLettres,textvariable=s_lGlobale, bg="white", width="10")
champ_lettreGlobale.pack()

#Label lettre locale et champ de saisie
s_lLocale=tkinter.StringVar()
s_lLocale.set("B")
Label(lf_formeLettres,text="Lettre Locale : ").pack()
champ_lettreLocale = tkinter.Entry(lf_formeLettres,textvariable=s_lLocale, bg="white", width="10")
champ_lettreLocale.pack()

#Taille lettre globale
nb_tailleGX = tkinter.IntVar()
nb_tailleGX.set(800)
Label(lf_formeLettres,text="Taille lettre globale : ").pack()
champ_tailleGX = tkinter.Entry(lf_formeLettres,textvariable=nb_tailleGX, bg="white", width="10")
champ_tailleGX.pack()


#--------------------------------------------------------------------- BOUTON GENERER
lf_sauvegardeForme= tkinter.LabelFrame(maFenetre, text="Sauvegarder la/les figures de Navon",padx=5,pady=1)
lf_sauvegardeForme.pack(fill="both",expand="yes")
#Bouton générer
bt_Generer = tkinter.Button(lf_sauvegardeForme,text="Générer",command=generer)
bt_Generer.pack()


#--------------------------------------------------------------------- GENERATION FENETRE

#CREATION FENETRE
maFenetre.mainloop()


