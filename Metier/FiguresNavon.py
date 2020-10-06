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
        self.parser = Parseur.Parseur("lettreA.json", elementGlobal)
        self.parser.lireFichier()

        #creation de l'image
        img_figure_navon = Image.new("RGB", (512, 512), "white")

        img1 = ImageDraw.Draw(img_figure_navon)

        
        img1.line((self.parser.get(0), self.parser.get(1)), fill=(0,0,255), width=5)
        img1.line((self.parser.get(2), self.parser.get(3)), fill=(0,0,255), width=5)
        img1.line((self.parser.get(4), self.parser.get(5)), fill=(0,0,255), width=5)

        img_figure_navon.show()
        #self.sauvegarderFigure(img1)        
        
        
        
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


F = FigureNavon("M","N")
F.creerFigureNavon()
