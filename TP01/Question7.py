# Demande à l'utilisateur de saisir le nombre de secondes
secondes = int(input("Entrez le nombre de secondes: "))
t_secondes = secondes
# Calcul du nombre d'années contenant ces secondes (en supposant une année de 365 jours)
annees = secondes/(86400*365)
secondes -= int(annees)*86400*365
# Calcul du nombre de semaines restantes dans le reste des secondes
semaines = secondes/(7*24*60*60)
secondes -= int(semaines)*7*24*60*60
# Calcul du nombre de jours restants dans le reste des secondes
jours = secondes/(24*60*60)
secondes -= int(jours)*24*60*60
# Calcul du nombre d'heures restantes dans le reste des secondes
heures = secondes/(60*60)
secondes -= int(heures)*60*60
# Calcul du nombre de minutes restantes dans le reste des secondes
minutes = secondes/60
secondes -= int(minutes)*60
# Affichage du nombre d'années, de semaines, de jours, d'heures, de minutes et de secondes

estAnneesNonNull   = int(annees) == 0
estSemainesNonNull = int(semaines) == 0
estJoursNonNull    = int(jours) == 0
estHeursNonNull    = int(minutes) == 0
estMinutesNonNull  = int(secondes) == 0

t_annees = f"{int(annees)} annees, "
t_semaines = f"{int(semaines)} semaines, "
t_jours = f"{int(jours)} jours, "
t_heures = f"{int(heures)} heures, "
t_minutes = f"{int(minutes)} minutes"

if estAnneesNonNull:
    t_annees = ""
if estSemainesNonNull:
    t_semaines = ""
if estJoursNonNull:
    t_jours = ""
if estHeursNonNull:
    t_heures = ""
if estMinutesNonNull:
    t_minutes = ""

print(f"En {t_secondes} secondes, on a: {t_annees}{t_semaines}{t_jours}{t_heures}{t_minutes} et {secondes} secondes.")