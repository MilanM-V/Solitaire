from random import *
from Pile import Pile

mon_dictionnaire_carte = {"As de PIQUE": 1, "2 de PIQUE": 2, "3 de PIQUE": 3, "4 de PIQUE": 4, "5 de PIQUE": 5, "6 de PIQUE": 6, "7 de PIQUE": 7, "8 de PIQUE": 8, "9 de PIQUE": 9, "10 de PIQUE": 10, "Valet de PIQUE": 11, "Dame de PIQUE": 12, "Roi de PIQUE": 13, "As de COEUR": 1, "2 de COEUR": 2, "3 de COEUR": 3, "4 de COEUR": 4, "5 de COEUR": 5, "6 de COEUR": 6, "7 de COEUR": 7, "8 de COEUR": 8, "9 de COEUR": 9, "10 de COEUR": 10, "Valet de COEUR": 11, "Dame de COEUR": 12, "Roi de COEUR": 13, "As de CARREAU": 1, "2 de CARREAU": 2, "3 de CARREAU": 3, "4 de CARREAU": 4, "5 de CARREAU": 5, "6 de CARREAU": 6, "7 de CARREAU": 7, "8 de CARREAU": 8, "9 de CARREAU": 9, "10 de CARREAU": 10, "Valet de CARREAU": 11, "Dame de CARREAU": 12, "Roi de CARREAU": 13, "As de TREFLE": 1, "2 de TREFLE": 2, "3 de TREFLE": 3, "4 de TREFLE": 4, "5 de TREFLE": 5, "6 de TREFLE": 6, "7 de TREFLE": 7, "8 de TREFLE": 8, "9 de TREFLE": 9, "10 de TREFLE": 10, "Valet de TREFLE": 11, "Dame de TREFLE": 12, "Roi de TREFLE": 13}

def pioche():
    ma_pioche = [a for a in mon_dictionnaire_carte.keys()]
    Pioche = Pile()
    for i in range(0,25):

        choix=randint(0,len(ma_pioche)-1)
        Pioche.empiler(ma_pioche[choix])
        del ma_pioche[choix]


