import datetime
class date ():
    def __init__(self,jour,mois,annee,heure):
        if (self.validdateh(jour,mois,annee,heure)==1):
            self.jour=jour
            self.mois=mois
            self.annee=annee
            self.heure=heure
        else:
            print("date not valide")
    def __init__(self,jour,mois,annee):
        if (self.validdate(jour,mois,annee)==1):
            self.jour=jour
            self.mois=mois
            self.annee=annee
        else:
            print("date not valide")
    def validdate(self,jour,mois,annee):
        try:
            ndate=datetime.datetime(annee, mois, jour)
            if(ndate.year<1900):
                return 0
            return 1
        except ValueError:
            return 0
    def validdateh(self,jour,mois,annee,heure):
        try:
            newDate = datetime.datetime(annee, mois, jour,heure)
            return 1
        except ValueError:
            return 0
    def daynumber(self,date1,date2):
        d1=datetime.datetime(date1.annee,date1.mois,date1.jour)
        d2=datetime.datetime(date2.annee,date2.mois,date2.jour)
        return(d2-d1).days
    def yearsnumber(self):
        annee=2022
        mois=5
        jour=5
        d1=datetime.datetime(self.annee,self.mois,self.jour)
        d2=datetime.datetime(annee,mois,jour)
        return d2.year-d1.year
    def validddate(self,date):
        if(self.daynumber(self,date)>0):
            print("date valide")
        else:
            print("date1 superieur a date2")
    def affiched(self):
        return(str(self.jour)+' '+str(self.mois)+' '+str(self.annee))

        
d1=date(5,5,2000)
d2=date(10,5,2022)
print(d1.yearsnumber())
