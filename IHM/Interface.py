
import tkinter
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

Titre = tkinter.StringVar()
l_lettreGlobale = tkinter.Label(maFenetre, textvariable=Titre)
Titre.set("------ Générateur de Navon  ------")
l_lettreGlobale.grid(row=0,column=10,padx=0,pady=0)


#--------------------------------------------------------------------- FORME DES LETTRES
   
#Label lettre Globale et champs de saisie
Text = tkinter.StringVar()
l_lettreGlobale = tkinter.Label(maFenetre, textvariable=Text)
Text.set("Lettre Globale : ")
l_lettreGlobale.grid(row=1,column=1,padx=5,pady=100)

lettreGlobale=tkinter.StringVar()
lettreGlobale.set("A")
champ_lettreGlobale = tkinter.Entry(maFenetre,textvariable=lettreGlobale, bg="white", width="10")
champ_lettreGlobale.grid(row=1,column=10,padx=5,pady=235)


#Label lettre locale et champ de saisie
Text2 = tkinter.StringVar()
l_lettreLocale = tkinter.Label(maFenetre, textvariable=Text2)
Text2.set("Lettre Locale : ")
l_lettreLocale.grid(row=1,column=15,padx=5,pady=100)

lettreLocale=tkinter.IntVar()
lettreLocale.set("B")
champ_lettreLocale =  tkinter.Entry(maFenetre,textvariable=lettreLocale, bg="white", width="10")
champ_lettreLocale.grid(row=1,column=20,padx=5,pady=235)


#---------------------------------------------------------------------TAILLE DES LETTRES GLOBALES
t_tailleGX = tkinter.StringVar()
l_tailleGX = tkinter.Label(maFenetre, textvariable=t_tailleGX)
t_tailleGX.set("Lettre Locale : ")
l_tailleGX.grid(row=2,column=1,padx=10,pady=100)

nb_tailleGX = tkinter.IntVar()
nb_tailleGX.set(800)
champ_tailleGX = tkinter.Entry(maFenetre,textvariable=nb_tailleGX, bg="white", width="10")
champ_tailleGX.grid(row=2,column=10,padx=0,pady=235)





#--------------------------------------------------------------------- BOUTON GENERER

#Bouton générer
bt_Generer = tkinter.Button(maFenetre,text="Générer",command=generer)
bt_Generer.grid(row=5,column=10,padx=15,pady=5)

#--------------------------------------------------------------------- GENERATION FENETRE

#CREATION FENETRE
maFenetre.mainloop()


