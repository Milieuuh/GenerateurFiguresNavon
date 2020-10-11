import elementGlobal, elementLocal, Parseur
from PIL import Image, ImageDraw

class FigureNavon:

    # ATTRIBUTS
    elementGlobal = ""
    elementLocal = ""
    listeFiguresNavon = []
    

    #CONSTRUCTEUR
    def __init__(self, elementG, elementL):
        self.elementGlobal = elementG
        self.elementLocal = elementL
        


    #METHODES

    def creerFigureNavon(self):
        print("creation Figure")
        self.parser = Parseur.Parseur("lettre"+self.elementGlobal+".json", elementGlobal)
        self.parser.lireFichier()

        #creation de l'image
        img_figure_navon = Image.new("RGB", (512, 512), "white")

        img1 = ImageDraw.Draw(img_figure_navon)

        i=0
        while i<len(self.parser.getListeCoordonnees()):
             #img1.line([(self.parser.get(i), self.parser.get(i+1)), (self.parser.get(i+2), self.parser.get(i+3))], fill=(0,0,255), width=5)
             self.placementElementsLocaux(self.parser.get(i), self.parser.get(i+1), self.parser.get(i+2), self.parser.get(i+3), img1)
             i=i+4
            
       
        img_figure_navon.show()
        #self.sauvegarderFigure(img1)
        

    def placementElementsLocaux(self, Xa, Ya, Xb, Yb, img):
        #calcul de l'équation des droites
            #coeff directeur m et de p
        if Xb-Xa!=0:
            if Xb>Xa:
                m= (Yb-Ya)/(Xb-Xa)
                p= Ya - Xa*m

                i=Xa
                for i in range(Xa, Xb, 10):
                    y= m*i+p
                    texte = img.multiline_text((i,y), str(self.elementLocal), fill=(0, 0, 0))
            else:
                m= (Ya-Yb)/(Xa-Xb)
                p= Ya - Xa*m

                i=Xa
                for i in range(Xb, Xa, 10):
                    y= m*i+p
                    texte = img.multiline_text((i,y), str(self.elementLocal), fill=(0, 0, 0))

            #x=k, k étant une constante
        elif Xa==Xb:
            y=Ya
            while y<Yb:
                texte = img.multiline_text((Xa,y), str(self.elementLocal), fill=(0, 0, 0))
                y= y+10
      
                
        
        
    def ajouterFigureNavon(newFigureNavon):
        listeFiguresNavon.append(newFigureNavon)

    def sauvegarderFigure(image):
        #image.save('nom')
        print("sauvegarde")
        

        
    ###############################################GETTER
    def getElementGlobal():
        return self.elementGlobal

    def getElementLocal():
        return self.elementLocal

    def getListeFiguresNavon():
        return self.listeFiguresNavon


#F = FigureNavon("M","N") 
#F.creerFigureNavon()
