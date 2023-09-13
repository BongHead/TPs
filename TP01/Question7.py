import math
# Demande à l'utilisateur de saisir le nombre de secondes
secondes = int(input("Entrez le nombre de secondes: "))
# Calcul du nombre d'années contenant ces secondes (en supposant une année de 365 jours)
annees = secondes/31536000

# Calcul du nombre de semaines restantes dans le reste des secondes
semaines = (annees - int(annees))*52

# Calcul du nombre de jours restants dans le reste des secondes
jours = (semaines - int(semaines))*7

# Calcul du nombre d'heures restantes dans le reste des secondes
heures = (jours - int(jours))*24

# Calcul du nombre de minutes restantes dans le reste des secondes
minutes = (heures - int(heures))*60
newsecondes = (minutes-int(minutes))*60
# Affichage du nombre d'années, de semaines, de jours, d'heures, de minutes et de secondes

estAnneesNonNull   = int(annees) != 0
estSemainesNonNull = int(semaines) != 0
estJoursNonNull    = int(jours) != 0
estHeursNonNull    = int(heures) != 0
estMinutesNonNull  = int(minutes) != 0

if estAnneesNonNull:
    print(f"En {secondes} secondes, on a: {int(annees)} annees, {int(semaines)} semaines, {int(jours)} jours, {int(heures)} heures, {int(minutes)} minutes et {int(newsecondes)} secondes.")
elif estSemainesNonNull:
    print(f"En {secondes} secondes, on a: {int(semaines)} semaines, {int(jours)} jours, {int(heures)} heures, {int(minutes)} minutes et {int(newsecondes)} secondes.")
elif estJoursNonNull:
    print(f"En {secondes} secondes, on a: {int(jours)} jours, {int(heures)} heures, {int(minutes)} minutes et {int(newsecondes)} secondes.")
elif estHeursNonNull:
    print(f"En {secondes} secondes, on a: {int(heures)} heures, {int(minutes)} minutes et {int(newsecondes)} secondes.")
elif estMinutesNonNull:
    print(f"En {secondes} secondes, on a: {int(minutes)} minutes et {int(newsecondes)} secondes.")