import fileparcv
import fileclients
import filedate
class locationcar:
    def __init__(self):
        self.cars=fileparcv.parccar()
        self.client=fileclients.clients()
        self.location=[]
        self.n=0
    def ajouterlocation(self,marq,color,jour,mois,annee,prix,cin,nom,prenom,age,address,adressmail,numphone,dureelocation):
        n=0
        m=0
        for i in range(len(self.cars.lcars)):
            if(self.cars.lcars[i].marq==marq and self.cars.lcars[i].color==color and self.cars.lcars[i].etat==0):
                break
            n=i+1
        if(n<len(self.cars.lcars)):
            for j in range(len(self.client.lclients)):
                if(self.client.lclients[j].cin==cin):
                    break
                m=j+1
            if(m>=len(self.client.lclients)):
                self.client.ajouterclient(cin,nom,prenom,age,address,adressmail,numphone)
            self.cars.lcars[n].changeetat()
            self.location.append({'locationnum':self.n,'clientcin':cin,'carmat':self.cars.lcars[n].mat,'datelocation':filedate.date(jour,mois,annee),'dureelocation':dureelocation,'montant':dureelocation*prix})
            self.n+=1
        else:
            print("pas de car trouvee")
    def supprimerlocation(self,cin,mat):
        n=0
        for i in range(len(self.location)):
            if(self.location[i]['clientcin']==cin and self.location[i]['carmat']== mat):
                break
            n=i+1
        if(n<len(self.location)):
            for j in range(len(self.cars.lcars)):
                if(self.cars.lcars[j].mat==mat):
                    self.cars.lcars[j].etat=0
                    break
            self.location.remove(self.location[n])
        else:
            print("location n est pas trouvee")
    def modifierdatelocation(self,cin,mat,datelocation):
        for i in range(len(self.location)):
            if(self.location[i]['clientcin']==cin and self.location[i]['carmat']== mat):
                break
        if(i<len(self.location)):
            self.location[i]['datelocation']=datelocation
        else:
            print("location n est pas trouvee")
    def modifierdureelocation(self,cin,mat,dureelocation):
        n=0
        for i in range(len(self.location)):
            if(self.location[i]['clientcin']==cin and self.location[i]['carmat']== mat):
                break
            n=i+1
        if(n<len(self.location)):
            self.location[n]['dureelocation']=dureelocation
        else:
            print("location n est pas trouvee")
    def recherchecin(self,cin):
        n=0
        l=[]
        for i in range(len(self.location)):
            if(self.location[i]['clientcin']==cin):
                print("le client trouvee avec cin:", self.location[i]['clientcin'], "le numero de location" ,self.location[i]['locationnum'])
                l.append(self.location[i])
                n=1
        if(n<1):
            return l
            print("location n est pas trouvee")
        return l
    def recherchemat(self,mat):
        n=0
        l=[]
        for i in range(len(self.location)):
            if(self.location[i]['carmat']==mat):
                print("le voiture trouvee avec mat:" ,self.location[i]['carmat'] ,"le numero de location", self.location[i]['locationnum'])
                l.append(self.location[i])
                n=1
        if(n<1):
            return l
            print("location n est pas trouvee")
        return l
    def recherchedate(self,date):
        n=0
        l=[]
        for i in range(len(self.location)):
            if(self.location[i]['datelocation'].daynumber(self.location[i]['datelocation'],date)==0):
                print("la date trouvee:" ,self.location[i]['datelocation'], "le numero de location" ,self.location[i]['locationnum'])
                l.append(self.location[i])
                n=1
        if(n<1):
            return l
            print("location n est pas trouvee")
        return l
    def recherchedureelocation(self,dureelocation):
        n=0
        l=[]
        for i in range(len(self.location)):
            if(self.location[i]['dureelocation']==dureelocation):
                print("la duree trouvee:" ,self.location[i]['dureelocation'], "le numero de location" ,self.location[i]['locationnum'])
                l.append(self.location[i])
                n=1
        if(n<1):
            return l
            print("location n est pas trouvee")
        return l
    def rechercheddate(self,date1,date2):
        n=0
        l=[]
        for i in range(len(self.location)):
            if(self.location[i]['datelocation'].daynumber(date1,self.location[i]['datelocation'])>0 and self.location[i]['datelocation'].daynumber(self.location[i]['datelocation'],date2)>0):
                print("la date trouvee:", self.location[i]['datelocation'] ,"le numero de location", self.location[i]['locationnum'])
                l.append(self.location[i])
                n=1
        if(n<1):
            return l
            print("location n est pas trouvee")
        return l
    def fileoutputlocation(self):
        l=[]
        f=open(r"C:\Users\21653\Documents\filelocation.txt","w")
        for i in range(len(self.location)):
            l.append(str(self.location[i]['locationnum'])+' ')
            l.append(str(self.location[i]['clientcin'])+' ')
            l.append(str(self.location[i]['carmat'])+' ')
            l.append(self.location[i]['datelocation'].affiched()+' ')
            l.append(str(self.location[i]['dureelocation'])+' ')
            l.append(str(self.location[i]['montant'])+' '+"\n")
        f.writelines(l)
        f.close()
    def fileinputlocation(self):
        l=[]
        n=0
        l2=[]
        f=open(r"C:\Users\21653\Documents\filelocation.txt","r")
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
            self.location.append({'locationnum':int(l[i][0]),'clientcin':int(l[i][1]),'carmat':int(l[i][2]),'datelocation':filedate.date(int(l[i][3]),int(l[i][4]),int(l[i][5])),'dureelocation':int(l[i][6]),'montant':int(l[i][6])})
        f.close()
    def affichel(self):
        for i in range(len(self.location)):
            print(self.location[i],self.location[i]['datelocation'].affiched())

        
        
        

        
            
        
        
        
        
            
            
        
        
                
        
        