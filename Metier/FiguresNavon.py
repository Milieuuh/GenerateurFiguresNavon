import elementGlobal, elementLocal, Parseur
import matplotlib
from PIL import Image, ImageDraw, ImageFont
from PIL import *
from math import *
from matplotlib.patches import *
import matplotlib.pyplot as plt

class FigureNavon:

    # ATTRIBUTS
    elementGlobal = ""
    elementLocal = ""
    tailleLG = 0
    fichier = ""
    nbCaracteresLocaux=0
    

    #CONSTRUCTEUR
    def __init__(self):
        print("costructeur")

    def __init__(self, elementG, elementL, LGHeight, LGWidth, LL,densite):
        self.elementGlobal = elementG
        self.elementLocal = elementL
        self.mesureTailleSegments = 0
        self.tailleLG=400
        self.densite = densite
        self.valeurMoyenneDeSymboles = 0
        self.nombreDeSegmentsDansLettre = 0
        self.listeTailleDesSegments = []
        self.listeFiguresNavon = []

        #RAJOUTS PAR RAPPORT AUX TAILLES DE LETTRES
        self.tailleLGHeight = LGHeight
        self.tailleLGWidth = LGWidth
        self.tailleLL = LL


    #METHODES

    def calculMesureTailleSegments(self, Xa, Ya, Xb, Yb):
        print("calcul taille de la lettre")
        self.mesureTailleSegments = self.mesureTailleSegments +((Xb-Xa)**2 +(Yb-Ya)**2)**(1/2)
        print(((Xb-Xa)**2 +(Yb-Ya)**2)**(1/2))
        self.listeTailleDesSegments.append(((Xb-Xa)**2 +(Yb-Ya)**2)**(1/2))
        


    def creerFigureNavon(self):
        print("creation Figure")
        self.parser = Parseur.Parseur(self.elementGlobal+".json", self.elementGlobal)
        self.parser.lireFichier()

        #creation de l'image
        img_figure_navon = Image.new("RGB", (self.tailleLGWidth, self.tailleLGHeight), "white")

        img1 = ImageDraw.Draw(img_figure_navon)

        i=0
        while i<len(self.parser.getListeCoordonnees()):
            #mesure de la taille de tous les segments
            self.calculMesureTailleSegments(self.parser.get(i)*self.tailleLGWidth//100, self.parser.get(i+1)*self.tailleLGWidth//100,
                                            self.parser.get(i+2)*self.tailleLGWidth//100, self.parser.get(i+3)*self.tailleLGWidth//100)
            self.nombreDeSegmentsDansLettre=self.nombreDeSegmentsDansLettre+1
            print(self.mesureTailleSegments)
            i = i+4

        i=0
        compteur =0
        while i<len(self.parser.getListeCoordonnees()):
             self.placementElementsLocaux(self.parser.get(i)*self.tailleLGWidth//100, self.parser.get(i+1)*self.tailleLGWidth//100,
                                          self.parser.get(i+2)*self.tailleLGWidth//100, self.parser.get(i+3)*self.tailleLGWidth//100,
                                          img1, compteur)
             compteur = compteur + 1
             i = i+4

        i=0
        for index in self.parser.getListeCurve():
            print(index)

        while i < len(self.parser.getListeCurve()):
            self.dessiner(self.parser.getElementCurve(i) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 1) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 2) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 3) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 4),
                                         self.parser.getElementCurve(i + 5), img1)
            compteur = compteur + 1
            i = i + 6


       
        img_figure_navon.show()
        self.mesureTailleSegments =0
        self.listeTailleDesSegments = []

        return img_figure_navon
        #self.sauvegarderFigure(img_figure_navon)

 
    def calculEquationDroite(self, Xa, Ya, Xb, Yb, img, numSegment):
        m= (Yb-Ya)/(Xb-Xa)
        p= Ya - Xa*m
        i=Xa

        nbElementsLocaux = self.densite * self.mesureTailleSegments / self.tailleLL
        nbElementSurMonSegment = nbElementsLocaux * self.listeTailleDesSegments[numSegment]*self.densite/ self.mesureTailleSegments
        ecart = (self.listeTailleDesSegments[numSegment]*self.densite) / nbElementSurMonSegment
        while i<Xb:
            y= m*i+p
            font = ImageFont.truetype("arial.ttf", size=self.tailleLL)
            img.multiline_text((i, y), str(self.elementLocal), fill=(0, 0, 0), font=font)
            i = i+ecart
        

    def placementElementsLocaux(self, Xa, Ya, Xb, Yb, img, numSegment):
        #calcul de l'équation des droites
            #coeff directeur m et de p
        if Xb-Xa != 0:
            if Xb > Xa:
               self.calculEquationDroite(Xa, Ya, Xb, Yb, img, numSegment)
            else:
                self.calculEquationDroite(Xb, Yb, Xa, Ya, img, numSegment)

            #x=k, k étant une constante
        elif Xa == Xb:
            y=Ya
            nbElementsLocaux = self.densite * self.mesureTailleSegments / self.tailleLL
            nbElementSurMonSegment = nbElementsLocaux * self.listeTailleDesSegments[numSegment]  / self.mesureTailleSegments
            ecart = (self.listeTailleDesSegments[numSegment] * self.densite) / nbElementSurMonSegment
            while y <self.listeTailleDesSegments[numSegment]:
                font = ImageFont.truetype("arial.ttf", size=self.tailleLL)
                img.multiline_text((Xa, y), str(self.elementLocal),  fill=(0, 0, 0), font=font)
                y= y+ecart

    def dessiner(self, X1, Y1,X2, Y2, angleDepart, angleArrive, img):
        print("dessiner un arc de cercle")

        #img.arc([(X, Y), (width,width)], 0, 360, fill=(255,0,0))

        img.arc([(X1, Y1), (X2, Y2)], angleDepart, angleArrive, fill=(255, 0, 0))
        #img.arc([(50, 50), (50, 50)], 90, 270, fill=(255, 0, 0))

        #img.ellipse(X, Y, width, height, angle)


    def ajouterFigureNavon(self, newFigureNavon):
        self.listeFiguresNavon.append(newFigureNavon)

    def sauvegarderFigure(self, image):
        image.save('nom.png')
        print("sauvegarde")

    def chargerFigure(self, fichier):
        self.fichier=fichier
        
    ###############################################GETTER
    def getElementGlobal(self):
        return self.elementGlobal

    def getElementLocal(self):
        return self.elementLocal

    def getListeFiguresNavon(self):
        return self.listeFiguresNavon

    def getNomFichier(self):
        return self.fichier

    def getTailleLG(self):
        return self.tailleLG

    def getNbCaractere(self):
        return self.nbCaracteresLocaux

    def getHeightLG(self):
        return self.tailleLGHeight

    def getWidthLG(self):
        return self.tailleLGWidth

    def getHeightLL(self):
        return self.tailleLLHeight

    def getWidthLL(self):
        return self.tailleLLWidth

    ###############################################SETTER
    def setElementGlobal(self, elmt):
        self.elementGlobal=elmt

    def setElementLocal(self,elmt):
        self.elementLocal=elmt

    def setNbCaractereLocaux(self, nb):
        self.nbCaracteresLocaux = nb

    def setDensite(self, nb):
        self.densite = nb

    def setHeightLG(self, nb):
        self.tailleLGHeigh = nb

    def setWidthLG(self, nb):
        self.tailleLGWidth = nb

    def setTailleLL(self, nb):
        self.tailleLL = nb
