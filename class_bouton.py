from tkinter import*
import customtkinter

class Bouton:
    def __init__(self,fenetre,hauteur,largeur,angle_coint,bordure_taille,bordure_couleur,fg_color,hover_color,text,text_couleur,text_font,x,y,command):
        try:
            self.fenetre=fenetre.fenetre
        except:
            self.fenetre=fenetre
        self.hauteur=hauteur
        self.largeur=largeur
        self.angle_coint=angle_coint
        self.bordure_px=bordure_taille
        self.bordure_couleur=bordure_couleur
        self.fg_color=fg_color
        self.hover_color=hover_color
        self.text=text
        self.text_couleur=text_couleur
        self.text_font=text_font
        self.x=x
        self.y=y
        self.command=command
    def draw_bouton(self):
        bouton=customtkinter.CTkButton(self.fenetre,width=self.hauteur,height=self.largeur,corner_radius=self.angle_coint,border_width=self.bordure_px,border_color=self.bordure_couleur,fg_color=self.fg_color,hover_color=self.hover_color,text=self.text,text_color=self.text_couleur,font=self.text_font,command=self.command)
        bouton.place(x=self.x,y=self.y)

