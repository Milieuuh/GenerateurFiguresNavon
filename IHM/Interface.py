
import tkinter
import aider
import aPropos

class Interface:


    def __init__(self):
        print("constructeur")

    def fenetreApropos():
        print("a voir pour apropos")

#Création de la fenêtre principale
        monInterface = Tk()

        monInterface.title("générateur de Navon")
        monInterface.geometry("300x400")



#Création d'un bouton aPropos
        bt_aPropos = Button(monInterface, text="i",command=fenetreApropos)
        bt_aPropos.grid(row=1,column=0,padx=5,pady=50)

        monInterface.mainloop()
