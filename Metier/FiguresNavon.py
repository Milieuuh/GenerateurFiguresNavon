import elementGlobal, elementLocal, Parseur
from PIL import Image, ImageDraw

class FigureNavon:

    # ATTRIBUTS
    elementGlobal = ""
    elementLocal = ""
    tailleLG = 0
    listeFiguresNavon = []
    

    #CONSTRUCTEUR
    def __init__(self, elementG, elementL, taille):
        self.elementGlobal = elementG
        self.elementLocal = elementL
        self.mesureTailleSegments = 0
        self.tailleLG=taille
        self.densite = 0.5
        self.valeurMoyenneDeSymboles = 0
        self.nombreDeSegmentsDansLettre = 0


    #METHODES

    def calculMesureTailleSegments(self, Xa, Ya, Xb, Yb):
        print("calcul taille de la lettre")
        self.mesureTailleSegments = self.mesureTailleSegments +((Ya-Xa)**2 +(Yb-Xb)**2)**(1/2) 
        


    def creerFigureNavon(self):
        print("creation Figure")
        self.parser = Parseur.Parseur("lettre"+self.elementGlobal+".json", elementGlobal)
        self.parser.lireFichier()

        #creation de l'image
        img_figure_navon = Image.new("RGB", (512, 512), "white")

        img1 = ImageDraw.Draw(img_figure_navon)

        i=0
        while i<len(self.parser.getListeCoordonnees()):
            #mesure de la taille de tous les segments
            self.calculMesureTailleSegments(self.parser.get(i)*self.tailleLG//100, self.parser.get(i+1)*self.tailleLG//100, self.parser.get(i+2)*self.tailleLG//100, self.parser.get(i+3)*self.tailleLG//100)
            self.nombreDeSegmentsDansLettre=self.nombreDeSegmentsDansLettre+1
            print(self.mesureTailleSegments)
            i=i+4

        i=0
        
        while i<len(self.parser.getListeCoordonnees()):
             self.placementElementsLocaux(self.parser.get(i)*self.tailleLG//100, self.parser.get(i+1)*self.tailleLG//100, self.parser.get(i+2)*self.tailleLG//100, self.parser.get(i+3)*self.tailleLG//100, img1)
             i=i+4
            
       
        img_figure_navon.show()
        #self.sauvegarderFigure(img1)

 
    def calculEquationDroite(self, Xa, Ya, Xb, Yb, img):
        m= (Yb-Ya)/(Xb-Xa)
        p= Ya - Xa*m
        i=Xa
        self.valeurMoyenneDeSymboles = self.densite*self.mesureTailleSegments
        while i<Xb:
            y= m*i+p
            texte = img.multiline_text((i,y), str(self.elementLocal), fill=(0, 255, 0))
            i=i+(self.valeurMoyenneDeSymboles//self.nombreDeSegmentsDansLettre)/2
        

    def placementElementsLocaux(self, Xa, Ya, Xb, Yb, img):        
        #calcul de l'équation des droites
            #coeff directeur m et de p
        if Xb-Xa!=0:
            if Xb>Xa:
               self.calculEquationDroite(Xa, Ya, Xb, Yb, img)
            else:
                self.calculEquationDroite(Xb, Yb, Xa, Ya, img)

            #x=k, k étant une constante
        elif Xa==Xb:
            y=Ya
            self.valeurMoyenneDeSymboles = self.densite * self.mesureTailleSegments
            while y<Yb:
                texte = img.multiline_text((Xa,y), str(self.elementLocal), fill=(0, 0, 0))
                y= y+(self.valeurMoyenneDeSymboles/self.nombreDeSegmentsDansLettre)/2



    def ajouterFigureNavon(newFigureNavon):
        listeFiguresNavon.append(newFigureNavon)

    def sauvegarderFigure(image):
        #image.save('nom')
        print("sauvegarde")
        
    
        
    ###############################################GETTER
    def getElementGlobal(self):
        return self.elementGlobal

    def getElementLocal(self):
        return self.elementLocal

    def getListeFiguresNavon(self):
        return self.listeFiguresNavon


#F = FigureNavon("L","N") 
#F.creerFigureNavon()
