from enum import Enum
import random

from simulation_constants import *
from animal import *
from grille_animaux import *
from simulation_logic import *

	
grille = creer_grille(5, 5)
predateur = creer_animal(age=50, jrs_gestation=0, energie=50, disponible=True)
case = creer_case(Contenu.PREDATEUR, predateur)
definir_case(grille, case, 0, 0)
proie = creer_animal(age=10, jrs_gestation=0, energie=20, disponible=True)
case = creer_case(Contenu.PROIE, proie )
definir_case(grille, case, 1, 0)
incrementer_nb_proies(grille)
incrementer_nb_predateurs(grille)
executer_cycle_predateur(grille, 0, 0, predateur)
population = obtenir_population(grille)
print(population)