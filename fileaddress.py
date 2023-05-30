class addressc:
    def __init__(self,adress):
        if(adress.count('a')==1):
            self.address=adress
        else:
            raise ValueError
    def changeadressmail(self,adress):
        if(adress.count('a')==1):
            self.address=adress
        else:
            print("l adresse n est pas valide")
    def affichead(self):
        return(str(self.address))

        
        
        
        