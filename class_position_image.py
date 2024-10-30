class PileAffichage:
    def __init__(self, pile, fenetre, coord_x=31, coord_y=331, ecart=20):
        self.pile = pile
        self.fenetre = fenetre
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.ecart = ecart
        self.labels = []
        self.last_pile_size = 0  # Pour garder la trace de la taille précédente de la pile

    def positionner_cartes(self):
        # Vérifiez si la pile a changé avant de mettre à jour les labels
        if self.pile.taille() == self.last_pile_size:
            print("La pile n'a pas changé, pas de mise à jour nécessaire.")
            return

        # Effacez les labels existants
        for label in self.labels:
            label.destroy()
        self.labels.clear()

        # Mettez à jour chaque carte de la pile avec un nouveau label
        for i in range(self.pile.taille()):
            image_label = customtkinter.CTkLabel(self.fenetre, text="")
            image_label.place(x=self.coord_x, y=self.coord_y + i * self.ecart)
            self.labels.append(image_label)

            image_path = self.pile.sommet(self.pile.taille() - i)[1]
            image = customtkinter.CTkImage(Image.open(image_path), size=(100, 150))
            image_label.configure(image=image)

            # Ajoutez le DragAndDrop uniquement au sommet de la pile
            if i == self.pile.taille() - 1:
                DragAndDrop(image_label, self.fenetre, self.pile, drop=False, drag=True)

        # Mettez à jour la taille de la pile pour éviter les duplications lors des prochains appels
        self.last_pile_size = self.pile.taille()

        print(f"Labels mis à jour : {self.labels}")
