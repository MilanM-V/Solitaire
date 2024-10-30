class Carte:
    coeur_rouge = {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13, "Rouge": 14}
    pique_noir = {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13, "Noir": 15}
    carreau_rouge = {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13, "Rouge": 14}
    trefle_noir = {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13, "Noir": 15}
    
    def __init__(self,valeur,symbole,couleur):
        self.valeur=valeur
        self.symbole=symbole
        self.couleur=couleur
       
    def different(self,x):
        if x.symbole=='Pique' and self.symbole=='Coeur' and self.coeur_rouge[self.couleur] != self.pique_noir[x.couleur]:
            print(True)
        elif x.symbole=='Trefle' and self.symbole=='Coeur' and self.coeur_rouge[self.couleur] != self.trefle_noir[x.couleur]:
            print(True)
        elif x.symbole=='Pique' and self.symbole=='Carreau' and self.carreau_rouge[self.couleur] != self.pique_noir[x.couleur]:
            print(True)
        elif x.symbole=='Trefle' and self.symbole=='Carreau' and self.carreau_rouge[self.couleur] != self.trefle_noir[x.couleur]:
            print(True)
        elif x.symbole=='Coeur' and self.symbole=='Pique' and self.pique_noir[self.couleur] != self.coeur_rouge[x.couleur]:
            print(True)
        elif x.symbole=='Coeur' and self.symbole=='Pique' and self.pique_noir[self.couleur] != self.coeur_rouge[x.couleur]:
            print(True)
        elif x.symbole=='Carreau' and self.symbole=='Trefle' and self.trefle_noir[self.couleur] != self.carreau_rouge[x.couleur]:
            print(True)
        elif x.symbole=='Carreau' and self.symbole=='Trefle' and self.trefle_noir[self.couleur] != self.carreau_rouge[x.couleur]:
            print(True)

        elif x.symbole=='Carreau' and self.symbole=='Coeur' and self.coeur_rouge[self.couleur] == self.carreau_rouge[x.couleur]:
            print(False)
        elif x.symbole=='Carreau' and self.symbole=='Coeur' and self.coeur_rouge[self.couleur] == self.carreau_rouge[x.couleur]:
            print(False)
        elif x.symbole=='Coeur' and self.symbole=='Carreau' and self.carreau_rouge[self.couleur] == self.coeur_rouge[x.couleur]:
            print(False)
        elif x.symbole=='Coeur' and self.symbole=='Carreau' and self.carreau_rouge[self.couleur] == self.coeur_rouge[x.couleur]:
            print(False)
        elif x.symbole=='Trefle' and self.symbole=='Pique' and self.pique_noir[self.couleur] != self.trefle_noir[x.couleur]:
            print(False)
        elif x.symbole=='Trefle' and self.symbole=='Pique' and self.pique_noir[self.couleur] != self.trefle_noir[x.couleur]:
            print(False)
        elif x.symbole=='Pique' and self.symbole=='Trefle' and self.trefle_noir[self.couleur] != self.pique_noir[x.couleur]:
            print(False)
        elif x.symbole=='Pique' and self.symbole=='Trefle' and self.trefle_noir[self.couleur] != self.pique_noir[x.couleur]:
            print(False)


        else:
            print(False)

    def plus_petit_que(self,autre):
        if self.mon_dictionnaire[self.valeur] < self.mon_dictionnaire[autre.valeur]:
            print(True)
        else:
            print(False)
    
    def afficher(self):
        print(f"{self.valeur} de {self.symbole} {self.couleur}")
    
carte1 = Carte("8","Coeur","Rouge")
carte2 = Carte("Roi","Pique","Noir")
carte3 = Carte("Valet","Carreau","Rouge")
carte4 = Carte("As","Trefle","Noir")

carte4.different(carte1)

carte1.afficher()
carte2.afficher()