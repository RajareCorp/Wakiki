################################
#                              #
#       Made by : Rajare       #
#       Version : 1.4          #
#                              #
################################

import re
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.colorchooser import askcolor

#_____________________________________

class Color:
    
    def __init__(self,hex_code):
        self.code = hex_code

colorbg = Color("#292B2F") #Couleur du fond
colormain = Color("#36393F") #Couleur secondaire
colorfont = Color("#FFFFFF") #Couleur de la police
coloradd = Color("#00FF00") #Couleur du bouton add
colordel = Color("#FF0000") #Couleur du bouton del
colorreset = Color("#000000") #Couleur du bouton reset

def actuColor():
    """
    Actualise les couleurs de chaques éléments de la fenètre
    """
    window.configure(bg = colorbg.code)
    GroupeEntry.configure(bg = colormain.code, fg = colorfont.code)
    Armure.configure(bg = colorbg.code,activebackground=colormain.code,selectcolor=colormain.code, fg = colorfont.code)
    SoinEtDégats.configure(bg = colorbg.code,activebackground=colormain.code,selectcolor=colormain.code, fg = colorfont.code)
    Kikimeter.configure(bg = colorbg.code,activebackground=colormain.code,selectcolor=colormain.code, fg = colorfont.code)
    Pw.configure(bg = colorbg.code,activebackground=colormain.code,selectcolor=colormain.code, fg = colorfont.code)
    Judge.configure(bg = colorbg.code,activebackground=colormain.code,selectcolor=colormain.code, fg = colorfont.code)
    Stele.configure(bg = colorbg.code,activebackground=colormain.code,selectcolor=colormain.code, fg = colorfont.code)
    LGroupeArmure.configure(bg = colorbg.code)
    LGroupeSoin.configure(bg = colorbg.code)
    LGroupeDégats.configure(bg = colorbg.code)
    LGroupePw.configure(bg = colorbg.code)
    LGroupeKiki.configure(bg = colorbg.code)
    LGroupeJuge.configure(bg = colorbg.code)
    StartButton.configure(bg = colormain.code, fg = colorfont.code)
    ResetButton.configure(bg = colorreset.code, fg = colorfont.code)
    GroupeAddButton.configure(bg = coloradd.code, fg = colorfont.code)
    GroupeRemoveButton.configure(bg = colordel.code, fg = colorfont.code)

#_____________________________________
#TKinter Initialisation
window = Tk()
window.title("Wakiki")
window.geometry('320x350')
window.minsize(300,350)
window.configure(bg = colorbg.code)

class Alpha:    
    def __init__(self,num):
        self.num = num

alpha = Alpha(0.5)

def ping():
    """
    Epingle Wakiki par dessus wakfu et le rend transparent si alpha.num est inférieur à 1.
    """
    window.attributes('-alpha', alpha.num)
    window.attributes('-topmost', 1)

def deping():
    """
    Désepingle Wakiki et lui rend son opacité.
    """
    window.attributes('-alpha', 1)
    window.attributes('-topmost', 0)

def alphaDef():
    """
    Définit le niveau d'opacité de la fenêtre Wakiki une fois épinglé.
    """
    number = simpledialog.askinteger("Transparence", "Taux de transparence ? (0,10)")
    number = number/10
    if number > 1:
        messagebox.showerror(title="Error", message="Le nombre doit être inférieur ou égal à 10 !")
        alphaDef()
    else:
        alpha.num = number

#_____________________________________

location = ""

while location=="": 
    try: #Essaye de lire le fichier qui contient l'emplacement de vos logs.
        ici = open("location.txt", "r", encoding="utf-8")
        location = ici.read()
        ici.close()
    except: #Force l'utilisateur à rentré son emplacement de log
        messagebox.showinfo('Emplacement log', "Wakiki a besoin de connaitre l'emplacement de vos logs pour fonctionner.")
        location = filedialog.askopenfilename(filetypes = (("Text files","*.log"),("all files","*.*")))
        ici = open("location.txt", "w", encoding="utf-8")
        ici.write(location)
        ici.close
try : #essaye de charger un thême
    color = open("theme.txt", "r", encoding="utf-8")
    theme = color.readlines()
    color.close()
    colorbg.code = theme[0][0:-1] #de 0 (début de la ligne) à -1 pour enlever le \n
    colormain.code = theme[1][0:-1]
    colorfont.code = theme[2][0:-1]
    coloradd.code = theme[3][0:-1]
    colordel.code = theme[4][0:-1]
    colorreset.code = theme[5]
    actuColor()
except: #Charge le thême de base.
    pass   

init = open(location, "w", encoding="utf-8")
init.close()

def reset():
    """
    Supprime tout le contenue des logs chat
    """
    init = open(location, "w", encoding="utf-8")
    init.close()
    start()

Groupe = []
GroupeArmure = []
GroupeSoin = []
GroupeDégats = []
GroupePw = []
GroupeKiki = []
GroupeEffet = []

#Liste des effets de chaque sort
ListeSortEffet =["Séisme","Relent Boisé","Vent Empoisonné","Ordre des Chênaies","Baroud","Brise'Os","Saignée mortelle","Piège de Silence","Piège de Lacération","Piège de Brume","Flèche Empoisonnée","Fiole Infectée"]
ListeEffet = ["Séisme","Maudit","Intoxiqué","Tétatoxine","Baroud","Saignement","Hémorragie","Piège de Silence","Piège de Lacération","Piège de Brume","Cràrsenic","Infection"]
ListeRetour = ["Sang pour sang","Sang brûlant","Calcination",] #Retour de flamme
ListeRetour1 = ["Souffle du dragon"] #Osamodas
#_____________________________________

result = Combobox(window,state="disabled")
result['values'] = ("Entité",)

delGroupe = Combobox(window,state="disabled")
delGroupe['values'] = ("Entité",)

delGroupe.place(x=140, y=7)

GroupeEntry = Entry(window,bg = colormain.code, fg = colorfont.code, width=15)

GroupeEntry.place(x=10, y=7)

def Add(Groupe = Groupe):   
    if GroupeEntry.get() !="":      
        Groupe.append(GroupeEntry.get())
        txt = "Groupe : "

        for i in Groupe:
            txt += i+" | "

        delGroupe.configure(values=tuple(Groupe), state="readonly" )
        delGroupe.current(0)
        result.configure(values=tuple(Groupe), state="readonly" )
        result.current(0)

        GroupeArmure.clear()
        GroupeSoin.clear()
        GroupeDégats.clear()
        GroupePw.clear()
        GroupeKiki.clear()
        GroupeEffet.clear()
        for i in range(len(Groupe)):
            GroupeArmure.append(0)
            GroupeSoin.append(0)
            GroupeDégats.append(0)
            GroupePw.append(0)
            GroupeKiki.append(0)
            GroupeEffet.append([Groupe[i]]) #nom de l'entité permettant ainsi de calculer les répliques/poisons etc...     

GroupeAddButton = Button(window, text="ADD", bg = "lime", fg=colorfont.code,command=Add)
GroupeAddButton.place(x=100, y=5)

def Remove(Groupe = Groupe):
    if Groupe != []:      
        Groupe.remove(result.get())

        if Groupe == []:
            delGroupe['values'] = ("Entité",)
            result['values'] = ("Entité",)  
            delGroupe.current(0)            
            result.current(0)        
            delGroupe.configure(state="disabled")
            result.configure(state="disabled")
            
        else:
            delGroupe.configure(values=tuple(Groupe))
            result.configure(values=tuple(Groupe))

        GroupeArmure.clear()
        GroupeSoin.clear()
        GroupeDégats.clear()
        GroupePw.clear()
        GroupeKiki.clear()
        GroupeEffet.clear()
        for i in range(len(Groupe)):
            GroupeArmure.append(0)
            GroupeSoin.append(0)
            GroupeDégats.append(0)
            GroupePw.append(0)
            GroupeKiki.append(0)
            GroupeEffet.append([Groupe[i]]) #nom de l'entité permettant ainsi de calculer les répliques/poisons etc...     

GroupeRemoveButton = Button(window, text="DEL", bg = "red", fg=colorfont.code,command=Remove)
GroupeRemoveButton.place(x=280, y=5)
#_____________________________________
Armure_state = BooleanVar()
Armure = Checkbutton(window, text='Armure           ',var=Armure_state, bg = colorbg.code, fg=colorfont.code, selectcolor=colormain.code, activebackground=colormain.code)
Armure.place(x=0, y=40)

def kikiConditionTrue():
    """
    Active le bouton Dégats infligés
    """
    SoinEtDégats.configure(command=kikiConditionFalse)
    Kikimeter.configure(state='normal')

def kikiConditionFalse():
    """
    Désactive le bouton Dégats infligés
    """
    SoinEtDégats.configure(command=kikiConditionTrue)
    Kikimeter.configure(state='disabled')
    Kikimeter.deselect()

SoinEtDégats_state = BooleanVar()
SoinEtDégats = Checkbutton(window, text='Soin et Dégats', var = SoinEtDégats_state, bg = colorbg.code, fg=colorfont.code, selectcolor=colormain.code,activebackground=colormain.code, command=kikiConditionTrue)
SoinEtDégats.place(x=0, y=65)

Kikimeter_state = BooleanVar()
Kikimeter = Checkbutton(window, text='Dégats infligés', var = Kikimeter_state, bg = colorbg.code, fg=colorfont.code, selectcolor=colormain.code,activebackground=colormain.code, state='disabled')
Kikimeter.place(x=0, y=90)

Pw_state = BooleanVar()
Pw = Checkbutton(window, text='Pw                    ', var = Pw_state, bg = colorbg.code, fg=colorfont.code, selectcolor=colormain.code,activebackground=colormain.code)
Pw.place(x=0, y=115)

Judge_state = BooleanVar()
Judge = Checkbutton(window, text='Juge                  ', var = Judge_state, bg = colorbg.code, fg=colorfont.code, selectcolor=colormain.code,activebackground=colormain.code)
Judge.place(x=0, y=140)

Stele_state = BooleanVar()
Stele = Checkbutton(window, text='Juge                  ', var = Stele_state, bg = colorbg.code, fg=colorfont.code, selectcolor=colormain.code,activebackground=colormain.code)

LGroupeArmure = Label(window, fg="green", bg = colorbg.code, text="Armures reçues :")

LGroupeSoin = Label(window, fg="cyan", bg = colorbg.code, text="Soin reçus :")

LGroupeDégats = Label(window, fg="orange", bg = colorbg.code, text="Dégats reçus :")

LGroupePw = Label(window, fg="cyan", bg = colorbg.code, text="PW :")

LGroupeKiki = Label(window, fg="red", bg = colorbg.code, text="Dégats :")

LGroupeJuge = Label(window, fg="gold", bg = colorbg.code, text="")
#_____________________________________
def start(GroupeArmure = GroupeArmure, GroupeSoin = GroupeSoin, GroupeDégats = GroupeDégats,GroupePw = GroupePw, GroupeKiki = GroupeKiki ):
    if Groupe != []:
        effet = None

        while True:
            log = open(location, "r", encoding="utf-8") #lis les logs chat
            data = log.read()

            if Armure_state.get() == True:
                LGroupeArmure.place(x=0, y=210)
            else:
                LGroupeArmure.place_forget()

            if SoinEtDégats_state.get() == True:    
                LGroupeSoin.place(x=0, y=230)
                LGroupeDégats.place(x=0, y=250)
            else:
                LGroupeSoin.place_forget()
                LGroupeDégats.place_forget()

            if Kikimeter_state.get() == True:                
                LGroupeKiki.place(x=0, y=270)
            else:
                LGroupeKiki.place_forget()

            if Pw_state.get() == True:
                LGroupePw.place(x=0, y=290)
            else:
                LGroupePw.place_forget()
            
            if Judge_state.get() == True:
                LGroupeJuge.configure(text = "") 
                LGroupeJuge.place(x=0, y=310)
            else:
                LGroupeJuge.place_forget()
                
            isOk = True
            retour = False

            for i in range(0,len(data)):

                if Armure_state.get() == True:
                    if data[i] == "A":
                        if data[i:i+6] == "Armure": #Détecte les dons d'armure
                            compteur = i
                            while data[compteur] != ":":
                                compteur -= 1
                            for test in data[compteur+2:i-1]: #Récupère la valeur
                                if test in list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "): #Tri pour ne garder que les chiffres
                                    isOk = False
                            if isOk == True:
                                valeur = data[compteur+2:i-1]
                                valeur = valeur.split()
                                valeur = "".join(valeur) #Converti les 1 000 en 1000                        

                                compteur_name = compteur+2
                                while data[compteur_name] != "]":
                                    compteur_name -= 1

                                if data[compteur_name+2:compteur] in Groupe: #Si le nom est dans la liste du grp
                                    GroupeArmure[Groupe.index(data[compteur_name+2:compteur])] += int(valeur)

                if SoinEtDégats_state.get() == True:
                    if data[i] == "P":
                        if data[i:i+2] == "PV": #Détecte les changements de PV
                            compteur = i
                            while data[compteur] != ":":
                                compteur -= 1

                            for test in data[compteur+2:i-1]: #Récupère la valeur
                                if re.search('[A-Za-z]',test): #Tri pour ne garder que les chiffres
                                    isOk = False
                            if isOk == True:
                                valeur = data[compteur+2:i-1]
                                valeur = valeur.split()
                                valeur = "".join(valeur) #Converti les 1 000 en 1000 

                                if "(" in data[i+5 : i+15]: #Vérifie si une parenthèse est présente après l'élément du sort
                                        compteurEffet = i + 5  
                                        while data[compteurEffet] != "(":
                                            compteurEffet += 1
                                        
                                        compteurFinEffet = compteurEffet
                                        while data[compteurFinEffet] != ")":
                                            compteurFinEffet += 1
                                        if data[compteurEffet+1 : compteurFinEffet] in  ListeEffet: #permet au steamer de ne pas bugger
                                            effet = data[compteurEffet+1 : compteurFinEffet]                                        

                                if Kikimeter_state.get() == True:
                                    if valeur[0] == "-":
                                        compteurKiki = compteur-34 #valeur approximative
                                        while data[compteurKiki:compteurKiki+13] != "lance le sort":                                   
                                            compteurKiki -= 1                            
                                        compteurKikiName = compteurKiki                               

                                        compteurNomDuSort = compteurKiki+14
                                        compteurNomDuSortFin = compteurKiki+15

                                        while data[compteurNomDuSortFin:compteurNomDuSortFin+1] != "\n":                                        
                                                compteurNomDuSortFin += 1

                                        if " (Critiques)" in data[compteurNomDuSort : compteurNomDuSortFin+1]:
                                            compteurNomDuSortFin -= 12
                                        
                                        if effet == None:
                                            if retour == False:
                                                while data[compteurKikiName] != "]":
                                                    compteurKikiName -= 1
                                                if data[compteurKikiName+2:compteurKiki-1] in Groupe: #Si le nom est dans la liste du grp
                                                    if data[compteurNomDuSort : compteurNomDuSortFin] !="Entaille" :                        
                                                        GroupeKiki[Groupe.index(data[compteurKikiName+2:compteurKiki-1])] += -int(valeur)
                                                        if data[compteurNomDuSort : compteurNomDuSortFin] in ListeSortEffet:                                                                      
                                                            GroupeEffet[Groupe.index(data[compteurKikiName+2:compteurKiki-1])].append(ListeEffet[ListeSortEffet.index(data[compteurNomDuSort : compteurNomDuSortFin])]) 
                                                        if data[compteurNomDuSort : compteurNomDuSortFin] in ListeRetour: 
                                                            retour = True 
                                            else:
                                                retour = False
                                        else:                                
                                            for test in GroupeEffet: #récupère la liste d'effet d'un perso
                                                
                                                if effet in test: #si l'effet est dans sa liste
                                                    GroupeEffet[Groupe.index(test[0])].remove(effet)
                                                    effet = None
                                                    GroupeKiki[Groupe.index(test[0])] += -int(valeur) #test[0] est le nom du joueur

                                compteur_name = compteur+2
                                while data[compteur_name] != "]":
                                    compteur_name -= 1
                                if data[compteur_name+2:compteur] in Groupe: #Si le nom est dans la liste du grp
                                    if valeur[0] == "+":
                                        GroupeSoin[Groupe.index(data[compteur_name+2:compteur])] += int(valeur)
                                    if valeur[0] == "-":
                                        GroupeDégats[Groupe.index(data[compteur_name+2:compteur])] += -int(valeur)
                                        if data[compteurNomDuSort : compteurNomDuSortFin] in ListeRetour1:

                                            GroupeKiki[Groupe.index(data[compteurKikiName+2:compteurKiki-1])] -= -int(valeur) #retire les retours de flammes qui sont avant la ligne de dégats                       

                if Pw_state.get() == True:
                    if data[i] == "P":
                        if data[i:i+2] == "PW": #Détecte les changements de PW
                            compteur = i
                            while data[compteur] != ":":
                                compteur -= 1

                            for test in data[compteur+2:i-1]: #Récupère la valeur
                                if re.search('[A-Za-z]',test): #Tri pour ne garder que les chiffres
                                    isOk = False
                            if isOk == True:
                                valeur = data[compteur+2:i-1]                        

                                compteur_name = compteur+2
                                while data[compteur_name] != "]":
                                    compteur_name -= 1
                                if data[compteur_name+2:compteur] in Groupe: #Si le nom est dans la liste du grp
                                    GroupePw[Groupe.index(data[compteur_name+2:compteur])] += int(valeur)

                if Stele_state.get() == True:
                    if data[i] == "s": #Détecte le mot stèle
                        if data[i:i+5] in ["stele","Stele","stèle","Stèle"]:
                            print("qqun veux dj stèle")

                isOk = True

            entite = Groupe.index(result.get())


            if Armure_state.get() == True:
                LGroupeArmure.configure(text = "Armures reçues : "+str(GroupeArmure[entite])) 
                    
            if SoinEtDégats_state.get() == True:
                LGroupeSoin.configure(text = "Soins reçus : "+str(GroupeSoin[entite])) 
                LGroupeDégats.configure(text = "Dégats reçus : "+str(GroupeDégats[entite])) 

            if Pw_state.get() == True:
                LGroupePw.configure(text = "PW : "+str(GroupePw[entite])) 

            if Kikimeter_state.get() == True:
                LGroupeKiki.configure(text = "Dégats : "+str(GroupeKiki[entite])) 

            if Judge_state.get() == True:               
                if GroupeArmure[entite] > GroupeDégats[entite]:
                    LGroupeJuge.configure(text = LGroupeJuge.cget("text")+"\n | BABYSITTING") 

                if (GroupeArmure[entite] + GroupeSoin[entite]) < GroupeDégats[entite]//2:
                    LGroupeJuge.configure(text = LGroupeJuge.cget("text")+"\n  | ALONE") 

                if GroupePw[entite] < -3:
                    LGroupeJuge.configure(text = LGroupeJuge.cget("text")+"\n  | WAKFUVORE") 

                if Kikimeter == True:
                    if GroupeKiki[entite] < GroupeDégats[entite]//2:
                        LGroupeJuge.configure(text = LGroupeJuge.cget("text")+"\n  | USELESS") 
                    
            
            GroupeArmure.clear()
            GroupeSoin.clear()
            GroupeDégats.clear()
            GroupePw.clear()
            GroupeKiki.clear()
            GroupeEffet.clear()
            effet = None

            for i in range(len(Groupe)):
                GroupeArmure.append(0)
                GroupeSoin.append(0)
                GroupeDégats.append(0)
                GroupePw.append(0)
                GroupeKiki.append(0)
                GroupeEffet.append([Groupe[i]])

            window.mainloop()
            log.close()

#_____________________________________
StartButton = Button(window, text="REFRESH",bg = colormain.code, fg=colorfont.code,command=start)
StartButton.place(x=145, y=178)

ResetButton = Button(window, text="RESET", bg="black", fg=colorfont.code,command=reset)
ResetButton.place(x=200, y=178)

delGroupe.current(0)
result.current(0) #set the selected item
result.place(x=0, y=180)


def saveS(entite = result.get()):
    text = ""
    if Armure_state.get() == True:
        text += "Armures reçues : "+str(GroupeArmure[entite])+"\n"
            
    if SoinEtDégats_state.get() == True:
        text += "Soins reçus : "+str(GroupeSoin[entite])+"\n" 
        text += "Dégats reçus : "+str(GroupeDégats[entite])+"\n" 

    if Pw_state.get() == True:
        text += "PW : "+str(GroupePw[entite])+"\n" 

    if Kikimeter_state.get() == True:
        text += "Dégats : "+str(GroupeKiki[entite])+"\n"

    if Judge_state.get() == True:
        text += str(LGroupeJuge[entite])
    
    save = open("Wakiki_"+entite+".txt", "w", encoding="utf-8")
    save.write(text)
    save.close()
    
def saveC():
    text = str(Armure_state.get())+"\n"+str(SoinEtDégats_state.get())+"\n"+str(Pw_state.get())+"\n"+str(Kikimeter_state.get())+"\n"+str(Judge_state.get())+"\n"
    name = simpledialog.askstring("Conf file", "Config name ?")
    save = open("Conf_"+name+".txt", "w", encoding="utf-8")
    save.write(text)
    save.close()

def saveG(grp = Groupe):
    text = ",".join(grp)
    name = simpledialog.askstring("Grp file", "Groupe name ?")
    save = open("Grp_"+name+".txt", "w", encoding="utf-8")
    save.write(text)
    save.close()

def openC():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    conf = open(file, "r", encoding="utf-8")
    conf = conf.readlines()
    print('test')
    if conf[0][0:-1] == "True":
        Armure_state.set(True)
    if conf[1][0:-1] == "True":
        SoinEtDégats_state.set(True)
        kikiConditionTrue()
    if conf[2][0:-1] == "True":
        Kikimeter_state.set(True)
    if conf[3][0:-1] == "True":
        Pw_state.set(True)

    
def openG():
    Groupe.clear    
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    grp = open(file, "r", encoding="utf-8")
    grp = grp.read()
    grp = list(grp.split(','))
    for entite in grp:
        GroupeEntry.insert(0,entite)
        Add()
        GroupeEntry.delete(0,999)

def Version():
    """
    Fournis des informations sur la version de Wakiki
    """
    messagebox.showinfo("Version 1.4", "Sortie le 23/08\n\n - Refonte visuel\n - Ajout du système de ping\n - Amélioration du code\n\nMade by Rajare")

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save stat", command=saveS)
filemenu.add_command(label="_____________",)
filemenu.add_command(label="Save config", command=saveC)
filemenu.add_command(label="Open config", command=openC)
filemenu.add_command(label="_____________",)
filemenu.add_command(label="Save group", command=saveG)
filemenu.add_command(label="Open group", command=openG)
menubar.add_cascade(label="Option", menu=filemenu)

def backgroundColor():
    color = askcolor(title="Background color")
    colorbg.code = color[1]
    actuColor()
    
def secondaireColor():
    color = askcolor(title="Secondaire color")
    colormain.code = color[1]
    actuColor()

def fontColor():
    color = askcolor(title="font color")
    colorfont.code = color[1]
    actuColor()

def addColor():
    color = askcolor(title="addButton color")
    coloradd.code = color[1]
    actuColor()

def delColor():
    color = askcolor(title="delButton color")
    colordel.code = color[1]
    actuColor()

def resetColor():
    color = askcolor(title="resetButton color")
    colorreset.code = color[1]
    actuColor()

def defaultColor():
    colorbg.code = "#292B2F"
    colormain.code = "#36393F"
    colorfont.code = "#FFFFFF"
    coloradd = Color("#00FF00")
    colordel = Color("#FF0000")
    colorreset = Color("#000000")
    actuColor()

def saveColor():
    text = colorbg.code+"\n"+colormain.code+"\n"+colorfont.code+"\n"+coloradd.code+"\n"+colordel.code+"\n"+colorreset.code
    save = open("theme.txt", "w", encoding="utf-8")
    save.write(text)
    save.close()

thememenu = Menu(menubar, tearoff=0)
thememenu.add_command(label="Background", command=backgroundColor)
thememenu.add_command(label="Secondaire", command=secondaireColor)
thememenu.add_command(label="Font", command=fontColor)
thememenu.add_command(label="AddButton", command=addColor)
thememenu.add_command(label="DelButton", command=delColor)
thememenu.add_command(label="ResetButton", command=resetColor)
thememenu.add_command(label="_____________",)
thememenu.add_command(label="Save", command=saveColor)
thememenu.add_command(label="Default", command=defaultColor)
menubar.add_cascade(label="Theme", menu=thememenu)

pingmenu = Menu(menubar, tearoff=0)
pingmenu.add_command(label="Ping", command=ping)
pingmenu.add_command(label="Deping", command=deping)
pingmenu.add_command(label="Paramètre", command=alphaDef)
menubar.add_cascade(label="Ping", menu=pingmenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label="Version", command=Version)
menubar.add_cascade(label="Info", menu=infomenu)

window.config(menu=menubar)

window.mainloop()