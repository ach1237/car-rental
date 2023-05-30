import fileclient
class clients:
    def __init__(self):
        self.lclients=[]
    def ajouterclient(self,cin,nom,prenom,age,address,adressmail,numphone):
        n=0
        for i in range(len(self.lclients)):
            if(self.lclients[i].cin==cin):
                break
            n=i+1
        if(n>=len(self.lclients)):
            self.lclients.append(fileclient.client(cin,nom,prenom,age,address,adressmail,numphone))
        else:
            print("le client existe")
    def supprimerclient(self,cin):
        n=0
        for i in range(len(self.lclients)):
            if(self.lclients[i].cin==cin):
                break
            n=i+1
        if(n<len(self.lclients)):
            self.lclients.remove(self.lclients[i])
        else:
            print("le client n existe pas ")
    def modifieradresse(self,cin,adresse):
        n=0
        for i in range(len(self.lclients)):
            if(self.lclients[i].cin==cin):
                break
            n=i+1
        if(n<len(self.lclients)):
            self.lclients[i].address=adresse
        else:
            print("le client n est pas trouvee")
    def modifiernumphone(self,cin,numphone):
        n=0
        for i in range(len(self.lclients)):
            if(self.lclients[i].cin==cin):
                break
            n=i+1
        if(n<len(self.lclients)):
            self.lclients[i].numphone=numphone
        else:
            print("le client n est pas trouvee")
    def modifieradressemail(self,cin,adressmail):
        n=1
        for i in range(len(self.lclients)):
            if(self.lclients[i].cin==cin):
                break
            n=i
        if(n<len(self.lclients)):
            self.lclients[i].adressmail.changeadressmail(adressmail)
        else:
            print("le client n est pas trouvee")
    def recherchecin(self,cin):
        n=0
        l=[]
        for i in range(len(self.lclients)):
            if(self.lclients[i].cin==cin):
                break
            n=i+1
        if(n<len(self.lclients)):
            self.lclients[i].affichec()
            l.append(self.lclients[i])
            return l
        else:
            return l
            print("le client n est pas trouvee")
    def fileoutputclients(self):
        l=[]
        f=open(r"C:\Users\21653\Documents\fileclients.txt","w")
        for i in range(len(self.lclients)):
            l.append(str(self.lclients[i].cin)+' ')
            l.append(str(self.lclients[i].nom)+' ')
            l.append(self.lclients[i].prenom+' ')
            l.append(str(self.lclients[i].age)+' ')
            l.append(str(self.lclients[i].address)+' ')
            l.append(str(self.lclients[i].adressmail.affichead())+' ')
            l.append(str(self.lclients[i].numphone)+' '+"\n")
        f.writelines(l)
        f.close()
    def fileinputclients(self):
        l=[]
        n=0
        l2=[]
        f=open(r"C:\Users\21653\Documents\fileclients.txt","r")
        l=f.readlines()
        for i in range(len(l)-1,-1,-1):
            l2=[]
            n=0
            for j in range(len(l[i])):
                if(l[i][j]==' '):
                    l2.append(l[i][n:j])
                    n=j+1
                if(j==len(l[i])-2):
                    break
            l[i]=l2
        for i in range(len(l)):
            self.ajouterclient(int(l[i][0]),l[i][1],l[i][2],int(l[i][3]),l[i][4],l[i][5],int(l[i][6]))
        f.close()
    def affichecl(self):
        for i in range(len(self.lclients)):
            self.lclients[i].affichec()
       
        
            
        
        
        
    