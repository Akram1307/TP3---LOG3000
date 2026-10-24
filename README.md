# Calculatrice Flask (LOG3000 TP3)

**Équipe :** 21

## Description
Application web de calculatrice simple construite avec Flask (Python).
L'utilisateur compose une expression avec les boutons de la page, puis le
serveur la calcule et affiche le résultat.

### Portée
- Une expression contient **deux nombres et un seul opérateur**, par exemple
  `12*3` ou `7.5/2`.
- Opérateurs supportés : addition `+`, soustraction `-`, multiplication `*`
  et division `/`.
- Les expressions avec plusieurs opérateurs (`1+2+3`), un opérateur au début
  ou à la fin (`-5`, `5+`) ou des opérandes non numériques sont refusées et
  un message `Error: ...` est affiché.

### Structure du projet
| Élément | Rôle |
|---|---|
| `app.py` | Serveur Flask. Définit la route `/` et la fonction `calculate()` qui découpe et évalue l'expression. |
| `operators.py` | Fonctions arithmétiques (`add`, `subtract`, `multiply`, `divide`) utilisées par `app.py`. |
| `templates/` | Page HTML de la calculatrice. Voir `templates/README.md`. |
| `static/` | Feuille de style CSS. Voir `static/README.md`. |
| `tests/` | Tests automatisés. Voir `tests/README.md`. |

## Prérequis
- Python 3.8 ou plus récent
- pip
- Git

## Installation
1. Cloner le dépôt et entrer dans le dossier :
   ```bash
   git clone https://github.com/Akram1307/TP3---LOG3000.git
   cd TP3---LOG3000
   ```
2. Installer les dépendances :
   ```bash
   pip install flask pytest
   ```
   Sur macOS ou Linux, il faut parfois utiliser `pip3` et `python3` au lieu
   de `pip` et `python`.

## Utilisation
1. Lancer le serveur depuis la racine du dépôt :
   ```bash
   python app.py
   ```
2. Ouvrir http://127.0.0.1:5000 dans un navigateur.
3. Composer une expression avec les boutons, par exemple `9`, `*`, `3`.
4. Appuyer sur `=` pour l'envoyer au serveur. Le résultat (`27.0`) s'affiche
   à l'écran.
5. Appuyer sur `C` pour effacer l'écran.

Pour arrêter le serveur, faire `Ctrl+C` dans le terminal.

## Tests
Les tests se trouvent dans le dossier `tests/` et utilisent pytest.
Depuis la racine du dépôt :
```bash
python -m pytest
```
Le détail de ce que couvrent les tests est dans `tests/README.md`.

## Contribution
1. **Issues :** chaque bogue ou tâche est d'abord décrit dans une issue
   GitHub (description, étapes pour reproduire, test qui échoue) et assigné
   à un membre de l'équipe.
2. **Branches :** chaque correction de bogue se fait sur sa propre branche.
   Pour chaque issue, créer une branche à partir de `main` :
   ```bash
   git checkout main
   git pull
   git checkout -b fix/NUMERO-description-courte
   ```
3. **Commits :** des messages clairs qui expliquent le changement et
   mentionnent l'issue, par exemple `Fix subtract operand order (#2)`.
4. **Pull requests :** pousser la branche et ouvrir une PR vers `main`. La
   description indique l'issue corrigée (`Closes #2`) et montre que les tests
   passent. Un autre membre de l'équipe relit la PR avant la fusion.
5. Après la fusion, relancer toute la suite de tests sur `main`.
