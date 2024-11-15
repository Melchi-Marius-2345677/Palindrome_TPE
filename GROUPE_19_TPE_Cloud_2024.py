# Fonction qui vérifie si une sous-chaîne est un palindrome
def est_palindrome(sous_chaine):
    return sous_chaine == sous_chaine[::-1]

# Fonction principale qui compte le nombre de sous-chaînes palindromiques dans une chaîne
def compter_sous_chaines_palindromiques(chaine):
    n = len(chaine)
    compteur_palindromes = 0

    # Parcourir toutes les sous-chaînes possibles
    for i in range(n):  # Position de départ de la sous-chaîne
        for j in range(i, n):  # Position de fin de la sous-chaîne
            sous_chaine = chaine[i:j+1]  # Extraire la sous-chaîne de i à j inclus
            if est_palindrome(sous_chaine):  # Vérifier si la sous-chaîne est un palindrome
                compteur_palindromes += 1  # Incrémenter le compteur si c'est un palindrome

    return compteur_palindromes

# Exemple d'utilisation
chaine = "abba"
resultat = compter_sous_chaines_palindromiques(chaine)
print("Le nombre total de sous-chaînes palindromiques est:", resultat)
