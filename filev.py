import filedate
class car :
    def __init__(self,mat,marq,color,jour,mois,annee,prix):
        self.mat=mat
        self.marq=marq
        self.color=color
        self.dateachat=filedate.date(jour,mois,annee)
        self.prix=prix
        self.etat=0
    def changeetat(self):
        self.etat=1
    def date(self):
        return(self.dateachat.yearsnumber())
    def affichec(self):
        print("le mat:", self.mat,"le marq:", self.marq,"le couleur", self.color, "le date d achat", self.dateachat.affiched() ,"le prix", self.prix ,"l etat ", self.etat)
        
    
        
        
    
    