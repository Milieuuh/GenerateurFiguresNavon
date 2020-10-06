

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
    def ajouterFigureNavon(newFigureNavon):
        listeFiguresNavon.append(newFigureNavon)

    def sauvegarderFigure():
        print("sauvegarde")

        
    ###############################################GETTER
    def getElementGlobal():
        return self.elementGlobal

    def getElementLocal():
        return self.elementLocal

    def getListeFiguresNavon():
        return self.listeFiguresNavon
