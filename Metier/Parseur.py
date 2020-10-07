import json

class Parseur:

    #ATTRIBUTS
    elementGlobal = ""
    nomFichier = ""


    #CONSTRUCTEUR
    def __init__(self, nomFile, elementG):
        self.nomFichier=nomFile
        self.elementGlobal = elementG
        self.listeCoordonnees = []


    #METHODES
        
      #permet de lire le fichier de description du symbole
    def lireFichier(self):
        print("Lecture en cours du fichier")

        with open("../Templates/"+self.nomFichier, 'r') as fichier:
            data = json.load(fichier)

        self.recupererPoints(data)

        print(self.listeCoordonnees)

        
       

        #récupère les points de départ et d'arrivée des différentes droites qui composent l'élément global
    def recupererPoints(self,data):
        i=0
        for x in data:
             i=i+1

        
        for nb in range(0,i):
            self.listeCoordonnees.append(int(data['Droite '+ str(nb)]['Point Depart X']))
            self.listeCoordonnees.append(int(data['Droite '+ str(nb)]['Point Depart Y']))
            self.listeCoordonnees.append(int(data['Droite '+ str(nb)]['Point Arrive X']))
            self.listeCoordonnees.append(int(data['Droite '+ str(nb)]['Point Arrive Y']))


    def get(self, numero):
            return self.listeCoordonnees[numero]

        
    ##############################GETTER
    def getNomFichier():
        return self.nomFichier

    def getListeCoordonnees():
        return self.listeCoordonnees


    
