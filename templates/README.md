# templates/

## Rôle
Contient les pages HTML de l'application. Flask cherche les gabarits dans ce
dossier quand `app.py` appelle `render_template()`.

## Fichiers
| Fichier | Responsabilité |
|---|---|
| `index.html` | Interface de la calculatrice : l'écran d'affichage, les boutons (chiffres, opérateurs, C, =) et deux fonctions JavaScript (`appendToDisplay`, `clearDisplay`) qui construisent l'expression dans le navigateur. |

## Fonctionnement
1. Les boutons ajoutent des caractères dans le champ `display` (côté client).
2. Le bouton `=` soumet le formulaire en POST à la route `/`.
3. `app.py` évalue l'expression et renvoie la page avec le résultat dans
   `{{ result }}`.

## Dépendances et hypothèses
- Utilise le moteur de gabarits Jinja2 (inclus avec Flask) pour `{{ result }}`
  et `url_for()`.
- La feuille de style est chargée depuis `static/style.css` avec
  `url_for('static', filename='style.css')`.
- Le champ du formulaire doit s'appeler `display`, car c'est le nom que lit
  `app.py`.
