# tests/

## Rôle
Contient les tests automatisés de la calculatrice, écrits avec pytest.

## Lancer les tests
Prérequis : `pip install flask pytest` (voir le README principal).

Depuis la racine du dépôt :
```bash
python -m pytest
```
Pour voir le résultat de chaque test :
```bash
python -m pytest -v
```
Pour lancer un seul fichier :
```bash
python -m pytest tests/test_operators.py
```
Il faut lancer les tests depuis la racine avec `python -m pytest`, sinon
Python ne trouve pas `app.py` et `operators.py`.

## Fichiers et couverture
| Fichier | Ce qui est testé |
|---|---|
| `test_operators.py` | Les fonctions `add`, `subtract`, `multiply` et `divide` : cas simples, nombres négatifs, décimaux et division par zéro. |
| `test_calculate.py` | La fonction `calculate()` de `app.py` : un calcul par opérateur, espaces ignorés, décimaux, et expressions invalides (vide, plusieurs opérateurs, opérateur au début ou à la fin, pas d'opérateur, texte au lieu d'un nombre) qui doivent lever `ValueError`. |
| `test_app.py` | La route `/` avec le client de test de Flask : affichage de la page, résultat après un POST, message d'erreur pour une expression invalide, et texte des boutons (chiffres et opérateurs) qui doit correspondre à la valeur ajoutée à l'écran. |
