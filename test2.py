from tkinter import*
import customtkinter
from class_bouton import Bouton
from class_fenetre import Fenetre
from Pile import Pile
import csv
from PIL import Image
from random import*
from class_file import File

def jeux():

    fenetre_jeu = Fenetre(1000, 700, 400,150,'#145810','Solitaire',"./images/fond_plateau.png",None)
    fenetre_jeu.draw_fenetre()

    mon_dictionnaire_carte = {"As de PIQUE": r"images\Jeux_de_carte\ace_of_spades.png", "2 de PIQUE": r"images\Jeux_de_carte\2_of_spades.png", "3 de PIQUE": r"images\Jeux_de_carte\3_of_spades.png", "4 de PIQUE": r"images\Jeux_de_carte\4_of_spades.png", "5 de PIQUE": r"images\Jeux_de_carte\5_of_spades.png", "6 de PIQUE": r"images\Jeux_de_carte\6_of_spades.png", "7 de PIQUE": r"images\Jeux_de_carte\7_of_spades.png", "8 de PIQUE": r"images\Jeux_de_carte\8_of_spades.png", "9 de PIQUE": r"images\Jeux_de_carte\9_of_spades.png", "10 de PIQUE": r"images\Jeux_de_carte\10_of_spades.png", "Valet de PIQUE": r"images\Jeux_de_carte\jack_of_spades2.png", "Dame de PIQUE": r"images\Jeux_de_carte\queen_of_spades2.png", "Roi de PIQUE": r"images\Jeux_de_carte\king_of_spades2.png", "As de COEUR": r"images\Jeux_de_carte\ace_of_hearts.png", "2 de COEUR": r"images\Jeux_de_carte\2_of_hearts.png", "3 de COEUR": r"images\Jeux_de_carte\3_of_hearts.png", "4 de COEUR": r"images\Jeux_de_carte\4_of_hearts.png", "5 de COEUR": r"images\Jeux_de_carte\5_of_hearts.png", "6 de COEUR": r"images\Jeux_de_carte\6_of_hearts.png", "7 de COEUR": r"images\Jeux_de_carte\7_of_hearts.png", "8 de COEUR": r"images\Jeux_de_carte\8_of_hearts.png", "9 de COEUR": r"images\Jeux_de_carte\9_of_hearts.png", "10 de COEUR": r"images\Jeux_de_carte\10_of_hearts.png", "Valet de COEUR": r"images\Jeux_de_carte\jack_of_hearts2.png", "Dame de COEUR": r"images\Jeux_de_carte\queen_of_hearts2.png", "Roi de COEUR": r"images\Jeux_de_carte\king_of_hearts2.png", "As de CARREAU": r"images\Jeux_de_carte\ace_of_diamonds.png", "2 de CARREAU": r"images\Jeux_de_carte\2_of_diamonds.png", "3 de CARREAU": r"images\Jeux_de_carte\3_of_diamonds.png", "4 de CARREAU": r"images\Jeux_de_carte\4_of_diamonds.png", "5 de CARREAU": r"images\Jeux_de_carte\5_of_diamonds.png", "6 de CARREAU": r"images\Jeux_de_carte\6_of_diamonds.png", "7 de CARREAU": r"images\Jeux_de_carte\7_of_diamonds.png", "8 de CARREAU": r"images\Jeux_de_carte\8_of_diamonds.png", "9 de CARREAU": r"images\Jeux_de_carte\9_of_diamonds.png", "10 de CARREAU": r"images\Jeux_de_carte\10_of_diamonds.png", "Valet de CARREAU":r"images\Jeux_de_carte\jack_of_diamonds2.png", "Dame de CARREAU": r"images\Jeux_de_carte\queen_of_diamonds2.png", "Roi de CARREAU": r"images\Jeux_de_carte\king_of_diamonds2.png", "As de TREFLE": r"images\Jeux_de_carte\ace_of_clubs.png", "2 de TREFLE": r"images\Jeux_de_carte\2_of_clubs.png", "3 de TREFLE": r"images\Jeux_de_carte\3_of_clubs.png", "4 de TREFLE": r"images\Jeux_de_carte\4_of_clubs.png", "5 de TREFLE": r"images\Jeux_de_carte\5_of_clubs.png", "6 de TREFLE": r"images\Jeux_de_carte\6_of_clubs.png", "7 de TREFLE": r"images\Jeux_de_carte\7_of_clubs.png", "8 de TREFLE": r"images\Jeux_de_carte\8_of_clubs.png", "9 de TREFLE": r"images\Jeux_de_carte\9_of_clubs.png", "10 de TREFLE": r"images\Jeux_de_carte\10_of_clubs.png", "Valet de TREFLE": r"images\Jeux_de_carte\jack_of_clubs.png", "Dame de TREFLE": r"images\Jeux_de_carte\queen_of_diamonds2.png", "Roi de TREFLE": r"images\Jeux_de_carte\king_of_clubs2.png"}

    mon_paquet = [a for a in mon_dictionnaire_carte.items()]
    Pioche = Pile("Pioche")

    

    for i in range(0,24):
        choix=randint(0,len(mon_paquet)-1)
        Pioche.empiler(mon_paquet[choix])
        del mon_paquet[choix]
    """
    different_pile_drop=[Pile1,Pile2,Pile3,Pile4,Pile5,Pile6,Pile7]
    nb_carte=2
    for i in range(7):
        for j in range(1,nb_carte):
            choix=randint(0,len(mon_paquet)-1)
            different_pile_drop[i].empiler(mon_paquet[choix])
            del mon_paquet[choix]
        nb_carte+=1
    """

    pioche_retourne= Pile("Pioche")
    
    def retourn_pioche(event):
        if Pioche.est_vide()==FALSE:
            for i in range(1):
                pioche_retourne.empiler(Pioche.sommet(1))
                Pioche.depiler()
        else:
            for i in range(pioche_retourne.taille()):
                Pioche.empiler(pioche_retourne.sommet(1))
                pioche_retourne.depiler()

                pioche_retourne_position.del_label(0)
        
        ne_pas_suppr = customtkinter.CTkLabel(fenetre_jeu.fenetre,text="")
        add_dragable()
        pioche()

    def add_dragable(): 
        try:
            pioche_retourne_position.del_label(1)
        except:
            pass
        
        pile_zone1_position.positionner_cartes()
        pile_zone2_position.positionner_cartes()
        pile_zone3_position.positionner_cartes()
        pile_zone4_position.positionner_cartes()
        pile_zone5_position.positionner_cartes()
        pile_zone6_position.positionner_cartes()
        pile_zone7_position.positionner_cartes()
        pioche_retourne_position.positionner_cartes()
        
    
        

    def pioche():
        if Pioche.est_vide():
            image_recommencer=customtkinter.CTkImage(Image.open('images/recommencer.png'),size=(98,148))
            image_label_pioche.configure(image=image_recommencer)
        else:
            #Image pioche
            image_path = r"images\Jeux_de_carte\card_back.png"
            image = customtkinter.CTkImage(Image.open(image_path),size=(98,148))
            image_label_pioche.configure(image=image)

    image_label_pioche = customtkinter.CTkLabel(fenetre_jeu.fenetre, text="")
    image_label_pioche.place(x=51, y=51)

    image_label_pioche.bind("<Button-1>", retourn_pioche)
    pioche()

    

    class DragAndDrop:
        list_drop=[]
        pile_list_drop=[]
        file_pioche=File()
        file_zone1=File()
        file_zone2=File()
        liste_jeu=File()
        def __init__(self,widget,fenetre,pile,drop,drag,file=None):
            self.drag=drag
            self.drop=drop
            self.pile=pile
            self.widget=widget
            self.fenetre=fenetre
            file_new=None
            if self.drag==True:
                if self.pile.nom=="Pioche":
                    self.file=DragAndDrop.file_pioche
                elif self.pile.nom=="pile_zone1":
                    self.file=DragAndDrop.file_zone1
                elif self.pile.nom=="pile_zone2":
                    self.file=DragAndDrop.file_zone2
                
                if self.file.est_vide()==False:
                    self.file.defiler().destroy()
                #print(self.pile.nom,self.file.contenue())
                self.file.enfiler(self.widget)
                self.widget=self.file.bout_file()
                self.set_drag(self.widget)

            if self.drop==True:
                DragAndDrop.list_drop.append(self.widget)
                DragAndDrop.pile_list_drop.append(self.pile)
                

        def set_drag(self,widget):
            self.widget.bind("<Button-1>",self.on_click_start)
            self.widget.bind("<B1-Motion>",self.on_click)
            self.widget.bind("<ButtonRelease-1>",self.on_drop)
            
        def on_click_start(self,event):
            self.widget_x=self.widget.winfo_x()
            self.widget_y=self.widget.winfo_y()

        def on_click(self,event):
            
            self.widget.place(x=event.x_root - self.fenetre.winfo_rootx(), y=event.y_root - self.fenetre.winfo_rooty())
            self.image=self.widget.cget("image")

        def on_drop(self,event):
            widget_dropped = False
            for target in DragAndDrop.list_drop:
                coord_target_x,coord_target_y=target.winfo_x(),target.winfo_y()
                coord_target_x_max,coord_target_y_max=coord_target_x+target.winfo_width(),coord_target_y+target.winfo_height()
                if self.widget.winfo_x()>=coord_target_x and self.widget.winfo_x()<=coord_target_x_max and self.widget.winfo_y()>=coord_target_y and self.widget.winfo_y()<=coord_target_y_max:
                    #try:
                    self.widget.place(x=coord_target_x,y=coord_target_y)
                    pile=DragAndDrop.pile_list_drop[DragAndDrop.list_drop.index(target)]
                    pile.empiler(self.pile.sommet(1))
                    self.pile.depiler()

                    
                    
                    
                    if pile.nom=="pile_zone1":
                        file_new=DragAndDrop.file_zone1
                    elif pile.nom=="pile_zone2":
                        file_new=DragAndDrop.file_zone2

                    widget_dropped = True
                    file_new.changement_file(self.file)
                    #print(self.file.contenue(),file_new.contenue())
                    self.pile=pile
                    pioche_retourne_position.nb_carte_afficher()
                    add_dragable()
                    """    
                    except Exception as e:
                        print(f"Error occurred: {e}")
                    """
            if not widget_dropped:
                self.widget.place(x=self.widget_x, y=self.widget_y)
                pioche_retourne_position.del_label(0)
                add_dragable()


    class PileAffichage:
        def __init__(self, pile, fenetre, coord_x, coord_y, ecart,taille_pile):
            self.pile = pile
            self.fenetre = fenetre
            self.coord_x = coord_x
            self.coord_y = coord_y
            self.ecart = ecart
            self.labels = []
            self.taille_pile=taille_pile
            self.carte_a_afficher=0

        def del_label(self,x):
            for i in range(len(self.labels)-x):
                self.labels[i].destroy()
        def nb_carte_afficher(self):
            self.carte_a_afficher-=1
        def positionner_cartes(self):
            try:
                self.labels.clear()
                if self.carte_a_afficher<self.taille_pile and self.carte_a_afficher!= self.pile.taille():
                    self.carte_a_afficher+=1

                for i in range(self.carte_a_afficher):
                    image_label = customtkinter.CTkLabel(self.fenetre, text="")
                    image_label.place(x=self.coord_x,y=self.coord_y+i*self.ecart)
                    self.labels.append(image_label)

                    image_path = self.pile.sommet(self.carte_a_afficher-i)[1]
                    image = customtkinter.CTkImage(Image.open(image_path), size=(100, 150))
                    image_label.configure(image=image)
                    

                    if i == self.carte_a_afficher- 1: 
                        DragAndDrop(image_label, self.fenetre, self.pile, drop=False, drag=True)
            except:
                self.carte_a_afficher=0
                



    

    def zone_drop():
        global pile_zone1,pile_zone2,pile_zone3,pile_zone4,pile_zone5,pile_zone6,pile_zone7
        zone1=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone2=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone3=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone4=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone5=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone6=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone7=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        pile_zone1=Pile("pile_zone1")
        pile_zone2=Pile("pile_zone2")
        pile_zone3=Pile("pile_zone3")
        pile_zone4=Pile("pile_zone4")
        pile_zone5=Pile("pile_zone5")
        pile_zone6=Pile("pile_zone6")
        pile_zone7=Pile("pile_zone7")
        zone1.place(x=31,y=331)
        zone2.place(x=171,y=331)
        zone3.place(x=311,y=331)
        zone4.place(x=451,y=331)
        zone5.place(x=591,y=331)
        zone6.place(x=731,y=331)
        zone7.place(x=871,y=331)
        drop1=DragAndDrop(zone1,fenetre_jeu.fenetre,pile_zone1,drop=True,drag=False)
        drop2=DragAndDrop(zone2,fenetre_jeu.fenetre,pile_zone2,drop=True,drag=False)
        drop3=DragAndDrop(zone3,fenetre_jeu.fenetre,pile_zone3,drop=True,drag=False)
        drop4=DragAndDrop(zone4,fenetre_jeu.fenetre,pile_zone4,drop=True,drag=False)
        drop5=DragAndDrop(zone5,fenetre_jeu.fenetre,pile_zone5,drop=True,drag=False)
        drop6=DragAndDrop(zone6,fenetre_jeu.fenetre,pile_zone6,drop=True,drag=False)
        drop7=DragAndDrop(zone7,fenetre_jeu.fenetre,pile_zone7,drop=True,drag=False)
    zone_drop()

    pioche_retourne_position=PileAffichage(pioche_retourne,fenetre_jeu.fenetre,200,50,30,3)
    pile_zone1_position=PileAffichage(pile_zone1,fenetre_jeu.fenetre,31,331,20,13)
    pile_zone2_position=PileAffichage(pile_zone2,fenetre_jeu.fenetre,171,331,20,13)
    pile_zone3_position=PileAffichage(pile_zone3,fenetre_jeu.fenetre,311,331,20,13)
    pile_zone4_position=PileAffichage(pile_zone4,fenetre_jeu.fenetre,451,331,20,13)
    pile_zone5_position=PileAffichage(pile_zone5,fenetre_jeu.fenetre,591,331,20,13)
    pile_zone6_position=PileAffichage(pile_zone6,fenetre_jeu.fenetre,731,331,20,13)
    pile_zone7_position=PileAffichage(pile_zone7,fenetre_jeu.fenetre,871,331,20,13)
    




jeux()
mainloop()

