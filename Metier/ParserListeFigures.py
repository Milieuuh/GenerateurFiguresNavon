class ParserListeFigures:


    #CONSTRUCTEUR
    def __init__(self, nomFile):
        self.nomFichier=nomFile
        self.lettreGlobal = ""
        self.lettreLocal = ""
        self.tailleImageWidth = 0
        self.tailleImageHeight = 0
        self.marginX = 0
        self.marginY = 0
        self.sizeLettreLocal = 0
        self.densite = 0

    #METHODES POUR PARSER LE FICHIER
    def recupererDonneesFichier(self):
        with open(self.nomFichier, "r") as fichier:
            lignes = fichier.readlines()
        for ligne in lignes:
            champs = ligne.split()
            self.lettreGlobal= champs[0]
            self.lettreLocal= champs[1]
            self.tailleImageWidth= champs[2]
            self.tailleImageHeight= champs[3]
            self.marginX= champs[4]
            self.marginY= champs[5]
            self.sizeLettreLocal= champs[6]
            self.densite= champs[7]

    ##################################GETTER
    def getNomfichier(self):
        return self.nomFichier

    def getLettreGlobal(self):
        return self.lettreGlobal

    def getLettreLocal(self):
        return self.lettreLocal

    def getTailleImageWidth(self):
        return self.tailleImageWidth

    def getTailleImageHeight(self):
        return self.tailleImageHeight

    def getMarginX(self):
        return self.marginX

    def getMarginY(self):
        return self.marginY

    def getSizeLettreLocal(self):
        return self.sizeLettreLocal

    def getDensite(self):
        return self.densite

    ############################SETTER
    def setNomFichier(self, nom):
        self.nomFichier = nom

    def setLettreGlobal(self, lG):
        self.lettreGlobal = lG

    def setLettreLocal(self, lL):
        self.nomFichier = lL

    def setTailleImageWidth(self, tailleX):
        self.tailleImageWidth = tailleX

    def setTailleImageHeight(self, tailleY):
        self.tailleImageHeight = tailleY

    def setMarginX(self, marge):
        self.marginX = marge

    def setMarginY(self, marge):
        self.marginY = marge

    def setSizeLettreLocal(self, size):
        self.sizeLettreLocal = size

    def setDensite(self, density):
        self.densite = density


monParseur = ParserListeFigures("C:/Users/Emilie Genton/Documents/GitHub/GenerateurFiguresNavon/Metier/text")
monParseur.recupererDonneesFichier()