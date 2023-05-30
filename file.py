from  tkinter import *
from tkinter import colorchooser
from tkcalendar import DateEntry
import datetime
import fileaddress
import filedate
import filelocationv
from PIL import Image
from PIL import ImageTk
import time
from tkinter import tix
import tkinter as tk
import tkinter.ttk as tkk
l=["red","blue","white"]
lm=["marcedece","ferrarie","bmx"]
aa=filelocationv.locationcar()
class frames(Tk):
    def __init__(self,m):
        Tk.__init__(self)
        self.m=m
        self.champ={'nom':tk.StringVar(),'prenom':tk.StringVar(),'size':tk.IntVar(),
                   'type':tk.StringVar(),'value1':tk.StringVar(),'value2':tk.StringVar(),'value3':tk.StringVar(),'text':tk.StringVar(),
                   'choix':tk.StringVar()}
        self.v=tk.StringVar()
        self.l1=Label(self,text="nom",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
        self.t1=Entry(self,width=30,font="Arial",textvariable=self.v)
        self.t1.grid(row=1,column=2 )
        self.l2=Label(self,text="prenom",font="italic",bd=5).grid(row=2,sticky= W, padx=35 )
        self.t2=Entry(self,width=30,font="Arial 12 italic",textvariable=self.champ['prenom'])
        self.t2.grid(row=2,column=2 )
        self.l3=Label(self,text="size",font="italic",bd=5).grid(row=3,sticky= W, padx=35 )
        self.t3=Entry(self,width=30,font="Arial",textvariable=self.champ['size'])
        self.t3.grid(row=3,column=2 )
        self.l4=Label(self,text="type",font="italic",bd=5).grid(row=4,sticky= W, padx=35 )
        self.t4=Entry(self,width=30,font="Arial",textvariable=self.champ['type'])
        self.t4.grid(row=4,column=2 )
        self.cb1=tkk.Checkbutton(self,text="value1",variable=self.champ['value1'])
        self.cb1.grid(row=5)
        self.cb2=tkk.Checkbutton(self,text="value2",variable=self.champ['value2'])
        self.cb2.grid(row=5,column=2)
        self.cb3=tkk.Checkbutton(self,text="value3",variable=self.champ['value3'])
        self.cb3.grid(row=5,column=3)
        self.rb1=tkk.Radiobutton(self,text="text1",value="italic",variable=self.champ['text'])
        self.rb1.grid(row=6)
        self.rb2=tkk.Radiobutton(self,text="text2",variable=self.champ['text'])
        self.rb2.grid(row=6,column=2)
        self.c=tkk.Combobox(self,text="choice",font="Arial",values=l,textvariable=self.champ['choix'])
        self.c.grid(row=7,column=2)
        Button(self,text="retour",width=10,command=self.back).grid(row=7)
        Button(self,text="valider",width=10,command=self.valider).grid(row=8,column=3)
        for i in range(8):
            self.columnconfigure(i,weight=1,minsize=75)
            self.rowconfigure(i,weight=1,minsize=50)
    def start(self):
        self.mainloop()
    def back(self):
        self.withdraw()
        self.m.deiconify()
    def getp(self):
        self.champ['nom'].set(self.t1.get())
        self.champ['prenom'].set(self.t2.get())
        try:
            self.champ['size'].set(self.t3.get())
        except:
            messagebox.showerror("error message", "la valeur not int")
        self.champ['type'].set(self.t4.get())
        self.champ['value1'].set(self.cb1.state())
        self.champ['value2'].set(self.cb2.state())
        self.champ['value3'].set(self.cb3.state())
        self.champ['text'].set(self.rb1.state())
        self.champ['choix'].set(self.c.get())
        
    def valider(self):
        self.f=Tk()
        self.ff=tk.Frame(self.f)
        Label(self.ff,text="votre information",font="Arial 14 bold",bd=5).pack(pady=5)
        self.getp()
        for v,k in self.champ.items():
            Label(self.ff,text=v+':',font="italic",bd=5).pack()
            Label(self.ff,text=k.get(),font="italic",bd=5).pack()
        self.ff.pack()
        r=messagebox.askyesno("confirmation", "sure")
        if(r==True):
            self.f.destroy()
            self.destroy()
        if(r==False):
            self.f.destroy()
        self.f.mainloop()
class carframe(tix.Tk):
    def __init__(self,m):
        tix.Tk.__init__(self)
        self.m=m
        self.f=Frame(self,bg="green",borderwidth=3,relief="groove",highlightbackground="white",highlightthickness=4)
        self.config(bg="#13a8ac")
        t4=tix.Balloon(self)
        t5=tix.Balloon(self)
        t6=tix.Balloon(self)
        t7=tix.Balloon(self)
        t8=tix.Balloon(self)
        Label(self,text="car information",font="Arial 40 bold",bd=5,bg="green").pack()
        self.champ={'mat':tk.IntVar(),'marq':tk.StringVar(),'color':tk.StringVar(),
                   'jour':tk.IntVar(),'mois':tk.IntVar(),'annee':tk.IntVar(),'prix':tk.IntVar()}
        self.l1=Label(self.f,text="mat:",fg="#13a8ac",font="Arial 14 italic",bd=5,bg="green").grid(row=1,sticky= W, padx=35 )
        self.t1=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t1.grid(row=1,column=2 )
        self.l2=Label(self.f,text="date d achat :",fg="#13a8ac",font="Arial 14 italic",bd=5,bg="green").grid(row=2,sticky= W, padx=35 )
        self.t2=DateEntry(self.f,width=28,font="Arial 12 italic",background="green",locale="en_US",date_pattern='dd/mm/y',highlightthickness=2)
        self.t2.grid(row=2,column=2 )
        self.l3=Label(self.f,text="prix",fg="#13a8ac",font="Arial 14 italic",bd=5,bg="green").grid(row=3,sticky= W, padx=35 )
        self.t3=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t3.grid(row=3,column=2 )
        self.cm=tkk.Combobox(self.f,text="marq",font="Arial",values=lm)
        self.cm.grid(row=4,column=1)
        self.bm=Button(self.f,text="+add",bg="white",width=10,command=self.fmarq).grid(row=4,column=2)
        self.c=tkk.Combobox(self.f,text="color",font="Arial",values=l)
        self.c.grid(row=4,column=3)
        self.bc=Button(self.f,text="+add",bg="white",width=10,command=self.fcolor).grid(row=4,column=4)
        self.le=Label(self.f,text="",font="italic",bd=5,foreground="red")
        Button(self.f,text="retour",width=10,bg="white",command=self.back).grid(row=5)
        Button(self.f,text="valider",width=10,bg="white",command=self.valider).grid(row=5,column=3)
        self.f.pack(padx=20,pady=20)
        t4.bind_widget(self.t1,balloonmsg="matricule de voiture:entier de 8 chiffre ")
        t5.bind_widget(self.t2,balloonmsg="date d achat:date suivant format jj/mm/aaaa ")
        t6.bind_widget(self.t3,balloonmsg="prix de voiture:entier de 3 chiffre ")
        t7.bind_widget(self.cm,balloonmsg="marque de voiture")
        t8.bind_widget(self.c,balloonmsg="color de voiture ")
        for i in range(8):
            self.columnconfigure(i,weight=1,minsize=75)
            self.rowconfigure(i,weight=1,minsize=50)
    def start(self):
        self.mainloop()
    def back(self):
        self.withdraw()
        self.m.deiconify()
    def getp(self):
        t=1
        try:
            float(self.t1.get())
            if(len(str(self.t1.get()))==8):
                self.champ['mat'].set(self.t1.get())
            else:
                raise ValueError
            self.t1.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t1.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur mat not int")
        try:
            float(self.t3.get())
            self.champ['prix'].set(self.t3.get())
            self.t3.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t3.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur de prix not int")
        try:
            v=self.t2.get()
            datetime.datetime.strptime(v,'%d/%m/%Y')
            self.t2.configure(highlightbackground="gray",highlightcolor="gray")
            jour,mois,annee=v.split('/')
            self.champ['jour'].set(jour)
            self.champ['mois'].set(mois)
            self.champ['annee'].set(annee)
        except ValueError:
            t=0
            self.t2.configure(highlightbackground="red",highlightcolor="red")
        try:
            if(self.c.get()==""):
                raise ValueError
            self.champ['color'].set(self.c.get())
        except ValueError:
            t=0
            self.le['text']+="color not selected"
            self.le.grid(row=5,column=2,sticky= W, padx=35 )
        try:
            if(self.cm.get()==""):
                raise ValueError
            self.champ['marq'].set(self.cm.get())
        except ValueError:
            t=0
            self.le['text']+="marq not selected"
            self.le.grid(row=5,column=2,sticky= W, padx=35 )
        return t
        
    def valider(self):
        if(self.getp()):
            if(len(aa.cars.recherchemat(self.champ['mat'].get()))!=1):
                self.f=Tk()
                self.ff=tk.Frame(self.f)
                l1=[]
                l2=[]
                Label(self.ff,text="votre information",font="Arial 14 bold",bd=5).pack(pady=5)
                aa.cars.ajoutecar(self.champ['mat'].get(),self.champ['marq'].get(),self.champ['color'].get(),self.champ['jour'].get(),self.champ['mois'].get(),self.champ['annee'].get(),self.champ['prix'].get())
                aa.cars.affiched()
                for v,k in self.champ.items():
                    Label(self.ff,text=v+':',font="italic",bd=5).pack()
                    Label(self.ff,text=k.get(),font="italic",bd=5).pack()
                self.ff.pack()
                for v,k in self.champ.items():
                    l1.append(v)
                    l2.append(k.get())
                self.tf=tableinfo(l1,l2,7)
                self.tf.starttable()
                r=messagebox.askyesno("confirmation", "sure")
                if(r==True):
                    self.f.destroy()
                    self.destroy()
                if(r==False):
                    self.f.destroy()
                self.tf.starttable()
                self.f.mainloop()
            else:
                messagebox.showerror("error message", "la car existe ")
    def fmarq(self):
        self.fm=framemarque(self,self.cm)
        self.withdraw()
        self.fm.start()
    def fcolor(self):
        self.fc=colorchooser.askcolor(title ="add new color")
        self.c['values']+=(self.fc,)
class framemarque(Tk):
    def __init__(self,m,c):
        Tk.__init__(self)
        self.m=m
        self.c=c
        self.nmarq="eeee"
        self.l1=Label(self,text=" new marque",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
        self.t1=Entry(self,width=30,font="Arial")
        self.t1.grid(row=1, column=2)
        Button(self,text="valider",width=10,command=self.ajoutmarque).grid(row=2,column=3)
    def ajoutmarque(self):
        self.nmarq=self.t1.get()
        if (self.nmarq not in lm):
            self.c['values']+=(self.nmarq,)
        messagebox.showinfo("infomation sur la  new marque", "new marque ajouter")
        self.destroy()
        self.m.deiconify()
         
    def getnmarque(self):
        return self.c
    def start(self):
        self.mainloop()
    
class clientframe(tix.Tk):
    def __init__(self,m):
        tix.Tk.__init__(self)
        self.m=m
        self.f=Frame(self,bg="orange",borderwidth=3,relief="groove",highlightbackground="white",highlightthickness=4)
        self.config(bg="gold")
        t4=tix.Balloon(self)
        t5=tix.Balloon(self)
        t6=tix.Balloon(self)
        t7=tix.Balloon(self)
        t8=tix.Balloon(self)
        t9=tix.Balloon(self)
        t10=tix.Balloon(self)
        Label(self,text="client information",bg="orange",font="Arial 40 italic",bd=5).pack()
        self.champ={'cin':tk.IntVar(),'nom':tk.StringVar(),'prenom':tk.StringVar(),
                   'age':tk.IntVar(),'address':tk.StringVar(),'adressmail':tk.StringVar(),'numphone':tk.StringVar()}
        self.l1=Label(self.f,text="cin:",bg="orange",fg="gold",font="Arial 14 italic",bd=5).grid(row=1,sticky= W, padx=35 )
        self.t1=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t1.grid(row=1,column=2 )
        self.l2=Label(self.f,text="nom:",bg="orange",fg="gold",font="Arial 14 italic",bd=5).grid(row=2,sticky= W, padx=35 )
        self.t2=Entry(self.f,width=30,font="Arial 12 italic",highlightthickness=2)
        self.t2.grid(row=2,column=2 )
        self.l3=Label(self.f,text="prenom:",bg="orange",fg="gold",font="Arial 14 italic",bd=5).grid(row=3,sticky= W, padx=35 )
        self.t3=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t3.grid(row=3,column=2 )
        self.l4=Label(self.f,text="age:",bg="orange",fg="gold",font="Arial 14 italic",bd=5).grid(row=4,sticky= W, padx=35 )
        self.t4=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t4.grid(row=4,column=2 )
        self.l5=Label(self.f,text="address:",bg="orange",fg="gold",font="Arial 14 italic",bd=5).grid(row=5,sticky= W, padx=35 )
        self.t5=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t5.grid(row=5,column=2 )
        self.l6=Label(self.f,text="addressmail:",bg="orange",fg="gold",font="Arial 14 italic",bd=5).grid(row=6,sticky= W, padx=35 )
        self.t6=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t6.grid(row=6,column=2 )
        self.l7=Label(self.f,text="numphone:",bg="orange",fg="gold",font="Arial 14 italic",bd=5).grid(row=7,sticky= W, padx=35 )
        self.t7=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t7.grid(row=7,column=2 )
        Button(self.f,text="retour",width=10,command=self.back).grid(row=8)
        Button(self.f,text="valider",width=10,command=self.valider).grid(row=8,column=3)
        self.f.pack(padx=20,pady=20)
        t4.bind_widget(self.t1,balloonmsg="cin de client:entier de 8 chiffre ")
        t5.bind_widget(self.t2,balloonmsg="nom de client ")
        t6.bind_widget(self.t3,balloonmsg="prenom de client ")
        t7.bind_widget(self.t4,balloonmsg="age de client:entier de 2 chiffre")
        t8.bind_widget(self.t5,balloonmsg="addresse de client")
        t9.bind_widget(self.t6,balloonmsg="addresse mail de client ")
        t10.bind_widget(self.t7,balloonmsg="numero de telephone de client : entier de 8 chiffre")
        for i in range(8):
            self.columnconfigure(i,weight=1,minsize=75)
            self.rowconfigure(i,weight=1,minsize=50)
    def start(self):
        self.mainloop()
    def back(self):
        self.withdraw()
        self.m.deiconify()
    def getp(self):
        t=1
        try:
            float(self.t1.get())
            if(len(str(self.t1.get()))==8):
                self.champ['cin'].set(self.t1.get())
            else:
                raise ValueError
            self.t1.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t1.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur cin  not int")
        try:
            if(len(str(self.t3.get()))<2 ):
                raise ValueError
            if(self.t3.get()==" "):
                raise ValueError
            self.champ['prenom'].set(self.t3.get())
            self.t3.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t3.configure(highlightbackground="red",highlightcolor="red")
        try:
            if(len(str(self.t2.get()))<2):
                raise ValueError
            if(self.t2.get()==" "):
                raise ValueError
            self.champ['nom'].set(self.t2.get())
            self.t2.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t2.configure(highlightbackground="red",highlightcolor="red")
        try:
            float(self.t4.get())
            if(len(str(self.t4.get()))<2):
                raise ValueError
            self.champ['age'].set(self.t4.get())
            self.t4.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t4.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur age not int")
        try:
            if(len(str(self.t5.get()))<10):
                raise ValueError
            if(str(self.t5.get())=="   "):
                raise ValueError
            self.champ['address'].set(self.t5.get())
            self.t5.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t5.configure(highlightbackground="red",highlightcolor="red")
        try:
            if(len(str(self.t6.get()))<10):
                raise ValueError
            if(str(self.t6.get())=="    "):
                raise ValueError
            d=fileaddress.addressc(self.t6.get())
            self.champ['adressmail'].set(self.t6.get())
            self.t6.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t6.configure(highlightbackground="red",highlightcolor="red")
        try:
            float(self.t7.get())
            if(len(str(self.t7.get()))!=8):
                raise ValueError
            self.champ['numphone'].set(self.t7.get())
            self.t7.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t7.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur numphone  not int")
        return t
    def valider(self):
        if(self.getp()):
            if(len(aa.client.recherchecin(self.champ['cin'].get()))!=1):
                self.f=Tk()
                self.ff=tk.Frame(self.f)
                l1=[]
                l2=[]
                Label(self.ff,text="votre information",font="Arial 14 bold",bd=5).pack(pady=5)
                aa.client.ajouterclient(self.champ['cin'].get(),self.champ['nom'].get(),self.champ['prenom'].get(),self.champ['age'].get(),self.champ['address'].get(),self.champ['adressmail'].get(),self.champ['numphone'].get())
                aa.client.affichecl()
                for v,k in self.champ.items():
                    Label(self.ff,text=v+':',font="italic",bd=5).pack()
                    Label(self.ff,text=k.get(),font="italic",bd=5).pack()
                self.ff.pack()
                for v,k in self.champ.items():
                    l1.append(v)
                    l2.append(k.get())
                self.tf=tableinfo(l1,l2,7)
                self.tf.starttable()
                r=messagebox.askyesno("confirmation", "sure")
                if(r==True):
                    self.f.destroy()
                    self.destroy()
                if(r==False):
                    self.f.destroy()
                self.f.mainloop()
            else:
                messagebox.showerror("error message", "le client trouvee")
class locationframe(tix.Tk):
    def __init__(self,m):
        tix.Tk.__init__(self)
        self.f=Frame(self,bg="#800040",borderwidth=3,relief="groove",highlightbackground="white",highlightthickness=4)
        self.config(bg="#b8b872")
        t4=tix.Balloon(self)
        t5=tix.Balloon(self)
        t6=tix.Balloon(self)
        t7=tix.Balloon(self)
        t8=tix.Balloon(self)
        t9=tix.Balloon(self)
        self.champ={'cin':tk.IntVar(),'marque':tk.StringVar(),'color':tk.StringVar(),
                   'jour':tk.IntVar(),'mois':tk.IntVar(),'annee':tk.IntVar(),'prix':tk.IntVar(),
                    'dureelocation':tk.IntVar()}
        Label(self,text="location information",bg="#800040",font="Arial 40 bold",bd=5).pack()
        self.l1=Label(self.f,text="cin:",bg="#800040",fg="#b8b872",font="Arial 14 italic",bd=5).grid(row=1,sticky= W, padx=35 )
        self.t1=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t1.grid(row=1,column=2 )
        self.l2=Label(self.f,text="date location:",bg="#800040",fg="#b8b872",font="Arial 14 italic",bd=5).grid(row=2,sticky= W, padx=35 )
        self.t2=DateEntry(self.f,width=28,background="#800040",locale="en_US",date_pattern='dd/mm/y',font="Arial 12 italic",highlightthickness=2)
        self.t2.grid(row=2,column=2 )
        self.l3=Label(self.f,text="prix",bg="#800040",fg="#b8b872",font="Arial 14 italic",bd=5).grid(row=3,sticky= W, padx=35 )
        self.t3=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t3.grid(row=3,column=2 )
        self.l4=Label(self.f,text="marque",bg="#800040",fg="#b8b872",font=" Arial 14 italic",bd=5).grid(row=4,sticky= W, padx=35 )
        self.t4=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t4.grid(row=4,column=2 )
        self.l5=Label(self.f,text="color",bg="#800040",fg="#b8b872",font="Arial 14 italic",bd=5).grid(row=5,sticky= W, padx=35 )
        self.t5=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t5.grid(row=5,column=2 )
        self.l6=Label(self.f,text="duree location",bg="#800040",fg="#b8b872",font="Arial 14 italic",bd=5).grid(row=6,sticky= W, padx=35 )
        self.t6=Entry(self.f,width=30,font="Arial",highlightthickness=2)
        self.t6.grid(row=6,column=2 )
        Button(self.f,text="retour",width=10,bg="white",command=self.back).grid(row=7)
        Button(self.f,text="valider",width=10,bg="white",command=self.valider).grid(row=7,column=3)
        self.f.pack(padx=20,pady=20)
        t4.bind_widget(self.t1,balloonmsg="cin de client:entier de 8 chiffre ")
        t5.bind_widget(self.t2,balloonmsg="date de location :date suivant format jj/mm/aaaa ")
        t6.bind_widget(self.t3,balloonmsg="prix de location: entier de 3 chiffre")
        t7.bind_widget(self.t4,balloonmsg="marque de voiture")
        t8.bind_widget(self.t5,balloonmsg="color de voiture")
        t9.bind_widget(self.t6,balloonmsg="duree de location : entier  ")
        for i in range(8):
            self.columnconfigure(i,weight=1,minsize=75)
            self.rowconfigure(i,weight=1,minsize=50)
    def start(self):
        self.mainloop()
    def back(self):
        self.withdraw()
        self.m.deiconify()
    def getp(self):
        t=1
        try:
            float(self.t1.get())
            if(len(str(self.t1.get()))!=8):
                raise ValueError
            self.champ['cin'].set(self.t1.get())
            self.t1.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t1.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur cin  not int")
        try:
            float(self.t3.get())
            if(len(str(self.t3.get()))<3):
                raise ValueError
            self.champ['prix'].set(self.t3.get())
            self.t3.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t3.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur prix  not int")
        try:
            v=self.t2.get()
            datetime.datetime.strptime(v,'%d/%m/%Y')
            self.t2.configure(highlightbackground="gray",highlightcolor="gray")
            jour,mois,annee=v.split('/')
            self.champ['jour'].set(jour)
            self.champ['mois'].set(mois)
            self.champ['annee'].set(annee)
        except ValueError:
            t=0
            self.t2.configure(highlightbackground="red",highlightcolor="red")
        try:
            if(self.t4.get() not in lm):
                raise ValueError
            self.champ['marque'].set(self.t4.get())
            self.t4.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t4.configure(highlightbackground="red",highlightcolor="red")
        try:
            if(self.t5.get() not in l):
                raise ValueError
            self.champ['color'].set(self.t5.get())
            self.t5.configure(highlightbackground="gray",highlightcolor="gray")
            
        except ValueError:
            t=0
            self.t5.configure(highlightbackground="red",highlightcolor="red")
        try:
            float(self.t6.get())
            self.champ['dureelocation'].set(self.t6.get())
            self.t6.configure(highlightbackground="gray",highlightcolor="gray")
        except ValueError:
            t=0
            self.t6.configure(highlightbackground="red",highlightcolor="red")
            messagebox.showerror("error message", "la valeur numphone  not int")
        return t
    def valider(self):
        if(self.getp()):
            if(len(aa.recherchecin(self.champ['cin'].get())!=1)and len(recherchemat(self.champ['mat'].get()))!=1):
                self.f=Tk()
                self.ff=tk.Frame(self.f)
                l1=[]
                l2=[]
                Label(self.ff,text="votre information",font="Arial 14 bold",bd=5).pack(pady=5)
                l=aa.client.recherchecin(self.champ['cin'].get())
                if(len(l)==1):
                    if(aa.n>0):
                        aa.ajouterlocation(self.champ['marque'].get(),self.champ['color'].get(),self.champ['jour'].get(),self.champ['mois'].get(),self.champ['annee'].get(),self.champ['prix'].get(),self.champ['cin'].get(),l[0].nom,l[0].prenom,l[0].age,l[0].address,l[0].adressmail,l[0].numphone,self.champ['dureelocation'].get())
                    else:
                        messagebox.showerror("error message", "pas de car trouvee")
                else:
                    lc=clientframe(self)
                    lc.start()
                for v,k in self.champ.items():
                    Label(self.ff,text=v+':',font="italic",bd=5).pack()
                    Label(self.ff,text=k.get(),font="italic",bd=5).pack()
                self.ff.pack()
                for v,k in self.champ.items():
                    l1.append(v)
                    l2.append(k.get())
                self.tf=tableinfo(l1,l2,6)
                self.tf.starttable()
                r=messagebox.askyesno("confirmation", "sure")
                if(r==True):
                    self.f.destroy()
                    self.destroy()
                if(r==False):
                    self.f.destroy()
                self.f.mainloop()
            else:
                messagebox.showerror("error message", "location trouvee")
                

class framed(Tk):
    def __init__(self,m,l):
        Tk.__init__(self)
        self.m=m
        self.l=l
        self.config(bg="orange")
        if(self.l=="cinmat"):
            self.l1=Label(self,text="cin",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t1.grid(row=1, column=2)
            self.l2=Label(self,text="mat",font="italic",bd=5).grid(row=2,sticky= W, padx=35 )
            self.t2=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t2.grid(row=2, column=2)
        else:
            self.l1=Label(self,text=self.l,font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t1.grid(row=1, column=2)
        Button(self,text="valider",width=10,command=self.search).grid(row=2,column=3)
    def search(self):
        if(self.l=="mat"):
            try:
                aa.cars.supprimercar(int(self.t1.get()))
                aa.cars.affiched()
            except ValueError:
                self.t1.configure(highlightbackground="red",highlightcolor="red")
        if(self.l=="marq"):
            try:
                aa.cars.supprimermarq(self.t1.get())
                aa.cars.affiched()
            except ValueError:
                self.t1.configure(highlightbackground="red",highlightcolor="red")
        if(self.l=="cin"):
            try:
                aa.client.supprimerclient(int(self.t1.get()))
                aa.client.affichecl()
            except ValueError:
                self.t1.configure(highlightbackground="red",highlightcolor="red")
        if(self.l=="cinmat"):
            try:
                aa.supprimerlocation(int(self.t1.get()),int(self.t2.get()))
                aa.affichel()
            except ValueError:
                self.t1.configure(highlightbackground="red",highlightcolor="red")
        messagebox.showinfo("infomation sur sup", "serach result")
        self.destroy()
    def start(self):
        self.mainloop()
class framedd(Tk):
    def __init__(self,m,l):
        Tk.__init__(self)
        self.m=m
        self.l=l
        self.config(bg="orange")
        if(self.l=="date"):
            self.l1=Label(self,text="cin",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t1.grid(row=1, column=2)
            self.l2=Label(self,text="mat",font="italic",bd=5).grid(row=2,sticky= W, padx=35 )
            self.t2=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t2.grid(row=2, column=2)
            self.l3=Label(self,text=self.l,font="italic",bd=5).grid(row=3,sticky= W, padx=35 )
            self.t3=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t3.grid(row=3, column=2)
        if(self.l=="dureelocation"):
            self.l1=Label(self,text="cin",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t1.grid(row=1, column=2)
            self.l2=Label(self,text="mat",font="italic",bd=5).grid(row=2,sticky= W, padx=35 )
            self.t2=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t2.grid(row=2, column=2)
            self.l3=Label(self,text=self.l,font="italic",bd=5).grid(row=3,sticky= W, padx=35 )
            self.t3=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t3.grid(row=3, column=2)
        if(self.l!="date"and self.l!="dureelocation"):
            self.l1=Label(self,text="mat",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t1.grid(row=1, column=2)
            self.l2=Label(self,text=self.l,font="italic",bd=5).grid(row=2,sticky= W, padx=35 )
            self.t2=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t2.grid(row=2, column=2)
        
        Button(self,text="valider",width=10,command=self.search).grid(row=2,column=3)
    def search(self):
        if(self.l=="prix"):
            aa.cars.modifierprix(int(self.t1.get()),int(self.t2.get()))
            aa.cars.affiched()
        if(self.l=="color"):
            aa.cars.modifiercouleur(int(self.t1.get()),self.t2.get())
            aa.cars.affiched()
        if(self.l=="address"):
            aa.client.modifieradresse(int(self.t1.get()),self.t2.get())
            aa.client.affichecl()
        if(self.l=="numphone"):
            aa.client.modifiernumphone(int(self.t1.get()),int(self.t2.get()))
            aa.client.affichecl()
        if(self.l=="adressemail"):
            aa.client.modifieradressemail(int(self.t1.get()),self.t2.get())
            aa.client.affichecl()
        if(self.l=="dureelocation"):
            aa.modifierdureelocation(int(self.t1.get()),int(self.t2.get()),int(self.t3.get()))
            aa.affichel()
        if(self.l=="date"):
            t=1
            try:
                v=self.t3.get()
                datetime.datetime.strptime(v,'%d/%m/%Y')
                self.t3.configure(highlightbackground="gray",highlightcolor="gray")
                jour,mois,annee=v.split('/')
                d1=filedate.date(int(jour),int(mois),int(annee))
            except ValueError:
                t=0
                self.t3.configure(highlightbackground="red",highlightcolor="red")
            if(t==1):
                aa.modifierdatelocation(int(self.t1.get()),self.t2.get(),d1)
                aa.affichel()
        messagebox.showinfo("infomation sur modification", "serach result")
        self.destroy()
    def start(self):
        self.mainloop()     
class framesearch(Tk):
    def __init__(self,m,l):
        Tk.__init__(self)
        self.m=m
        self.l=l
        self.config(bg="orange")
        if(self.l=="date"):
            self.l1=Label(self,text="date1",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t1.grid(row=1, column=2)
            self.l2=Label(self,text="date2",font="italic",bd=5).grid(row=2,sticky= W, padx=35 )
            self.t2=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t2.grid(row=2, column=2)
        if(self.l=="datedelocation"):
            self.l1=Label(self,text="date1",font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t1.grid(row=1, column=2)
            self.l2=Label(self,text="date2",font="italic",bd=5).grid(row=2,sticky= W, padx=35 )
            self.t2=Entry(self,width=30,font="Arial",highlightthickness=2)
            self.t2.grid(row=2, column=2)
        else:
            self.l1=Label(self,text=self.l,font="italic",bd=5).grid(row=1,sticky= W, padx=35 )
            self.t1=Entry(self,width=30,font="Arial")
            self.t1.grid(row=1, column=2)
        Button(self,text="valider",width=10,command=self.search).grid(row=2,column=3)
    def search(self):
        if(self.l=="mat"):
            self.td=tableinfo2(["mat","marq","color","date","prix","etat"],aa.cars.recherchemat(int(self.t1.get())))
            self.td.starttable()
        if(self.l=="marq"):
            self.td=tableinfo2(["mat","marq","color","date","prix","etat"],aa.cars.recherchemarque(self.t1.get()))
            self.td.starttable()
        if(self.l=="color"):
            self.td=tableinfo2(["mat","marq","color","date","prix","etat"], aa.cars.recherchecolor(self.t1.get()))
            self.td.starttable()
        if(self.l=="cin"):
            self.td=tableinfo2(["cin","nom","prenom","age","addresse","adressemail","numphone"], aa.client.recherchecin(int(self.t1.get())))
            self.td.starttable()
        if(self.l=="clientcin"):
            self.td=tableinfo2(["locationnum","clientcin","carmat","datelocation","dureelocation","montant"], aa.recherchecin(int(self.t1.get())))
            self.td.starttable()
        if(self.l=="carmat"):
            self.td=tableinfo2(["locationnum","clientcin","carmat","datelocation","dureelocation","montant"], aa.recherchemat(int(self.t1.get())))
            self.td.starttable()
        if(self.l=="locationdate"):
            t=1
            try:
                v=self.t1.get()
                datetime.datetime.strptime(v,'%d/%m/%Y')
                self.t1.configure(highlightbackground="gray",highlightcolor="gray")
                jour,mois,annee=v.split('/')
                d1=filedate.date(int(jour),int(mois),int(annee))
            except ValueError:
                t=0
                self.t1.configure(highlightbackground="red",highlightcolor="red")
            if(t==1):
                self.td=tableinfo2(["locationnum","clientcin","carmat","datelocation","dureelocation","montant"], aa.recherchedate(d1))
                self.td.starttable()
        if(self.l=="dureelocation"):
            self.td=tableinfo2(["locationnum","clientcin","carmat","datelocation","dureelocation","montant"], aa.recherchedureelocation(int(self.t1.get())))
            self.td.starttable()
        if(self.l=="datedelocation"):
            t=1
            try:
                v=self.t1.get()
                datetime.datetime.strptime(v,'%d/%m/%Y')
                self.t2.configure(highlightbackground="gray",highlightcolor="gray")
                jour,mois,annee=v.split('/')
                d1=filedate.date(int(jour),int(mois),int(annee))
            except ValueError:
                t=0
                self.t1.configure(highlightbackground="red",highlightcolor="red")
            try:
                v=self.t2.get()
                datetime.datetime.strptime(v,'%d/%m/%Y')
                self.t2.configure(highlightbackground="gray",highlightcolor="gray")
                jour2,mois2,annee2=v.split('/')
                d2=filedate.date(int(jour2),int(mois2),int(annee2))
            except ValueError:
                t=0
                self.t2.configure(highlightbackground="red",highlightcolor="red")
            if(t==1):
                self.td=tableinfo2(["locationnum","clientcin","carmat","datelocation","dureelocation","montant"], aa.rechercheddate(d1,d2))
                self.td.starttable()
        if(self.l=="date"):
            t=1
            try:
                v=self.t1.get()
                datetime.datetime.strptime(v,'%d/%m/%Y')
                self.t1.configure(highlightbackground="gray",highlightcolor="gray")
                jour,mois,annee=v.split('/')
                d1=filedate.date(int(jour),int(mois),int(annee))
            except ValueError:
                t=0
                self.t1.configure(highlightbackground="red",highlightcolor="red")
            try:
                v=self.t2.get()
                datetime.datetime.strptime(v,'%d/%m/%Y')
                self.t2.configure(highlightbackground="gray",highlightcolor="gray")
                jour2,mois2,annee2=v.split('/')
                d2=filedate.date(int(jour2),int(mois2),int(annee2))
            except ValueError:
                t=0
                self.t2.configure(highlightbackground="red",highlightcolor="red")
            if(t==1):
                self.td=tableinfo2(["mat","marq","color","date","prix","etat"], aa.cars.rechercheldcar(d1,d2))
                self.td.starttable()
        messagebox.showinfo("infomation sur search", "serach result")
        self.destroy()
    def startsearch(self):
        self.mainloop()
        
class menus(Toplevel):
    def __init__(self,m):
        Toplevel.__init__(self)
        self.m=m
        self.geometry("1500x900")
        self.mbar=Menu(self,background="blue",activebackground="blue")
        self.appmenu=Menu(self.mbar,tearoff=0)
        self.appmenu.add_command(label="recherche and affiche")
        self.appmenu.add_separator()
        self.mbar.add_cascade(label="parccar",menu=self.appmenu)
        self.appmenua=Menu(self.appmenu,tearoff=0)
        self.appmenua.add_command(label="ajouter",command=self.framec)
        self.appmenu.add_cascade(label="car update",menu=self.appmenua)
        self.appmenua2=Menu(self.appmenua,tearoff=0)
        self.appmenua.add_command(label="ajoute1",command=self.frame1)
        self.appmenua2.add_command(label="supprimer car",command=self.framedd)
        self.appmenua2.add_command(label="supprimer marque car",command=self.framedd1)
        self.appmenua2.add_command(label="supprimer cars",command=self.framedd2)
        self.appmenua.add_cascade(label="supprimer car",menu=self.appmenua2)
        self.appmenum=Menu(self.appmenua,tearoff=0)
        self.appmenum.add_command(label="modifier prix",command=self.framedd3)
        self.appmenum.add_command(label="modifier color",command=self.framedd4)
        self.appmenua.add_cascade(label="modifier car",menu=self.appmenum)
        self.appmenuar=Menu(self.appmenu,tearoff=0)
        self.appmenuar.add_command(label="affiche cars",command=self.opentable)
        self.appmenuar.add_command(label="recherche mat",command=self.search)
        self.appmenuar.add_command(label="recherche marque",command=self.search2)
        self.appmenuar.add_command(label="recherche color",command=self.search3)
        self.appmenuar.add_command(label="recherche dcar",command=self.search4)
        self.appmenuar.add_command(label="recherche lcar",command=self.search5)
        self.appmenuar.add_command(label="recherche lddcar",command=self.search6)
        self.appmenu.add_cascade(label="recherche and affiche",menu=self.appmenuar)
        self.appmenuc=Menu(self.mbar,tearoff=0)
        self.appmenuca=Menu(self.appmenuc,tearoff=0)
        self.appmenuca.add_command(label="ajouter client",command=self.frameclient)
        self.appmenuca.add_command(label="supprimer client",command=self.framedd5)
        self.appmenuca2=Menu(self.appmenuca,tearoff=0)
        self.appmenuca2.add_command(label="modifier addresse",command=self.framedd6)
        self.appmenuca2.add_command(label="modifier numphone",command=self.framedd7)
        self.appmenuca2.add_command(label="modifier adressemail",command=self.framedd8)
        self.appmenuca.add_cascade(label="modifier client",menu=self.appmenuca2)
        self.appmenuc.add_cascade(label="client update",menu=self.appmenuca)
        self.appmenucr=Menu(self.appmenuc,tearoff=0)
        self.appmenucr.add_command(label="affiche client",command=self.opentable2)
        self.appmenucr.add_command(label="recherche cin",command=self.search7)
        self.appmenuc.add_cascade(label="recherche and affiche client",menu=self.appmenucr)
        self.mbar.add_cascade(label="mclients",menu=self.appmenuc)
        self.appmenul=Menu(self.mbar,tearoff=0)
        self.appmenula=Menu(self.appmenul,tearoff=0)
        self.appmenula.add_command(label="ajouter location",command=self.framelocation)
        self.appmenula.add_command(label="supprimer location",command=self.framedd9)
        self.appmenula2=Menu(self.appmenula,tearoff=0)
        self.appmenula2.add_command(label="modifier date location",command=self.framedd10)
        self.appmenula2.add_command(label="modifier duree location",command=self.framedd11)
        self.appmenula.add_cascade(label="modifier location",menu=self.appmenula2)
        self.appmenul.add_cascade(label="location update",menu=self.appmenula)
        self.appmenulr=Menu(self.appmenul,tearoff=0)
        self.appmenulr.add_command(label="affiche location",command=self.opentable3)
        self.appmenulr.add_command(label="recherche cin",command=self.search8)
        self.appmenulr.add_command(label="recherche mat",command=self.search9)
        self.appmenulr.add_command(label="recherche date",command=self.search10)
        self.appmenulr.add_command(label="recherche dureelocation",command=self.search11)
        self.appmenulr.add_command(label="recherche dateddlocation",command=self.search12)
        self.appmenul.add_cascade(label="recherche and affiche client",menu=self.appmenulr)
        self.mbar.add_cascade(label="mlocation",menu=self.appmenul)
        self.appmenuf=Menu(self.mbar,tearoff=0)
        self.appmenuf.add_command(label="enregister file car",command=self.enregisterfilecar)
        self.appmenuf.add_command(label="open file car",command=self.chargementfilecar)
        self.appmenuf.add_command(label="enregister file client",command=self.enregisterfileclients)
        self.appmenuf.add_command(label="open file client",command=self.chargementfileclients)
        self.appmenuf.add_command(label="enregister file location",command=self.enregisterfilelocation)
        self.appmenuf.add_command(label="open file location",command=self.chargementfilelocation)
        self.mbar.add_cascade(label="searchfile app",menu=self.appmenuf)
        self.c=Canvas(self,height=900,width=1500)
        self.bgk="imagecar2.jpg"
        image1=Image.open(self.bgk)
        img=image1.resize((1500,900),Image.ANTIALIAS)
        self.imgb=ImageTk.PhotoImage(img)
        self.c.create_image(0,0,image=self.imgb, anchor="nw")
        self.c.grid(row=0,column=0)
    def startmenu(self):
        self.config(menu=self.mbar)
        self.mainloop()
    def framec(self):
        self.fc=carframe(self)
        self.fc.start()
    def frameclient(self):
        self.fclient=clientframe(self)
        self.fclient.start()
    def framelocation(self):
        self.flocation=locationframe(self)
        self.flocation.start()
    def framedd(self):
        self.fd=framed(self,"mat")
        self.fd.start()
    def framedd1(self):
        self.fd=framed(self,"marq")
        self.fd.start()
    def framedd2(self):
        aa.cars.supprimercarv()
    def framedd3(self):
        self.fd=framedd(self,"prix")
        self.fd.start()
    def framedd4(self):
        self.fd=framedd(self,"color")
        self.fd.start()
    def framedd5(self):
        self.fd=framed(self,"cin")
        self.fd.start()
    def framedd6(self):
        self.fd=framedd(self,"address")
        self.fd.start()
    def framedd7(self):
        self.fd=framedd(self,"numphone")
        self.fd.start()
    def framedd8(self):
        self.fd=framedd(self,"adressemail")
        self.fd.start()
    def framedd9(self):
        self.fd=framed(self,"cinmat")
        self.fd.start()
    def framedd10(self):
        self.fd=framedd(self,"date")
        self.fd.start()
    def framedd11(self):
        self.fd=framedd(self,"dureelocation")
        self.fd.start()
    def frame1(self):
        self.f=frames(self)
        self.f.start()
    def search(self):
        self.fs=framesearch(self,"mat")
        self.fs.startsearch()
    def search2(self):
        self.fs=framesearch(self,"marq")
        self.fs.startsearch()
    def search3(self):
        self.fs=framesearch(self,"color")
        self.fs.startsearch()
    def search4(self):
        self.td=tableinfo2(["mat","marq","color","date","prix","etat"],aa.cars.recherchedcar())
        self.td.starttable()
    def search5(self):
        self.td=tableinfo2(["mat","marq","color","date","prix","etat"],aa.cars.recherchelcar())
        self.td.starttable()
    def search6(self):
        self.fs=framesearch(self,"date")
        self.fs.startsearch()
    def search7(self):
        self.fs=framesearch(self,"cin")
        self.fs.startsearch()
    def search8(self):
        self.fs=framesearch(self,"clientcin")
        self.fs.startsearch()
    def search9(self):
        self.fs=framesearch(self,"carmat")
        self.fs.startsearch()
    def search10(self):
        self.fs=framesearch(self,"locationdate")
        self.fs.startsearch()
    def search11(self):
        self.fs=framesearch(self,"dureelocation")
        self.fs.startsearch()
    def search12(self):
        self.fs=framesearch(self,"datedelocation")
        self.fs.startsearch()
    def enregisterfilecar(self):
        aa.cars.fileoutputcars()
    def enregisterfileclients(self):
        aa.client.fileoutputclients()
    def enregisterfilelocation(self):
        aa.fileoutputlocation()
    def chargementfilecar(self):
        aa.cars.fileinputcars()
    def chargementfileclients(self):
        aa.client.fileinputclients()
    def chargementfilelocation(self):
        aa.fileinputlocation()
        
    def opentable(self):
        self.td=tableinfo2(["mat","marq","color","date","prix","etat"],aa.cars.lcars)
        self.td.starttable()
    def opentable2(self):
        self.td=tableinfo2(["cin","nom","prenom","age","addresse","adressemail","numphone"],aa.client.lclients)
        self.td.starttable()
    def opentable3(self):
        self.td=tableinfo2(["locationnum","clientcin","carmat","datelocation","dureelocation","montant"],aa.location)
        self.td.starttable()
    def searchfile(self):
        choice=filedialog.askopenfilename()
class tableinfo(Tk):
    def __init__(self,l1,l2,m):
        Tk.__init__(self)
        n=0
        self.m=m
        for i in range (self.m):
            for j in range(2):
                self.te=Entry(self,width=30,font="Arial")
                self.te.grid(row=i,column=j)
                if(j==0):
                    self.te.insert(0,l1[n])
                    self.te.config(state="disabled")
                    self.te.config(disabledbackground="white")
                    self.te.config(disabledforeground="red")
                if(j==1):
                    self.te.insert(0,l2[n])
                    self.te.config(state="disabled")
                    self.te.config(disabledbackground="white")
                    self.te.config(disabledforeground="red")
            n+=1
                    
                   
    def starttable(self):
        self.mainloop()
class tableinfo2(Tk):
    def __init__(self,la,lv):
        Tk.__init__(self)
        self.la=la
        self.lv=lv
        l=()
        lvv=()
        for i in range(len(self.la)):
            l=tuple(self.la)
        self.tb=tkk.Treeview(self,column=l,show='headings',height=5)
        for i in range(len(self.la)):
            self.tb.heading(l[i],text=self.la[i])
        if(len(la)==6 and la[0]=="mat"):
            for i in range(len(lv)):
                lvv=(self.lv[i].mat,self.lv[i].marq,self.lv[i].color,self.lv[i].dateachat.affiched(),self.lv[i].prix,self.lv[i].etat)
                self.tb.insert('',tk.END,values=lvv)
        if(len(la)==7):
            for i in range(len(lv)):
                lvv=(self.lv[i].cin,self.lv[i].nom,self.lv[i].prenom,self.lv[i].age,self.lv[i].address,self.lv[i].adressmail.affichead(),self.lv[i].numphone)
                self.tb.insert('',tk.END,values=lvv)
        if(len(la)==6 and la[0]=="locationnum"):
            for i in range(len(lv)):
                lvv=(self.lv[i]['locationnum'],self.lv[i]['clientcin'],self.lv[i]['carmat'],self.lv[i]['datelocation'].affiched(),self.lv[i]['dureelocation'],self.lv[i]['montant'])
                self.tb.insert('',tk.END,values=lvv)
        
        self.tb.bind('<<TreeviewSelect>>',self.selectitem)
        self.tb.grid(row=1,column=1)
        self.sb=tkk.Scrollbar(self,orient=tk.VERTICAL,command=self.tb.yview)
        self.tb.configure(yscroll=self.sb.set)
        self.sb.grid(row=1,column=2,sticky='ns')
        self.sbb=tkk.Scrollbar(self,orient="horizontal",command=self.tb.xview)
        self.tb.configure(xscroll=self.sb.set)
        self.sbb.grid(row=2,column=1,sticky='ew')
    def selectitem(self,event):
        for i in self.tb.selection():
            value=self.tb.item(i)
            values=value['values']
            self.tt=tableinfo(self.la,values,len(self.la))
            messagebox.showinfo("information","selected value")
            
    def starttable(self):
        self.mainloop()
    

        
        
       
        
        
        
                
        
        
        
        
        
        
        
        
        

        
    
    
class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(background="sky blue")
        self.ff=Frame(borderwidth=3,relief="groove",highlightbackground="green",highlightthickness=2)
        self.ff.pack(padx=20,pady=20)
        self.c=Canvas(self.ff,height=700,width=500)
        self.bgk="imagecar.jpg"
        image1=Image.open(self.bgk)
        img=image1.resize((500,700))
        self.imgb=ImageTk.PhotoImage(img)
        self.c.pack(expand=True, fill= BOTH)
        self.c.create_image(0,0,image=self.imgb, anchor="nw")
        l="welcome to our application"
        self.l=self.c.create_text((10,10),text=l,anchor="nw")
        Button(self.ff,text="conncet",command=self.frame1).pack(side="bottom")
    
        
    def frame1(self):
        self.withdraw()
        self.m=menus(self)
        self.m.startmenu()
   

        
a=app()
a.mainloop()
        
    