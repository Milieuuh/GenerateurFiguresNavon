import elementGlobal, elementLocal, Parseur, ParserListeFigures
import matplotlib
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from PIL import *
from math import *
from matplotlib.patches import *

import matplotlib.pyplot as plt
import turtle

class FigureNavon:


    #CONSTRUCTEUR
    def __init__(self):
        print("constructeur")

    def __init__(self, elementG, elementL, tailleX, tailleY, LGHeight, LGWidth,margeX, margeY ,LL,  densite):
        self.elementGlobal = elementG
        self.elementLocal = elementL
        self.mesureTailleSegments = 0
        self.tailleLG=400
        self.densite = densite
        self.valeurMoyenneDeSymboles = 0
        self.nombreDeSegmentsDansLettre = 0
        self.listeTailleDesSegments = []
        self.listeFiguresNavon = []
        self.tailleX= tailleX
        self.tailleY= tailleY

        #RAJOUTS PAR RAPPORT AUX TAILLES DE LETTRES
        self.tailleLGHeight = LGHeight
        self.tailleLGWidth = LGWidth
        self.tailleLL = LL

        #AJOUT MARGES GAUCHE ET HAUT
        self.margeX = margeX
        self.margeY = margeY

        #fichier chargé ?
        self.fichierCharge = False
        self.cheminFichierCharge = ""

        self.aUnArc = False


    #METHODES

    def calculMesureTailleSegments(self, Xa, Ya, Xb, Yb):
        print("calcul taille de la lettre")
        self.mesureTailleSegments = self.mesureTailleSegments +((Xb-Xa)**2 +(Yb-Ya)**2)**(1/2)
        print(((Xb-Xa)**2 +(Yb-Ya)**2)**(1/2))
        self.listeTailleDesSegments.append(((Xb-Xa)**2 +(Yb-Ya)**2)**(1/2))

    def calculMesureTailleSegmentsArc(self, Xa, Ya, Xb, Yb, angled, angleF):
        angleDegre = angleF - angled
        angleRadian = angleDegre * 2 * math.pi / 360
        self.mesureTailleSegments = self.mesureTailleSegments + 2*math.pi*(Ya-Yb)
        self.listeTailleDesSegments.append(2*math.pi*(Ya-Yb))


    def creerFigureNavon(self):
        print("creation Figure")
        self.parser = Parseur.Parseur(self.elementGlobal+".json", self.elementGlobal)
        self.parser.lireFichier()

        #creation de l'image
        self.img_figure_navon = Image.new("RGB", (self.tailleX, self.tailleY), "white")

        img1 = ImageDraw.Draw(self.img_figure_navon)

        if self.parser.getListeCurve()!=0:
            self.aUnArc = True

        #on s'occupe des droites en fonction des coordonées obtenues par le parser
        i=0
        while i<len(self.parser.getListeCoordonnees()):
            #mesure de la taille de tous les segments
            self.calculMesureTailleSegments(self.parser.get(i)*((self.tailleLGWidth+self.tailleLGHeight)/2)//100 + self.margeX,
                                            self.parser.get(i+1)*((self.tailleLGWidth+self.tailleLGHeight)/2)//100 + self.margeY,
                                            self.parser.get(i+2)*((self.tailleLGWidth+self.tailleLGHeight)/2)//100 + self.margeX,
                                            self.parser.get(i+3)*((self.tailleLGWidth+self.tailleLGHeight)/2)//100 + self.margeY)

            self.nombreDeSegmentsDansLettre=self.nombreDeSegmentsDansLettre+1
            print(self.mesureTailleSegments)
            i = i+4

        while i < len(self.parser.getListeCurve()):
            # mesure de la taille de tous les segments
            self.calculMesureTailleSegmentsArc(
                self.parser.getElementCurve(i) * ((self.tailleLGWidth + self.tailleLGHeight) / 2) // 100 + self.margeX,
                self.parser.getElementCurve(i + 1) * ((self.tailleLGWidth + self.tailleLGHeight) / 2) // 100 + self.margeY,
                self.parser.getElementCurve(i + 2) * ((self.tailleLGWidth + self.tailleLGHeight) / 2) // 100 + self.margeX,
                self.parser.getElementCurve(i + 3) * ((self.tailleLGWidth + self.tailleLGHeight) / 2) // 100 + self.margeY,
                self.parser.getElementCurve(i + 4),
                self.parser.getElementCurve(i + 5)
            )

            self.nombreDeSegmentsDansLettre = self.nombreDeSegmentsDansLettre + 1
            print(self.mesureTailleSegments)
            i = i + 6

        i=0
        compteur =-1
        while i<len(self.parser.getListeCoordonnees()):
            compteur = compteur + 1
            self.placementElementsLocaux(self.parser.get(i) * ((self.tailleLGWidth+self.tailleLGHeight)/2) // 100 + self.margeX,
                                          self.parser.get(i + 1) * ((self.tailleLGWidth+self.tailleLGHeight)/2) // 100 + self.margeY,
                                          self.parser.get(i + 2) * ((self.tailleLGWidth+self.tailleLGHeight)/2) // 100 + self.margeX,
                                          self.parser.get(i + 3) * ((self.tailleLGWidth+self.tailleLGHeight)/2) // 100 + self.margeY,
                                          img1, compteur)

            i = i+4

        i=0
        print("nombre ", len(self.listeTailleDesSegments))
        #Pour la liste des coordonnées et angles des arcs
        while i < len(self.parser.getListeCurve()):
            compteur = compteur + 1
            self.dessinerArc(self.parser.getElementCurve(i) * self.tailleLGWidth // 100 + self.margeX,
                                         self.parser.getElementCurve(i + 1) * ((self.tailleLGWidth+self.tailleLGHeight)/2) // 100 + self.margeY,
                                         self.parser.getElementCurve(i + 2) * ((self.tailleLGWidth+self.tailleLGHeight)/2) // 100 + self.margeX,
                                         self.parser.getElementCurve(i + 3) * ((self.tailleLGWidth+self.tailleLGHeight)/2) // 100 + self.margeY,
                                         self.parser.getElementCurve(i + 4),
                                         self.parser.getElementCurve(i + 5), img1, self.img_figure_navon, compteur-1)

            i = i + 6




        self.mesureTailleSegments = 0
        self.listeTailleDesSegments = []
        return self.img_figure_navon

    def preview(self, img):
        img.show()
 
    def calculEquationDroite(self, Xa, Ya, Xb, Yb, img, numSegment):
        m= (Yb-Ya)/(Xb-Xa)
        p= Ya - Xa*m
        i=Xa
        x1 = Xa
        y1 = Xb

        nbElementsLocaux = self.densite * self.mesureTailleSegments / self.tailleLL
        nbElementSurMonSegment = nbElementsLocaux * self.listeTailleDesSegments[numSegment]*self.densite/ self.mesureTailleSegments
        ecart = (self.listeTailleDesSegments[numSegment]*self.densite) / nbElementSurMonSegment
        while i<Xb:
            y= m*i+p
            distance = sqrt((x1-i)**2 + (y-y1)**2)
            if distance >= ecart:
                font = ImageFont.truetype("arial.ttf", size=int(self.tailleLL))
                img.multiline_text((i, y), str(self.elementLocal), fill=(0, 0, 0), font=font)
                x1 = i
                y1 = y

            i = i+1

        #img.multiline_text((Xb, Yb), str(self.elementLocal), fill=(0, 0, 0), font=font)
        

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
            nbElementSurMonSegment =nbElementsLocaux * self.listeTailleDesSegments[numSegment]*self.densite/ self.mesureTailleSegments
            ecart = (self.listeTailleDesSegments[numSegment] * self.densite) / nbElementSurMonSegment
            while y <self.listeTailleDesSegments[numSegment]+self.margeY:
                font = ImageFont.truetype("arial.ttf", size=int(self.tailleLL))
                img.multiline_text((Xa, y), str(self.elementLocal),  fill=(0, 0, 0), font=font)
                y = y+ecart

    def dessinerArc(self, X1, Y1,X2, Y2, angleDepart, angleArrive, imgDraw, img, numSegment):
        print("dessiner un arc de cercle")

        #on dessine l'arc en rouge
        imgDraw.arc([(X1, Y1), (X2, Y2)], angleDepart, angleArrive, fill=(255,0,0))
        font = ImageFont.truetype("arial.ttf", size=int(self.tailleLL))
        compteur = 0
        for i in range (self.tailleX):
            for j in range (self.tailleY):
                r, g, b = img.getpixel((i, j))
                #si le pixel est dans les tons rouges, alors on est sur l'arc et donc on remet le pixel en blanc
                if r > g and r > b:
                    img.putpixel((i,j), (255,255,255))
                    compteur = compteur+1
                    #if compteur > ecart:
                       # compteur = 0
                    imgDraw.text((i, j), str(self.elementLocal), fill=(0, 0, 0), font=font)
            '''
        elif img.getpixel(i, j) == (0,0,0):
            imgDraw.text((i, j), str(self.elementLocal), fill=(0, 0, 0), font=font)'''





    def ajouterFigureNavon(self, newFigureNavon):
        self.listeFiguresNavon.append(newFigureNavon)

    def sauvegarderFigure(self, image, filePath):
        image.save(filePath)
        print("sauvegarde")

    def chargerFigure(self, fichier):
        self.fichier=fichier
        self.fichierCharge = True
        self.cheminFichierCharge = fichier

        parseurFichier = ParserListeFigures.ParserListeFigures(fichier)
        parseurFichier.recupererDonneesFichier()

        for element in parseurFichier.getListeFigures():
            self.ajouterFigureNavon(element)


    def genererToutesLesfiguresDUnFichier(self, cheminFichierLecteur, cheminSauvegarde):
        print("génération des figures à partir d'un fichier")
        parseurFichier = ParserListeFigures.ParserListeFigures(cheminFichierLecteur)
        parseurFichier.recupererDonneesFichier()

        i=0
        for element in parseurFichier.getListeFigures():
            self.ajouterFigureNavon(element)
            element.creerFigureNavon()
            element.sauvegarderFigure(element.img_figure_navon, cheminSauvegarde+"/"+str(i)+".png")
            i = i +1


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

    def getTailleLL(self):
        return self.tailleLL

    def getMargeX(self):
        return self.margeX

    def getMargeY(self):
        return self.margeY

    def getFichierCharge(self):
        return self.fichierCharge

    def getCheminFichierCharge(self):
        return  self.cheminFichierCharge

    def getDensite(self):
        return  self.densite

    def getTailleX(self):
        return  self.tailleX

    def getTailleY(self):
        return  self.tailleY

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
        self.tailleLGHeight = nb

    def setWidthLG(self, nb):
        self.tailleLGWidth = nb

    def setTailleLL(self, nb):
        self.tailleLL = nb

    def setMargeX(self, nb):
        self.margeX = nb

    def setMargeY(self, nb):
            self.margeY= nb

    def setTailleX(self, nb):
        self.tailleX = nb

    def setTailleY(self, nb):
        self.tailleY = nb

    def setFichierCharge(self, bool):
        self.fichierCharge = bool


    #############################################toString
    def toString(self):
        return self.getElementGlobal() + " " + self.getElementLocal()+" "+str(self.getTailleX())+" "+str(self.getTailleY())+" "+str(self.getWidthLG())+" "+str(self.getHeightLG())+" "+str(self.margeX)+" "+str(self.margeY)+" "+str(self.tailleLL)+" "+str(self.getDensite())

        #return self.getElementGlobal()+" "+self.getElementLocal()+" "+str(self.getWidthLG())+" "+str(self.getHeightLG())+" "+str(self.densite)+" "+str(self.tailleLL)+" "+str(self.margeX)+" "+str(self.margeY())
