"""
Générateur de données expériementales pour l'activité
Étude de la caractéristique d'un conducteur ohmnique.
Niveau : Seconde
Chapitre : 11 Électricité
"""
from random import gauss


# Fonctions
def arrondir_nombresduneliste(liste, arrondi=2):
    return [round(x, arrondi) for x in liste]


def transformer_listedenombre_en_chaine(liste):
    listechaine = "[" + ", ".join([str(element) for element in liste]) + "]"
    return listechaine


##### Programme principal
### Réglages
R = 25  # Valeur de la résistance utilisé pour le tp
Lugene = [0.0, 3.0, 4.5, 6.0, 7.5, 9.0, 12.0]  # Listes des valeurs indiqué sur le générateur de tension prévue pour le tp

U = [u + gauss(0, 0.05) for u in Lugene]  # Ajout d'une erreur aléatoire de type distribution gaussienne aux valeurs affichées sur l'appareil
I = [u / R + gauss(0, 0.015) for u in U]  # Ajout d'une erreur aléatoire de type distribution gaussienne aux valeurs de I

# Forcage du premier point à 0,0
U[0] = 0.00
I[0] = 0.00

fichier = open("ValeurExperimentaleSimule.txt", "a")
fichier.write("U =" + transformer_listedenombre_en_chaine(arrondir_nombresduneliste(U)))
fichier.write("\nI =" + transformer_listedenombre_en_chaine(arrondir_nombresduneliste(I)))
fichier.write("\n\n")
fichier.close()

print("Les données sont prètes, "
      "elles sont dans le fichier texte "
      "′ ValeurExperimentaleSimule.txt′ ")
