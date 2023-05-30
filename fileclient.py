import fileaddress
class client :
    def __init__(self,cin,nom,prenom,age,address,adressmail,numphone):
        self.cin=cin
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.address=address
        self.adressmail=fileaddress.addressc(adressmail)
        self.numphone=numphone
    def affichec(self):
        print("le cin:" ,self.cin, "le nom:" ,self.nom, "le prenom:" ,self.prenom ,"l age:", self.age, "l addresse" ,self.address ,"l adresse mail" ,self.adressmail.affichead(), "le numero phone" ,self.numphone)
        
        
        