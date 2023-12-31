from enum import Enum
import random

from simulation_constants import *
from animal import *
from grille_animaux import *

def simulation_est_terminee(grille):
    # TODO: Vérifier si la simulation est terminée.
    # Elle se termine lorsque le nombre de proies ou le nombre de prédateurs est égal à zéro.
    # Renvoyer un booléen indiquant l'état de la simulation.
    return grille["nb_proies"] == 0 or grille["nb_predateurs"] == 0


def rendre_animaux_disponibles(grille):
    # TODO: Parcourir chaque case de la grille et rendre tous les animaux disponibles (Booléen à True) pour la prochaine itération.
    for i in range(len(grille["matrice"])):
        for j in range(len(grille["matrice"][i])):
            if grille["matrice"][i][j]["animal"]:
                definir_disponibilite(grille["matrice"][i][j]["animal"],True)


def deplacer_animal(grille, ligne, col, animal):
    # TODO: Trouver un voisin vide où déplacer l'animal, effectuer le déplacement et mettre à jour l'état
    # et la disponibilité de l'animal. Utiliser "choix_voisin_autour", "definit_etat", "definir_animal",
    # "definir_disponibilite" et "vider_case" pour réaliser ces étapes.
    nb_v,x,y = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
    definit_etat(grille,obtenir_etat(grille, ligne, col),x,y)
    definir_animal(grille,animal,x,y)
    definir_disponibilite(animal,False)
    vider_case(grille,ligne,col)


def executer_cycle_proie(grille, ligne, col, animal):
    # TODO: Gérer le cycle de vie d'une proie à une position donnée sur la grille.
    # 1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PROIE, le retirer de la grille et décrémenter le compteur de proies.
    animal["age"] += NB_JRS_PUBERTE_PROIE
    # 2. Si l'animal est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PROIE), tenter de générer un nouveau bébé proie.
    if animal["age"] > MAX_AGE_PROIE:
        vider_case(grille,ligne,col)
        decrementer_nb_proies(grille)
    elif obtenir_age(animal) >= NB_JRS_PUBERTE_PROIE and obtenir_jours_gestation(animal) >= NB_JRS_GESTATION_PROIE:
        nv,x,y = choix_voisin_autour(grille,ligne,col,Contenu.VIDE)
        if (x!=None and y!=None) and grille["nb_proies"] < NB_MAX_PROIES:
            case = creer_case(Contenu.PROIE,creer_animal())
            definir_case(grille,case,x,y)
            incrementer_nb_proies(grille)
        definir_jours_gestation(animal,0)
    else:
        deplacer_animal(grille,ligne,col,animal)
    #    Pour ce faire, chercher un voisin vide autour de la proie. Si un voisin est trouvé, créer un bébé proie et le placer dans la grille.
    # 3. Sinon, déplacer l'animal vers une case vide à proximité.


def executer_cycle_predateur(grille, ligne, col, animal):
    # TODO: Gérer le cycle de vie d'un prédateur à une position donnée sur la grille.
    # 1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PRED ou si le prédateur manque d'énergie (énergie < MIN_ENERGIE), le retirer
    #    de la grille et décrémenter le compteur de prédateurs.
    animal["age"] += NB_JRS_PUBERTE_PRED
    # 2. Si le prédateur peut manger une proie dans une case voisine, le faire en le déplaçant dans la case de la proie et en
    #    incrémentant son énergie de AJOUT_ENERGIE (n'oubliez pas de décrémenter le compteur de proies). Après avoir mangé, si le
    #    prédateur est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PRED), tenter de générer un nouveau bébé
    #    prédateur. Pour ce faire, chercher un voisin vide autour du prédateur. Si un voisin est trouvé, créer un bébé prédateur et
    #    le placer dans la grille.
    if animal["energie"] < MIN_SANTE_PRED or animal["age"] > MAX_AGE_PRED:
        vider_case(grille,ligne,col)
        decrementer_nb_predateurs(grille)
        return
    nb_proies,x,y = choix_voisin_autour(grille,ligne,col,Contenu.PROIE)
    if x != None and y != None:
        definir_disponibilite(animal,False)
        ajouter_energie(animal,AJOUT_ENERGIE)
        definir_case(grille,creer_case(Contenu.PREDATEUR,animal),x,y)
        vider_case(grille,ligne,col)
        decrementer_nb_proies(grille)
        if animal["age"] >= NB_JRS_PUBERTE_PRED and animal["jrs_gestation"] >= NB_JRS_GESTATION_PRED:
            definir_jours_gestation(animal,0)
            definir_animal(grille,animal,x,y)
            a,x2,y2 = choix_voisin_autour(grille,x,y,Contenu.VIDE)
            if x2 != None and y2 != None:
                definir_case(grille,creer_case(Contenu.PREDATEUR,creer_animal()),x2,y2)
                incrementer_nb_predateurs(grille)
    else:
        ajouter_energie(animal,-1)
        deplacer_animal(grille,ligne,col,animal)

    # 3. Sinon, déplacer l'animal vers une case vide à proximité et décrémenter son énergie de 1.
    


def executer_cycle(grille):
    # TODO: Marquer tous les animaux comme disponibles pour ce cycle, puis parcourir la grille pour exécuter la bonne procédure
    # du cycle de vie pour chaque animal. Il est nécessaires d'utiliser au minimum les fonctions "rendre_animaux_disponibles",
    # "executer_cycle_proie" et "executer_cycle_predateur".
    rendre_animaux_disponibles(grille)
    for i in range(grille["nb_lignes"]):
        for j in range(grille["nb_colonnes"]):
            if obtenir_etat(grille,i,j) != Contenu.VIDE and obtenir_animal(grille,i,j) != None:
                animal = obtenir_animal(grille,i,j)
                if obtenir_disponibilite(animal):
                    if obtenir_etat(grille,i,j) == Contenu.PROIE:
                        executer_cycle_proie(grille,i,j,animal)
                    else:
                        executer_cycle_predateur(grille,i,j,animal)
    
