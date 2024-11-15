 Répartition des tâches

 *GANDEBE MARIUS (20B178FS)*
Tache: Implémentation de la fonction `compter_sous_chaines_palindromiques`.
def compter_sous_chaines_palindromiques(chaine):
    n = len(chaine)
    compteur_palindromes = 0

     Parcourir toutes les sous-chaînes possibles
    for i in range(n):  # Position de départ de la sous-chaîne
        for j in range(i, n):  # Position de fin de la sous-chaîne
            sous_chaine = chaine[i:j+1]  # Extraire la sous-chaîne de i à j inclus
            if est_palindrome(sous_chaine):  # Vérifier si la sous-chaîne est un palindrome
                compteur_palindromes += 1  # Incrémenter le compteur si c'est un palindrome

    return compteur_palindromes
Cette fonction parcourt toutes les sous-chaînes possibles d'une chaîne donnée, en vérifiant si chacune est un palindrome à l'aide de la fonction est_palindrome. Si c'est le cas, elle incrémente un compteur pour suivre le nombre total de sous-chaînes palindromiques.

 *YOUSSOUFOU YAYA (22B099FS)*
Tache:  Développement de la fonction `est_palindrome`.
  def est_palindrome(sous_chaine):
    return sous_chaine == sous_chaine[::-1]
La fonction est_palindrome vérifie si une sous-chaîne donnée est un palindrome en la comparant avec sa version inversée. L'opérateur [::-1] permet d'inverser la chaîne. Si la chaîne est identique à sa version inversée, c'est un palindrome.

 *HOUSSEINI ABDOURAHMAN (22A816FS)*
Tache: Écriture des tests et des exemples d’utilisation avec des chaînes comme "abba".

 Exemple d'utilisation

```python
chaine = "abba"
resultat = compter_sous_chaines_palindromiques(chaine)
print("Le nombre total de sous-chaînes palindromiques est:", resultat)
# Résultat attendu : 6 (a, b, b, a, bb, abba)
