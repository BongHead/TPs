# Demande à l'utilisateur d'entrer le montant initial de l'investissement
initial = int(input("Entrez le montant initial: "))
# Demande à l'utilisateur d'entrer le taux d'intérêt annuel en pourcentage
annuel = float(input("Entrez le taux d'interet annuel (en %): "))
# Demande à l'utilisateur d'entrer le nombre d'années de l'investissement
annees = int(input("Entrez le nombre d'annees de l'investissement: "))
# Calcule le montant final en utilisant la formule de l'intérêt composé
r=annuel/100
# Affiche le montant final avec deux décimales
print(f"Montant final apres {annees} ans: {round(initial*(1+r)**annees,2)}")