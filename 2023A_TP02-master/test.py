from enum import Enum
import random

from simulation_constants import *
from animal import *
from grille_animaux import *
from simulation_logic import *

grille = creer_grille(3, 3)
rendre_animaux_disponibles(grille)
print(grille)