# Chiffrement Polybe 

Ce dépôt contient un petit script Python qui chiffre une chaîne de caractères en utilisant le carré de Polybe . Le script fourni présente une implémentation simple et pédagogique adaptée aux alphabets latins de base, en traitant la lettre **J** comme équivalente de **I** (convention courante pour les carrés de Polybe à 5×5).

---

## Présentation

Le chiffrement de Polybe transforme chaque lettre en deux chiffres correspondant à sa position (ligne, colonne) dans une grille 5×5. Ici :

* Les lignes et colonnes sont numérotées de `1` à `5`.
* L'alphabet utilisé est l'alphabet latin majuscule sans la lettre `J` (donc `A`..`I`, `K`..`Z`).
* La lettre `J` est traitée comme `I` pour que la grille tienne dans 25 cases.
* Les espaces sont conservés tels quels dans le texte chiffré.

---

## Fichiers

* `README.md` : ce fichier d'explication et d'utilisation.
* `polybe.py` (ou le script principal) : contient l'implémentation Python fournie.

---

## Fonctions principales (explication du code)

Le script contient les fonctions suivantes :

* `first_char(n)` :

  * Entrée : `n` (position numérique de la lettre dans l'alphabet réduit à 25 lettres, indexé à 1).
  * Retour : numéro de la **ligne** dans la grille 5×5 (entier entre 1 et 5).
  * Calcul : `return (5 + n - 1) // 5` (division entière qui ramène `n` à la ligne correspondante).

* `second_char(n)` :

  * Entrée : `n`.
  * Retour : numéro de la **colonne** dans la grille (entier entre 1 et 5).
  * Calcul : `return ((n - 1) % 5) + 1`.

* `get_letter_number(letter)` :

  * Entrée : `letter` (caractère alphabétique).
  * Retour : position `n` dans l'alphabet réduit (1..25), en considérant `J` comme `I`.
  * Comportement : met la lettre en majuscule, remplace `J` par la valeur associée à `I` (9), puis parcourt la chaîne `alphabet` pour trouver l'indice.

* `polybe(letters)` :

  * Entrée : `letters` (chaîne de caractères en clair).
  * Retour : chaîne chiffrée composée de paires de chiffres et d'espaces.
  * Comportement : pour chaque caractère non espace, obtient `n` via `get_letter_number` et concatène `first_char(n)` puis `second_char(n)`.

* Variable `alphabet` : initialisée comme `string.ascii_uppercase` puis modifiée pour exclure la lettre `J` afin d'obtenir le jeu de 25 lettres attendu par un carré de Polybe 5×5.

---

## Exemple d'utilisation

Exécution typique (ligne de commande) :

```bash
$ python polybe.py
Entrez une chaîne de caractères : Bonjour
Texte chiffré : 12343324344542
```

Explication de l'exemple : chaque lettre de `Bonjour` a été convertie en une paire de chiffres selon sa position dans la grille.

---

## Améliorations possibles

Voici quelques améliorations recommandées si vous souhaitez rendre le script plus robuste ou complet :

1. **Validation d'entrée** : filtrer et gérer les caractères non alphabétiques (chiffres, ponctuation), ou normaliser les accents (`é` → `E`) avant le chiffrement.
2. **Déchiffrement** : ajouter une fonction réciproque (`unpolybe`) pour convertir une séquence de chiffres en texte clair.
3. **Tests unitaires** : fournir des tests automatisés (avec `unittest` ou `pytest`) couvrant les cas normaux et limites.
4. **Options CLI** : permettre l'utilisation via arguments (ex. `--decrypt`, `--input "..."`, `--ignore-punctuation`).
5. **Support d'autres conventions** : proposer des variantes où `J` n'est pas fusionné avec `I` (par ex. en utilisant une grille 6×6 incluant chiffres), ou permettre de choisir la convention.

---

## Licence

Ce projet est fourni à titre pédagogique. Vous pouvez le réutiliser et le modifier librement. Si vous souhaitez appliquer une licence formelle, ajoutez un fichier `LICENSE` avec la licence désirée (ex. MIT, Apache-2.0).

---

## Remarques finales

Le code fourni est volontairement simple pour favoriser la compréhension du principe du carré de Polybe. Pour un usage en production ou éducatif plus poussé, il est recommandé d'appliquer les améliorations listées ci-dessus et d'ajouter des commentaires, la gestion d'erreurs et des tests.
