import filev
import filedate
class parccar:
    def __init__(self):
        self.lcars=[]
    def ajoutecar(self,mat,marq,color,jour,mois,annee,prix):
        i=0
        while(i<len(self.lcars)):
            if(self.lcars[i].mat==mat):
                break
            i+=1
        if(i>=len(self.lcars)):
            self.lcars.append(filev.car(mat,marq,color,jour,mois,annee,prix))
        else:
            print("la voiture existe")
    def supprimercar(self,mat):
        i=0
        while(i<len(self.lcars)):
            if(self.lcars[i].mat==mat):
                break
            i+=1
        if(i<len(self.lcars)):
            self.lcars.remove(self.lcars[i])
        else:
            print("le voiture ne existe pas")
    def supprimermarq(self,marq):
        n=0
        l=0
        while(l<len(self.lcars)):
            i=l
            while(i<len(self.lcars)):
                if(self.lcars[i].marq==marq):
                    self.lcars.remove(self.lcars[i])
                    n=1
                    l=i
                    break
                i+=1
            l=i  
        if (n>0):
            print("remove success")
        else:
            print("marque n est pas trouvee")
    def supprimercarv(self):
        n=0
        l=0
        while(l<len(self.lcars)):
            i=l
            while(i<len(self.lcars)):
                if(self.lcars[i].date()>10):
                    self.lcars.remove(self.lcars[i])
                    n=1
                    l=i
                    break
                i+=1
            l=i
        if (n>0):
            print("remove success")
        else:
            print("cars n est pas trouvee")
            
    def modifierprix(self,mat,prix):
        n=0
        for i in range(len(self.lcars)):
            if(self.lcars[i].mat==mat):
                self.lcars[i].prix=prix
                break
            n=i+1
        if(n<len(self.lcars)):
            print("change success")
        else:
            print("le voiture n est pas trouvee")
    def modifiercouleur(self,mat,color):
        n=0
        for i in range(len(self.lcars)):
            if(self.lcars[i].mat==mat):
                self.lcars[i].color=color
                n=1
                break
        if(n>0):
            print("change success")
        else:
            print("le voiture n est pas trouvee")
    def recherchemat(self,mat):
        n=0
        l=[]
        for i in range(len(self.lcars)):
            if(self.lcars[i].mat==mat):
                l.append(self.lcars[i])
                break
            n=i+1
        if(n<len(self.lcars)):
            print("le voiture existe")
            return l
        else:
            return l
            print("le voiture n est pas trouvee")
    def recherchemarque(self,marq):
        n=0
        l=[]
        for i in range(len(self.lcars)):
            if(self.lcars[i].marq==marq):
                l.append(self.lcars[i])
                print("le car trouvee")
                n=1
        if(n>0):
            print("recherche success")
            return l
        else:
            return l
            print("le voiture n est pas trouvee")
    def recherchecolor(self,color):
        n=0
        l=[]
        for i in range(len(self.lcars)):
            if(self.lcars[i].color==color):
                l.append(self.lcars[i])
                print("le car trouvee")
                n=1
        if(n>0):
            print("recherche success")
            return l
        else:
            return l
            print("le voiture n est pas trouvee")
    def recherchedcar(self):
        n=0
        l=[]
        for i in range(len(self.lcars)):
            if(self.lcars[i].etat==0):
                print("le car trouvee avec mat:",self.lcars[i].mat)
                l.append(self.lcars[i])
                n=1
        if(n>0):
            print("recherche success")
            return l
        else:
            return l
            print("le voiture n est pas trouvee")
    def recherchelcar(self):
        n=0
        l=[]
        for i in range(len(self.lcars)):
            if(self.lcars[i].etat==1):
                print("le car trouvee avec mat:",self.lcars[i].mat)
                l.append(self.lcars[i])
                n=1
        if(n>0):
            print("recherche success")
            return l
        else:
            return l
            print("le voiture n est pas trouvee")
    def rechercheldcar(self,date1,date2):
        n=0
        l=[]
        for i in range(len(self.lcars)):
            if(self.lcars[i].dateachat.daynumber(date1,self.lcars[i].dateachat)>0 and self.lcars[i].dateachat.daynumber(self.lcars[i].dateachat,date2)>0):
                l.append(self.lcars[i])
                print("le car trouvee avec mat:",self.lcars[i].mat)
                n=1
        if(n>0):
            print("recherche success")
            return l
        else:
            return l
            print("le voiture n est pas trouvee")
    def fileoutputcars(self):
        l=[]
        f=open(r"C:\Users\21653\Documents\filecars.txt","w")
        for i in range(len(self.lcars)):
            l.append(str(self.lcars[i].mat)+' ')
            l.append(str(self.lcars[i].marq)+' ')
            l.append(self.lcars[i].color+' ')
            l.append(str(self.lcars[i].dateachat.affiched())+' ')
            l.append(str(self.lcars[i].prix)+' ')
            l.append(str(self.lcars[i].etat)+' '+"\n")
        f.writelines(l)
        f.close()
    def fileinputcars(self):
        l=[]
        n=0
        l2=[]
        f=open(r"C:\Users\21653\Documents\filecars.txt","r")
        l=f.readlines()
        print(l[0])
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
            self.ajoutecar(int(l[i][0]),l[i][1],l[i][2],int(l[i][3]),int(l[i][4]),int(l[i][5]),int(l[i][6]))
        f.close()
        
    def affiched(self):
        for i in range(len(self.lcars)):
            self.lcars[i].affichec()
       
        
            
        
        
        
        
        
        
        
                
        
        
                
        
        
        
        
        
            
        
