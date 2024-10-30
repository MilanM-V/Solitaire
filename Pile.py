class Pile:
    instances = []
    def __init__(self,nom):
        self.contenu=[]
        Pile.instances.append(self)
        self.nom=nom

    def est_vide(self):
        if self.contenu:
            return False
        else:
            return True
    

    def empiler(self,x):
        self.contenu.append(x)

    def depiler (self):
        self.contenu.pop()

    def taille(self):
        return len(self.contenu)

    def sommet(self,i):
        return self.contenu[-i]

    def contenue(self):
        try:
            return self.contenu,self.nom
        except:
            return self.contenu
    
            
"""
pile1=Pile()

pile1.empiler(1)
pile1.empiler(9)
pile1.empiler(15)
pile1.empiler(144)

print(pile1.contenue())
pile1.depiler()
pile1.depiler()
print(pile1.sommet(1))
print(pile1.contenue())

"""