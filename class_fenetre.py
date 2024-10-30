from tkinter import *

class Fenetre:
    def __init__(self, x, y,position_x,position_y, couleur, titre,image,fenetre):
        self.largeur = x
        self.hauteur = y
        self.largeur_ecran=position_x
        self.hauteur_ecran=position_y
        self.couleur = couleur
        self.titre = titre
        if fenetre ==None:
            self.fenetre = Tk()
        else:
            self.fenetre=Toplevel(fenetre)
        self.fond=image
        self.bg_image = None
    def draw_fenetre(self):
        self.fenetre.geometry(f'{self.largeur}x{self.hauteur}+{self.largeur_ecran}+{self.hauteur_ecran}')
        self.fenetre.title(self.titre)
        if self.fond==None:
            self.fenetre.configure(bg=self.couleur)
        else:
            canvas = Canvas(self.fenetre, width=self.largeur, height=self.hauteur)
            canvas.pack()

            # Charger l'image de fond
            self.bg_image = PhotoImage(file=self.fond)

            # Afficher l'image de fond sur le Canvas
            canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
            self.fenetre.configure(bg=self.couleur)

    def fenetre_enlever(self):
        self.fenetre.withdraw()

    def fenetre_apparaitre(self):


        self.fenetre.deiconify()


