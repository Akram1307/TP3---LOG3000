# static/

## Rôle
Contient les fichiers statiques servis directement par Flask, sans
traitement côté serveur. Ici, il s'agit seulement du style de la page.

## Fichiers
| Fichier | Responsabilité |
|---|---|
| `style.css` | Mise en page et apparence de la calculatrice : centrage de la page, écran d'affichage, grille de boutons à 4 colonnes, couleurs des boutons (orange pour les opérateurs) et effets au survol et au clic. |

## Dépendances et hypothèses
- Flask sert automatiquement ce dossier à l'URL `/static/`.
- Les sélecteurs (`.calculator`, `#display`, `.buttons`, `.btn`, `.operator`)
  correspondent aux classes et identifiants de `templates/index.html`. Si on
  les renomme dans le HTML, il faut aussi les changer ici.
