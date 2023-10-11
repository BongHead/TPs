from enum import Enum
import random

from simulation_constants import *
from animal import *


class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2


def creer_case(etat=Contenu.VIDE, animal=None):
    # TODO: Créer et retourner un dictionnaire représentant une case. Utiliser les arguments pour initialiser l'état et l'animal dans la case.
    return {"etat":etat,"animal":animal}


def creer_grille(nb_lignes, nb_colonnes):
    # TODO: Créer une matrice 2D de cases vides et la retourner sous forme de dictionnaire
    # TODO: Dans le dictionnaire, ajouter des métadonnées décrites dans l'énoncé (nombre de proies, de prédateurs, etc.)
    return {"matrice":[[creer_case() for i in range(nb_colonnes)]for i in range(nb_lignes)], "nb_proies":0,"nb_predateurs":0,"nb_lignes":nb_lignes,"nb_colonnes":nb_colonnes}


def obtenir_population(grille):
    # TODO: Retourner un tuple contenant le nombre actuel de proies et de prédateurs dans la grille (Tuple[Int, Int])
    return grille["nb_proies"], grille["nb_predateurs"]


def obtenir_dimensions(grille):
    # TODO: Retourner un tuple avec le nombre de lignes et de colonnes de la grille (Tuple[Int, Int])
    return grille["nb_lignes"], grille["nb_colonnes"]


def obtenir_animal(grille, ligne, colonne):
    # TODO: Retourner l'animal présent dans la case aux coordonnées données (ligne, col) (Dict)
    return grille["matrice"][ligne][colonne]["animal"]


def incrementer_nb_proies(grille):
    # TODO: Augmenter le compteur du nombre de proies dans la grille de 1 (Int)
    grille["nb_proies"] += 1


def decrementer_nb_proies(grille):
    # TODO: Diminuer le compteur du nombre de proies dans la grille de 1 (Int)
    if grille["nb_proies"] > 0:
        grille["nb_proies"] -= 1


def incrementer_nb_predateurs(grille):
    # TODO: Augmenter le compteur du nombre de prédateurs dans la grille de 1 (Int)
    grille["nb_predateurs"] += 1


def decrementer_nb_predateurs(grille):
    # TODO: Diminuer le compteur du nombre de prédateurs dans la grille de 1 (Int)
    if grille["nb_predateurs"] > 0:
        grille["nb_predateurs"] -= 1


def check_nb_proies(grille, max_val):
    # TODO: Vérifier si le nombre actuel de proies dans la grille est inférieur à max_val (Booléen)
    return grille["nb_proies"] < max_val


def vider_case(grille, ligne, col):
    # TODO: Écraser la case située à la ligne et la colonne données avec une case vide
    grille["matrice"][ligne][col]["etat"] = Contenu.VIDE
    grille["matrice"][ligne][col]["animal"] = None


def definit_etat(grille, etat, ligne, col):
    # TODO: Mettre à jour l'état de la case située à la ligne et la colonne données.
    # Utiliser le paramètre 'etat', qui est une valeur de l'Enum Contenu (VIDE, PROIE, PREDATEUR).
    grille["matrice"][ligne][col]["etat"] = etat


def definir_animal(grille, animal, ligne, col):
    # TODO: Placer un animal (sous forme de dictionnaire) sur la case indiquée par les coordonnées (ligne, col).
    grille["matrice"][ligne][col]["animal"] = animal


def obtenir_etat(grille, ligne, colonne):
    # TODO: Obtenir et retourner l'état actuel de la case à la position (ligne, col).
    # Le type de retour est une valeur de l'Enum Contenu (VIDE, PROIE, PREDATEUR).
    return grille["matrice"][ligne][colonne]["etat"]

def obtenir_case(grille, ligne, colonne):
    return grille["matrice"][ligne][colonne]

def definir_case(grille, case, ligne, col):
    grille["matrice"][ligne][col] = case


def generer_entier(min_val, max_val):
    # TODO: Utiliser une librairie pour générer un nombre entier aléatoire entre min_val et max_val inclus.
    # Le résultat doit être un entier.
    return random.randint(min_val,max_val+1)



def ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col):
    # TODO: Ajuster la position (ligne, colonne) pour une grille circulaire en utilisant les dimensions de la grille.
    # Indice: Un modulo (%) peut être utile.
    '''
    if lig < 0:
        lig += dim_lig
    elif lig >= dim_lig:
        while lig >= dim_lig:
            lig -= dim_lig
        
    if col < 0:
        col += dim_col
    elif col >= dim_col:
        while col >= dim_col:
            col -= dim_col
    '''
    lig %= dim_lig
    col %= dim_col
    return lig, col


def choix_voisin_autour(grille, ligne, col, contenu: Contenu):
    # TODO: Chercher tous les voisins autour de la cellule (ligne, col) qui correspondent au "contenu" donné (Enum).
    # TODO: Renvoyer le nombre total de ces voisins, ainsi que les coordonnées d'un voisin choisi aléatoirement (Tuple).
    #       Si le contenu n'est pas VIDE, le voisin doit être disponible (voir la fonction obtenir_disponibilite).
    # Indice: Utiliser la fonction "ajuster_position_pour_grille_circulaire" pour ajuster les positions des voisins qui sont en dehors de la grille.
    lig_voisin = None
    col_voisin = None
    tabcases = []
    nb_ligne, nb_col = obtenir_dimensions(grille)
    for i in range(ligne-1,ligne+2):
        for j in range(col-1,col+2):
            if i != ligne or j != col:
                i2,j2 = ajuster_position_pour_grille_circulaire(i,j,nb_ligne,nb_col)
                animal = obtenir_animal(grille, i2, j2)
                if obtenir_etat(grille, i2, j2) == contenu and (contenu == Contenu.VIDE or animal["disponible"]):
                    tabcases.append((i2,j2))
    
    if tabcases:
        lig_voisin, col_voisin = random.choice(tabcases)
        return len(tabcases), lig_voisin, col_voisin
    else:
        return len(tabcases), None, None


def remplir_grille(grille, pourcentage_proie, pourcentage_predateur):
    # TODO: Obtenir les dimensions de la grille.
    lig, col = obtenir_dimensions(grille)
    # TODO: Calculer le nombre total de cases dans la grille.
    cases_total = lig*col
    # TODO: Calculer le nombre de proies à placer dans la grille.
    nbr_proies = int(cases_total*pourcentage_proie)
    # TODO: Calculer le nombre de prédateurs à placer dans la grille.
    nbr_predateurs = int(cases_total*pourcentage_predateur)
    # TODO: Générer et mélanger aléatoirement la liste de toutes les positions possibles.
    pos_possibles = [(i,j) for i in range(lig) for j in range(col)] #(0,0), (0,1) ... etc
    random.shuffle(pos_possibles)
    # TODO: Placer les proies dans la grille.
    for proie in range(nbr_proies):
        choix = random.choice(pos_possibles)
        pos_possibles.remove(choix)
    # Utilisez MAX_AGE_PROIE pour générer un âge aléatoire entre 0 et l'âge maximum de la proie.
        age_proie = random.randrange(0,MAX_AGE_PROIE)
    # Utilisez NB_JRS_GESTATION_PROIE et NB_JRS_PUBERTE_PROIE pour déterminer la période de gestation si la proie est en âge de procréer.
        gest_proie = random.randrange(0,NB_JRS_GESTATION_PROIE) if age_proie > NB_JRS_PUBERTE_PROIE else 0
    # TODO: Mettre à jour le compteur du nombre de proies.
        case = creer_case(Contenu.PROIE, creer_animal(age=age_proie,jrs_gestation=gest_proie,energie=MIN_ENERGIE))
        i,j = choix
        grille["matrice"][i][j] = case
        incrementer_nb_proies(grille)
    
    # TODO: Placer les prédateurs dans la grille.
    for predateur in range(nbr_predateurs):
        choix = random.choice(pos_possibles)
        pos_possibles.remove(choix)
    # Utilisez MAX_AGE_PRED pour générer un âge aléatoire entre 0 et l'âge maximum du prédateur.
        age_pred = random.randrange(0,MAX_AGE_PRED)
    # Utilisez NB_JRS_GESTATION_PRED et NB_JRS_PUBERTE_PRED pour déterminer la période de gestation si le prédateur est en âge de procréer.
        gest_pred = random.randrange(0,NB_JRS_GESTATION_PRED) if age_pred > NB_JRS_PUBERTE_PRED else 0
    # Utilisez AJOUT_ENERGIE pour initialiser la quantité d'énergie du prédateur.
        energie_pred = MIN_ENERGIE + AJOUT_ENERGIE #???
    # TODO: Mettre à jour le compteur du nombre de prédateurs.
        case = creer_animal(Contenu.PREDATEUR, creer_animal(age=age_pred,jrs_gestation=gest_pred,energie=energie_pred))
        i,j = choix
        grille["matrice"][i][j] = case
        incrementer_nb_predateurs(grille)
        