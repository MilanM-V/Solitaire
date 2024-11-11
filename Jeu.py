from tkinter import*
import customtkinter
from class_bouton import Bouton
from class_fenetre import Fenetre
from Pile import Pile
from PIL import Image
from random import*
from class_file import File
import sqlite3
from tkinter import messagebox

db = sqlite3.connect("./donnees/compte.db")
cursor=db.cursor()

connexion_statut=False
btn_state = False

try:
    username=cursor.execute("SELECT Pseudo FROM compte WHERE statut_connexion=?",("Oui",)).fetchone()[0]
except:
    pass
fenetre_page_principal = Fenetre(1000, 700, 400,150,'#145810','Solitaire',None,None)
fenetre_page_principal.draw_fenetre()
fenetre_page_regle = Fenetre(1000, 700, 400,150,'#145810','Solitaire',None,fenetre_page_principal.fenetre)
fenetre_page_regle.draw_fenetre()
fenetre_page_regle.fenetre_enlever()
fenetre_jeu = Fenetre(1000, 700, 400,150,'#145810','Solitaire',"./images/fond_plateau.png",fenetre_page_principal.fenetre)
fenetre_jeu.draw_fenetre()
fenetre_jeu.fenetre_enlever()
fenetre_page_compte = Fenetre(1000, 700, 400,150,'#145810','Solitaire',None,fenetre_page_principal.fenetre)
fenetre_page_compte.draw_fenetre()
fenetre_page_compte.fenetre_enlever()


#Image 4 carte
image_path_4_carte = "images/carte_image-removebg-preview.png"
image_4_carte = customtkinter.CTkImage(Image.open(image_path_4_carte),size=(350,249))
image_label_4_carte = customtkinter.CTkLabel(fenetre_page_principal.fenetre, image=image_4_carte,text="")
image_label_4_carte.place(x=330, y=450)
#Image 4 carte mélanger
image_path_4_melange = "images/image_carte_2png-removebg-preview.png"
image_4_melange = customtkinter.CTkImage(Image.open(image_path_4_melange),size=(281,179))
image_label_4_melange = customtkinter.CTkLabel(fenetre_page_principal.fenetre, image=image_4_melange,text="")
image_label_4_melange.place(x=650, y=300)
#Image 4 carte socle
image_path_4_socle = "images/images-removebg-preview.png"
image_4_socle = customtkinter.CTkImage(Image.open(image_path_4_socle),size=(281,179))
image_label_4_socle = customtkinter.CTkLabel(fenetre_page_principal.fenetre, image=image_4_socle,text="")
image_label_4_socle.place(x=50, y=300)
#Image 3cartes
image_path_3image = "images/3photo.png"
image_3image = customtkinter.CTkImage(Image.open(image_path_3image),size=(600,300))
image_label_3image = customtkinter.CTkLabel(fenetre_page_principal.fenetre, image=image_3image,text="")
image_label_3image.place(x=200, y=-10)

#Titre Page
texte_page_principal = customtkinter.CTkLabel(fenetre_page_principal.fenetre, text = "Solitaire",text_color = '#22dc1c',font=('Sitka Text Semibold',50),fg_color='transparent')
texte_page_principal.place(x=400,y=250)

#Bouton Quitter
bouton_quitter=Bouton(fenetre_page_principal,50,50,10,2,'black','#e73535','#d12e2e','Quitter','black',('Sitka Text Semibold',30),860,10,quit)
bouton_quitter.draw_bouton()

def retour():
    global btn_state
    fenetre_page_compte.fenetre_enlever()
    fenetre_page_regle.fenetre_enlever()
    fenetre_jeu.fenetre_enlever()
    fenetre_page_principal.fenetre_apparaitre()
    btn_state=False
    NavBar.destroy()
    frame.destroy()
    bandeau(fenetre_page_principal.fenetre,"fenetre_page_principal")

"""Creation de la fenetre de connection"""
def creation_compte():
    fenetre_compte=Fenetre(200,200,500,250,'#10480d','Connectez-vous à votre compte',None,fenetre_page_principal.fenetre)
    fenetre_compte.draw_fenetre()
    fenetre_compte.fenetre.overrideredirect(True)
    quitter=Bouton(fenetre_compte,50,25,4,2,'Black','#e73535','#d12e2e','Quitter','Black',('Sitka Text Semibold',12),145,0,fenetre_compte.fenetre_enlever)
    quitter.draw_bouton()


    def username_existe_dans_colonne(username):
        pseudo= [nom[0] for nom in cursor.execute("SELECT Pseudo FROM compte").fetchall()]
        for i in range(len(pseudo)):
            if pseudo[i]==username:
                return True
        return False
    def password_existe_dans_colonne(password, pseudo):
        motsDePasse= cursor.execute("SELECT mdp FROM compte WHERE Pseudo=?",(pseudo,)).fetchone()[0]
        if motsDePasse==password:
            return True
        else:
            return False
        
    #fonction de connection
    def login():
        global username,connexion_statut,btn_state
        username = entry_username.get()
        password = entry_password.get()

        if username_existe_dans_colonne(username) == True: 
            if password_existe_dans_colonne(password, username) == True:
                fenetre_compte.fenetre_enlever()
                """mettre à jour le bandeau"""
                connexion_statut=True
                NavBar.destroy()
                frame.destroy()
                btn_state=False
                bandeau(fenetre_page_principal.fenetre,"fenetre_page_principal")
                db.execute("UPDATE compte SET statut_connexion=? WHERE statut_connexion=?",('Non','Oui'))
                db.execute("UPDATE compte SET statut_connexion=? WHERE Pseudo=?",('Oui',username))

                db.commit()
            else:
                messagebox.showerror("Erreur d'authentification", "Le mot de passe est incorrect")#erreur messagebox car mdp incorrect
        else:
            if username_existe_dans_colonne(username) == False:
                messagebox.showerror("Erreur d'authentification", "Ce compte n'existe pas")#erreur messagebox car Pseudo incorrect
            
    #création du label d'entré du Pseudo
    label_username = Label(fenetre_compte.fenetre, text="Pseudonyme:",bg="#10480d")
    label_username.pack()
    label_username.place(x=35, y=15)
    entry_username = Entry(fenetre_compte.fenetre)
    entry_username.pack()
    entry_username.place(x=35, y=40)

    #création du label mdp
    label_password = Label(fenetre_compte.fenetre, text="Mot De Passe:",bg="#10480d")
    label_password.pack()
    label_password.place(x=35, y=70)
    entry_password = Entry(fenetre_compte.fenetre, show="*")
    entry_password.pack()
    entry_password.place(x=35, y=100)

    #Bouton connection
    login_button=Bouton(fenetre_compte,80,30,4,1,'Black','#d6cfa0','#bfb88b','Se connecter','Black',('Sitka Text Semibold',11),60,140,login)
    login_button.draw_bouton()

#fonction pour se creer un compte
def inscription():

    fenetre_inscription=Fenetre(200,200,500,250,'#10480d','Inscrivez-vous',None,fenetre_page_principal.fenetre)
    fenetre_inscription.draw_fenetre()
    fenetre_inscription.fenetre.overrideredirect(True)
    quitter=Bouton(fenetre_inscription,50,25,4,2,'Black','#e73535','#d12e2e','Quitter','Black',('Sitka Text Semibold',12),145,0,fenetre_inscription.fenetre_enlever)
    quitter.draw_bouton()

    #Vérification de l'éxistence du Pseudo et mdp
    def present(mot):
        pseudo = [ nom [0] for nom in cursor.execute("SELECT Pseudo FROM compte").fetchall()]
        for i in range (len(pseudo)):
            if mot == pseudo[i]:
                return False
        return True
    #fonction pour enregister les nouveaux compte dans le csv
    def enregistrer_infos():
        global connexion_statut,btn_state
        nom = entry_nom.get()
        password = entry_password.get()
        #Ouverture du fichier CSV en mode écriture
        
        if present(nom) ==True:
            cursor.execute("INSERT INTO compte (Pseudo,Mdp,statut_connexion) VALUES (?,?,?)",(nom,password,"Oui"))
            db.commit()
            """mettre à jour le bandeau"""
            connexion_statut=True
            NavBar.destroy()
            frame.destroy()
            btn_state=False
            bandeau(fenetre_page_principal.fenetre,"fenetre_page_principal")
            
            fenetre_inscription.fenetre_enlever()
        else:
            messagebox.showerror("Erreur de création de compte", "Ce Pseudo est déjà utilisé")

    # Création des étiquettes et des champs de saisie
    nom_label = Label(fenetre_inscription.fenetre, text="Nom :", bg="#10480d")
    nom_label.grid(row=0, column=0)
    nom_label.place(x=35, y=15)
    mdp_label = Label(fenetre_inscription.fenetre, text="Mot de Passe :", bg="#10480d")
    mdp_label.grid(row=1, column=0)
    mdp_label.place(x=35, y=70)

    entry_nom = Entry(fenetre_inscription.fenetre)
    entry_nom.grid(row=0, column=1)
    entry_nom.place(x=35, y=40)
    entry_password = Entry(fenetre_inscription.fenetre)
    entry_password.grid(row=1, column=1)
    entry_password.place(x=35, y=100)

    # Création du bouton pour enregistrer les informations
    bouton_enregistrer=Bouton(fenetre_inscription,80,30,4,1,'Black','#d6cfa0','#bfb88b','Enregistrer','Black',('Sitka Text Semibold',11),60,140,enregistrer_infos)
    bouton_enregistrer.draw_bouton()


def deconnection():
    global connexion_statut,btn_state
    connexion_statut=False
    db.execute("UPDATE compte SET statut_connexion=? WHERE statut_connexion=?",('Non','Oui'))
    db.commit()
    NavBar.destroy()
    frame.destroy()
    btn_state=False
    bandeau(fenetre_page_principal.fenetre,"fenetre_page_principal")

def lvl_compte():
    print(username)
    xp=cursor.execute("SELECT xp FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]
    if xp<=250:
        lvl=1
        progress=xp/250
        return progress,lvl
    elif xp<=600:
        lvl=2
        progress=(xp-250)/350
        return progress,lvl
    elif xp<=1050:
        lvl=3
        progress=(xp-600)/450
        return progress,lvl
    elif xp<=1600:
        lvl=4
        progress=(xp-1050)/550
        return progress,lvl
    elif xp<=2250:
        lvl=5
        progress=(xp-1600)/650
        return progress,lvl
    elif xp<=3000:
        lvl=6
        progress=(xp-2250)/750
        return progress,lvl
    elif xp<=3850:
        lvl=7
        progress=(xp-3000)/850
        return progress,lvl
    elif xp<=4800:
        lvl=8
        progress=(xp-3850)/950
        return progress,lvl
    elif xp<=5850:
        lvl=9
        progress=(xp-4800)/1050 
        return progress,lvl
    elif xp<=7000:
        lvl=10
        progress=(xp-5850)/1150 
        return progress,lvl

def compte_pg():
    global btn_state
    fenetre_page_regle.fenetre_enlever()
    fenetre_jeu.fenetre_enlever()
    fenetre_page_principal.fenetre_enlever()
    fenetre_page_compte.fenetre_apparaitre()
    btn_state=False
    progressbar = customtkinter.CTkProgressBar(fenetre_page_compte.fenetre, orientation="horizontal",height=30,fg_color='gray',progress_color='black')
    progressbar.place(x=400,y=160)
    progress,lvl=lvl_compte()
    progressbar.set(progress)

    try:
        win=cursor.execute("SELECT win FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]
        loose=cursor.execute("SELECT loose FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]
        ratio=win/loose
    except:
        ratio=0


    try:
        deplacement=cursor.execute("SELECT deplacement_totaux FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]
        game=cursor.execute("SELECT nb_parties FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]
        moyen_deplacement=deplacement/gammavariate
    except:
        moyen_deplacement=0

    label_ratio_win = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Ratio de victoires : {ratio}% ", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_ratio_win.place(x=130,y=260)
    label_lvl_compte = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Niveaux du compte : {lvl}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_lvl_compte.place(x=400,y=120)
    label_game_play = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Parties jouées : {cursor.execute("SELECT nb_parties FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_game_play.place(x=130,y=320)
    label_game_win = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Parties gagner : {cursor.execute("SELECT win FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_game_win.place(x=130,y=380)
    label_game_loose = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Parties perdu : {cursor.execute("SELECT loose FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_game_loose.place(x=130,y=440)
    label_best_score = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Meilleur score : {cursor.execute("SELECT best_score FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_best_score.place(x=130,y=500)
    label_best_temps = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Meilleur temps : {cursor.execute("SELECT best_temps FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_best_temps.place(x=600,y=260)
    label_best_deplacement = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Minimun de deplacement : {cursor.execute("SELECT best_deplacement FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_best_deplacement.place(x=600,y=320)
    label_temps_total = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"temps de jeux : {cursor.execute("SELECT temps_jeu FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_temps_total.place(x=600,y=380)
    label_deplacement_moyen = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Moyenne de deplacement : {moyen_deplacement}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_deplacement_moyen.place(x=600,y=440)
    label_victoire_cons = customtkinter.CTkLabel(fenetre_page_compte.fenetre, text=f"Victoire consécutive maximun : {cursor.execute("SELECT victoire_cons FROM compte WHERE Pseudo=?",(username,)).fetchone()[0]}", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label_victoire_cons.place(x=600,y=500)
    bandeau(fenetre_page_compte.fenetre,"fenetre_page_compte")
    bouton_quitter=Bouton(fenetre_page_regle,50,50,10,2,'black','#e73535','#d12e2e','Quitter','black',('Sitka Text Semibold',30),860,10,quit)
    bouton_quitter.draw_bouton()


def regle():
    global btn_state,fenetre_page_regle
    fenetre_page_principal.fenetre_enlever()
    fenetre_page_regle.fenetre_apparaitre()
    btn_state=False
    label = customtkinter.CTkLabel(fenetre_page_regle.fenetre, text="Règles du Solitaire : \n\nAu début de la partie, vous devez commencer à créer des suites parmi les sept piles du tableau. Vous ne pouvez empiler les cartes que dans l'ordre décroissant (roi, reine, valet, 10, etc.), en alternant les couleurs (par exemple, rouge, noir, rouge, noir, etc.). \n\nIl est possible de déplacer les suites d'une pile à l'autre. Vous pouvez toujours commencer à former une pile à partir de n'importe quelle carte, pas nécessairement un roi. Lorsque vous déplacez une carte visible d'une pile, une carte cachée située en dessous est retournée pour devenir visible. C'est ainsi que vous découvrez les cartes sur le tableau lorsque vous jouez au Solitaire. \n\nQuand l'une des sept piles du tableau est vide, vous pouvez placer un roi ou une suite commençant par un roi (et uniquement un roi) sur l'emplacement libre. \n\nVous ne pouvez déplacer que les cartes ou les suites supérieures. Dans les cas où le plateau n'offre plus aucune action possible, vous pouvez introduire de nouvelles cartes dans le jeu à l'aide de la pioche.", font=('Sitka Text Semibold', 18), justify="left", wraplength=660, text_color="white")
    label.pack(padx=60, pady=60)
    bandeau(fenetre_page_regle.fenetre,"fenetre_page_regle")
    bouton_quitter=Bouton(fenetre_page_regle,50,50,10,2,'black','#e73535','#d12e2e','Quitter','black',('Sitka Text Semibold',30),860,10,quit)
    bouton_quitter.draw_bouton()

"""Creation et affichage du menu/bandeau de navigation"""
def bandeau(window,fenetre):
    global nav_icon,btn_state,close_icon,NavBar,frame,connexion_statut,username
    try:
        NavBar.destroy()
        frame.destroy()
    except:
        pass
    #Chargement des images
    nav_icon = PhotoImage(file="./images/navbar.png")
    close_icon = PhotoImage(file="images/close.png")

    #Création du frame principal
    frame = Frame(window, bg='#145810',height=40,width=500)

    frame.place(x=0,y=0)
    frame.lower()
    #Fonction pour basculer l'affichage du menu
    def switch():
        global btn_state
        if btn_state is True:
            for x in range(251):
                NavBar.place(x=-x, y=0)
                frame.update()
            frame.config(bg='#145810')
            btn_state = False
        else:
            for x in range(-250, 0):
                NavBar.place(x=x, y=0)
                frame.update()
            frame.config(bg='#145810')
            btn_state = True

    #Bouton pour ouvrir le menue
    navbar_btn = Button(frame, image=nav_icon, bg='black', bd=0, command=switch)
    navbar_btn.grid(row=1, column=1)

    #Création du menu déroulant
    NavBar = Frame(window, bg='black', height=700, width=250)
    NavBar.place(x=-250, y=0)
    NavBar.lift()



    statut_co= [co[0] for co in cursor.execute("SELECT statut_connexion FROM compte").fetchall()]
    for donnees in statut_co:
        if donnees=='Oui':
            username=cursor.execute("SELECT Pseudo FROM compte WHERE statut_connexion=?",("Oui",)).fetchone()[0]
            connexion_statut=True
            compte=Bouton(NavBar,40,40,6,1,"white",'black','#ada1a1','Compte',"white",('artel 18 bold',24),50,60,None)
            compte.draw_bouton()
    if connexion_statut==False:
        #Bouton du menue deroulant appelant des fonctions
        login=Bouton(NavBar,15,40,3,1,"white",'black','#252527','Se connecter',"white",('artel 18 bold',12),25,50,creation_compte)
        login.draw_bouton()
        register=Bouton(NavBar,15,40,3,1,"white",'black','#252527','Créer son compte',"white",('artel 18 bold',12),115,50,inscription)
        register.draw_bouton()
    else:
        compte=Bouton(NavBar,150,40,6,1,"white",'black','#ada1a1','Compte',"white",('artel 18 bold',24),50,60,compte_pg)
        compte.draw_bouton()
    
    if fenetre=="fenetre_page_regle":
        menu_btn=Bouton(NavBar,150,40,6,1,"#a09d8a",'black','#252527','Menu',"white",('artel 18 bold',24),50,150,retour)
        menu_btn.draw_bouton()
        """
        compte_btn=Bouton(NavBar,150,40,6,1,"#a09d8a",'black','#252527','Compte',"white",('artel 18 bold',24),50,200,compte_pg)
        compte_btn.draw_bouton()"""
    
    elif fenetre=="fenetre_page_principal":
        regle_btn=Bouton(NavBar,150,40,6,1,"#a09d8a",'black','#252527','Regles',"white",('artel 18 bold',24),50,150,regle)
        regle_btn.draw_bouton()
        """
        compte_btn=Bouton(NavBar,150,40,6,1,"#a09d8a",'black','#252527','Compte',"white",('artel 18 bold',24),50,200,compte_pg)
        compte_btn.draw_bouton()"""

    elif fenetre=="fenetre_page_compte":
        menu_btn=Bouton(NavBar,150,40,6,1,"#a09d8a",'black','#252527','Menu',"white",('artel 18 bold',24),50,150,retour)
        menu_btn.draw_bouton()
        regle_btn=Bouton(NavBar,150,40,6,1,"#a09d8a",'black','#252527','Regles',"white",('artel 18 bold',24),50,200,regle)
        regle_btn.draw_bouton()
    deconnection_btn=Bouton(NavBar,40,40,6,1,"#a09d8a",'black','#252527','Se Deconnecter',"white",('artel 18 bold',24),35,600,deconnection)
    deconnection_btn.draw_bouton()



    #Bouton pour fermer le menu
    close_btn = Button(NavBar, image=close_icon, bg='black', bd=0, command=switch)
    close_btn.place(x=200, y=5)

bandeau(fenetre_page_principal.fenetre,"fenetre_page_principal")



def jeux():
    global fenetre_jeu
    fenetre_page_principal.fenetre_enlever()
    fenetre_jeu.fenetre_apparaitre()

    mon_dictionnaire_carte = {"As de PIQUE": r"images\Jeux_de_carte\ace_of_spades.png", "2 de PIQUE": r"images\Jeux_de_carte\2_of_spades.png", "3 de PIQUE": r"images\Jeux_de_carte\3_of_spades.png", "4 de PIQUE": r"images\Jeux_de_carte\4_of_spades.png", "5 de PIQUE": r"images\Jeux_de_carte\5_of_spades.png", "6 de PIQUE": r"images\Jeux_de_carte\6_of_spades.png", "7 de PIQUE": r"images\Jeux_de_carte\7_of_spades.png", "8 de PIQUE": r"images\Jeux_de_carte\8_of_spades.png", "9 de PIQUE": r"images\Jeux_de_carte\9_of_spades.png", "10 de PIQUE": r"images\Jeux_de_carte\10_of_spades.png", "Valet de PIQUE": r"images\Jeux_de_carte\jack_of_spades2.png", "Dame de PIQUE": r"images\Jeux_de_carte\queen_of_spades2.png", "Roi de PIQUE": r"images\Jeux_de_carte\king_of_spades2.png", "As de COEUR": r"images\Jeux_de_carte\ace_of_hearts.png", "2 de COEUR": r"images\Jeux_de_carte\2_of_hearts.png", "3 de COEUR": r"images\Jeux_de_carte\3_of_hearts.png", "4 de COEUR": r"images\Jeux_de_carte\4_of_hearts.png", "5 de COEUR": r"images\Jeux_de_carte\5_of_hearts.png", "6 de COEUR": r"images\Jeux_de_carte\6_of_hearts.png", "7 de COEUR": r"images\Jeux_de_carte\7_of_hearts.png", "8 de COEUR": r"images\Jeux_de_carte\8_of_hearts.png", "9 de COEUR": r"images\Jeux_de_carte\9_of_hearts.png", "10 de COEUR": r"images\Jeux_de_carte\10_of_hearts.png", "Valet de COEUR": r"images\Jeux_de_carte\jack_of_hearts2.png", "Dame de COEUR": r"images\Jeux_de_carte\queen_of_hearts2.png", "Roi de COEUR": r"images\Jeux_de_carte\king_of_hearts2.png", "As de CARREAU": r"images\Jeux_de_carte\ace_of_diamonds.png", "2 de CARREAU": r"images\Jeux_de_carte\2_of_diamonds.png", "3 de CARREAU": r"images\Jeux_de_carte\3_of_diamonds.png", "4 de CARREAU": r"images\Jeux_de_carte\4_of_diamonds.png", "5 de CARREAU": r"images\Jeux_de_carte\5_of_diamonds.png", "6 de CARREAU": r"images\Jeux_de_carte\6_of_diamonds.png", "7 de CARREAU": r"images\Jeux_de_carte\7_of_diamonds.png", "8 de CARREAU": r"images\Jeux_de_carte\8_of_diamonds.png", "9 de CARREAU": r"images\Jeux_de_carte\9_of_diamonds.png", "10 de CARREAU": r"images\Jeux_de_carte\10_of_diamonds.png", "Valet de CARREAU":r"images\Jeux_de_carte\jack_of_diamonds2.png", "Dame de CARREAU": r"images\Jeux_de_carte\queen_of_diamonds2.png", "Roi de CARREAU": r"images\Jeux_de_carte\king_of_diamonds2.png", "As de TREFLE": r"images\Jeux_de_carte\ace_of_clubs.png", "2 de TREFLE": r"images\Jeux_de_carte\2_of_clubs.png", "3 de TREFLE": r"images\Jeux_de_carte\3_of_clubs.png", "4 de TREFLE": r"images\Jeux_de_carte\4_of_clubs.png", "5 de TREFLE": r"images\Jeux_de_carte\5_of_clubs.png", "6 de TREFLE": r"images\Jeux_de_carte\6_of_clubs.png", "7 de TREFLE": r"images\Jeux_de_carte\7_of_clubs.png", "8 de TREFLE": r"images\Jeux_de_carte\8_of_clubs.png", "9 de TREFLE": r"images\Jeux_de_carte\9_of_clubs.png", "10 de TREFLE": r"images\Jeux_de_carte\10_of_clubs.png", "Valet de TREFLE": r"images\Jeux_de_carte\jack_of_clubs.png", "Dame de TREFLE": r"images\Jeux_de_carte\queen_of_diamonds2.png", "Roi de TREFLE": r"images\Jeux_de_carte\king_of_clubs2.png"}

    mon_paquet = [a for a in mon_dictionnaire_carte.items()]
    Pioche = Pile()
    Pile1=Pile()
    Pile2=Pile()
    Pile3=Pile()
    Pile4=Pile()
    Pile5=Pile()
    Pile6=Pile()
    Pile7=Pile()
    Pile_paquet_1=Pile()
    Pile_paquet_2=Pile()
    Pile_paquet_3=Pile()
    Pile_paquet_4=Pile()

    for i in range(0,24):
        choix=randint(0,len(mon_paquet)-1)
        Pioche.empiler(mon_paquet[choix])
        del mon_paquet[choix]
    
    different_pile_drop=[Pile1,Pile2,Pile3,Pile4,Pile5,Pile6,Pile7]
    nb_carte=2
    for i in range(7):
        for j in range(1,nb_carte):
            choix=randint(0,len(mon_paquet)-1)
            different_pile_drop[i].empiler(mon_paquet[choix])
            del mon_paquet[choix]
        nb_carte+=1


    pioche_retourne= Pile()
    
    def retourn_pioche(event):
        global add_dragable
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
        

        
        
        
        def add_dragable(): 
            try:
                pioche_retourne_position.del_label(1)
            except:
                pass
            pioche_retourne_position.positionner_cartes()
            
        ###
        add_dragable()
        pioche()

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
        liste=File()
        liste_jeu=File()
        def __init__(self,widget,fenetre,pioche,drop,drag):
            self.drag=drag
            self.drop=drop
            self.pioche=pioche
            self.widget=widget
            self.fenetre=fenetre
            
            if self.drag==True:
                
                if DragAndDrop.liste.est_vide()==False:
                    DragAndDrop.liste.defiler().destroy()
                DragAndDrop.liste.enfiler(self.widget)

                self.widget=DragAndDrop.liste.bout_file()
                self.set_drag(self.widget)

            if self.drop==True:
                DragAndDrop.list_drop.append(self.widget)
                DragAndDrop.pile_list_drop.append(self.pioche)
                

        def set_drag(self,widget):
            self.widget.bind("<Button-1>",self.on_click_start)
            self.widget.bind("<B1-Motion>",self.on_click)
            self.widget.bind("<ButtonRelease-1>",self.on_drop)
            self.widget["cursor"] = "hand1"
            
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
                    try:
                        self.widget.place(x=coord_target_x,y=coord_target_y)
                        pile=DragAndDrop.pile_list_drop[DragAndDrop.list_drop.index(target)]
                        pile.empiler(self.pioche.sommet(1))
                        self.pioche.depiler()

                        
                        self.pioche=pile
                        widget_dropped = True
                        DragAndDrop.liste_jeu.changement_file(DragAndDrop.liste)
                        pioche_retourne_position.nb_carte_afficher()
                        add_dragable()
                        
                    except Exception as e:
                        print(f"Error occurred: {e}")
            if not widget_dropped:
                self.widget.place(x=self.widget_x, y=self.widget_y)
                pioche_retourne_position.del_label(0)


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
                


    pioche_retourne_position=PileAffichage(pioche_retourne,fenetre_jeu.fenetre,200,50,30,3)

    def zone_drop():
        global pile_zone1,pile_zone2,pile_zone3,pile_zone4,pile_zone5,pile_zone6,pile_zone7
        zone1=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone2=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone3=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone4=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone5=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone6=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        zone7=customtkinter.CTkLabel(fenetre_jeu.fenetre, text="",height=148,width=98)
        pile_zone1=Pile()
        pile_zone2=Pile()
        pile_zone3=Pile()
        pile_zone4=Pile()
        pile_zone5=Pile()
        pile_zone6=Pile()
        pile_zone7=Pile()
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
    bouton_quitter=Bouton(fenetre_jeu,50,50,10,2,'black','#e73535','#d12e2e','Quitter','black',('Sitka Text Semibold',30),860,10,quit)
    bouton_quitter.draw_bouton()


#Bouton de Jeu
bouton_jouer=Bouton(fenetre_page_principal,50,50,10,1,'#247c26','#36c170','#358f5a','Jouer','white',('Sitka Text Semibold',30),450,330,jeux)
bouton_jouer.draw_bouton()


mainloop()
