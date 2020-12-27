import elementGlobal, elementLocal, Parseur
import matplotlib
import numpy as np
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

    def __init__(self, elementG, elementL, LGHeight, LGWidth, LL,densite, margeX, margeY):
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

        #AJOUT MARGES GAUCHE ET HAUT
        self.margeX = margeX
        self.margeY = margeY


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

        #on s'occupe des droites en fonction des coordonées obtenues par le parser
        i=0
        while i<len(self.parser.getListeCoordonnees()):
            #mesure de la taille de tous les segments
            self.calculMesureTailleSegments(self.parser.get(i)*self.tailleLGWidth//100+self.margeX, self.parser.get(i+1)*self.tailleLGWidth//100+ self.margeY,
                                            self.parser.get(i+2)*self.tailleLGWidth//100+self.margeX, self.parser.get(i+3)*self.tailleLGWidth//100+ self.margeY)
            self.nombreDeSegmentsDansLettre=self.nombreDeSegmentsDansLettre+1
            print(self.mesureTailleSegments)
            i = i+4

        i=0
        compteur =0
        while i<len(self.parser.getListeCoordonnees()):
             self.placementElementsLocaux(self.parser.get(i)*self.tailleLGWidth//100+self.margeX, self.parser.get(i+1)*self.tailleLGWidth//100+ self.margeY,
                                          self.parser.get(i+2)*self.tailleLGWidth//100+self.margeX, self.parser.get(i+3)*self.tailleLGWidth//100+ self.margeY,
                                          img1, compteur)
             compteur = compteur + 1
             i = i+4

        i=0
        #Pour la liste des coordonnées et angles des arcs
        while i < len(self.parser.getListeCurve()):
            self.dessinerArc(self.parser.getElementCurve(i) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 1) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 2) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 3) * self.tailleLG // 100,
                                         self.parser.getElementCurve(i + 4),
                                         self.parser.getElementCurve(i + 5), img1, img_figure_navon)
            compteur = compteur + 1
            i = i + 6


        self.mesureTailleSegments = 0
        self.listeTailleDesSegments = []
       


        return img_figure_navon

    def preview(self, img):
        img.show()
 
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

    def dessinerArc(self, X1, Y1,X2, Y2, angleDepart, angleArrive, imgDraw, img):
        print("dessiner un arc de cercle")
        b = Y1
        #on dessine l'arc en rouge
        imgDraw.arc([(X1, Y1), (X2, Y2)], angleDepart, angleArrive, fill=(255,0,0))
        font = ImageFont.truetype("arial.ttf", size=self.tailleLL)
        compteur = 0
        for i in range (self.tailleLGWidth):
            for j in range (self.tailleLGHeigh):
                r, g, b = img.getpixel((i, j))
                #si le pixel est dans les tons rouges, alors on est sur l'arc et donc on remet le pixel en blanc
                if r > g and r > b:
                    img.putpixel((i,j), (255,255,255))
                    compteur = compteur+1
                    if compteur == 50:
                        compteur = 0
                        imgDraw.text((i, j), str(self.elementLocal), fill=(0, 0, 0), font=font)


    def ajouterFigureNavon(self, newFigureNavon):
        self.listeFiguresNavon.append(newFigureNavon)

    def sauvegarderFigure(self, image, filePath):
        image.save(filePath)
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

    def getMargeX(self):
        return self.margeX

    def getMargeY(self):
        return self.margeY

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

    def setMargeX(self, nb):
        self.margeX = nb

    def setMargeY(self, nb):
            self.margeY= nb
