# Demande à l'utilisateur d'entrer une phrase.
phrase = input("Entrez une phrase: ")
# Divise la phrase en mots en utilisant l'espace comme séparateur et compte le nombre de mots
espace = 0
for i in phrase:
    if i==' ':
        espace+=1
# Affiche le nombre de mots dans la phrase
print(f"La phrase contient {espace+1} mots.")
# Affiche la phrase en lettres majuscules
maj = phrase.upper()
print(f"Phrase en majuscules: {maj}")