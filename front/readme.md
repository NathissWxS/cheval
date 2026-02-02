# TP Armurerie du château
## Formateur : Dufrène Valérian
“Déclaration d’activité enregistrée sous le numéro **32800232680** auprès du préfet de région HAUTS-DE-FRANCE”









Durée estimée : **6 à 7 heures**

Dans ce TP, vous devrez utiliser les connaissances acquises sur les points suivants : 

- créer une application structurée
- gérer des routes publiques et protégées
- utiliser des templates avec héritage (si pertinent sur le choix des technos)
- manipuler des formulaires POST
- implémenter un CRUD
- gérer une session utilisateur (authentification)
 - restreindre l’accès à certaines zones
- exposer une API REST simple
- versionner votre application, avec GIT


Le tout dans une application cohérente et immersive (et surtout, **fonctionnelle !**).

## Contexte
Bienvenue au château de Valdrak.

Chaque jour, des chevaliers se présentent à l’armurerie pour s’équiper avant d’aller combattre sur le champ de bataille… ou se détendre à la taverne.

Mais attention :

le gardien du château n’**autorise l’accès** qu’aux chevaliers qu’il reconnaît


un chevalier ne **peut pas aller au combat** sans équipement


l’armurerie contient un **stock limité** d’équipements

Zones accessibles dans l’application :

### L’Armurerie 
- Permet au chevalier de s’équiper
- Gestion des équipements
- Accès réservé aux chevaliers connectés


### Le Champ de bataille
- Accessible uniquement si le chevalier est :
- connecté
- équipé d’au moins une arme


### La Taverne
- Accessible à tous
- Zone de détente, sans restriction

## Contraintes techniques
Libre choix techno front

Libre choix techno back

API REST

SQL

Utilisation des sessions

Architecture claire


## Partie 1 — Installation et entrée du château
### Objectif

Permettre au gardien de reconnaître les chevaliers.

### Travail demandé
Créer la structure suivante (exemple en python, adaptez à votre choix de techno) :
``` sh
project/
│
├── app.py
├── models.py
├── templates/
│   ├── base.html
│   ├── login.html
│   └── home.html
├── static/
└── database.db
```

Créer une page /login

### Lors de la connexion :
stocker l’identité du chevalier en session

afficher un message du gardien : “Le gardien vous reconnaît, chevalier. Vous pouvez entrer.”

## Partie 2 — Navigation dans le château
### Objectif
Mettre en place les différentes zones.
### Travail demandé
Créer les routes :
```
/ → cour du château
/armurerie
/champ-de-bataille
/taverne
```



Créer un base.html avec :

- un menu de navigation
- affichage conditionnel selon la session









## Partie 3 — Base de données : équipements
### Objectif
Créer l’inventaire de l’armurerie.
### Travail demandé
Créer un modèle Equipement avec :
```
id
nom
type (arme / défense)
disponible (booléen)
```



### Équipements disponibles par défaut :
- 🗡️ épée
- 🛡️ bouclier
- 🧥 cotte de maille
- 🪖 casque en fer


Afficher la liste des équipements dans l’armurerie.






## Partie 4 — S’équiper à l’armurerie
### Objectif
Permettre au chevalier de s’équiper.
### Travail demandé
Créer un formulaire permettant de :
- choisir un équipement
- l’assigner au chevalier connecté
- Mettre à jour la base de données
- Empêcher :
- l’équipement multiple du même objet
- l’accès à l’armurerie sans session
- Ajouter des messages flash :
- succès : “Vous êtes désormais équipé d’une épée”
- erreur : “Vous devez vous équiper d’au moins une pièce”










## Partie 5 — Contrôles d’accès et règles du château
### Objectif
Appliquer les règles de sécurité.
### Règles à implémenter
- ❌ Armurerie inaccessible sans session
- ❌ Champ de bataille inaccessible :
  - sans être connecté
  - sans équipement
- ✅ Taverne accessible à tous


### Travail demandé
- utiliser les sessions
- conditionner l’accès à une vérification chevalier_requis
- afficher des messages adaptés du gardien comme : “Retournez à l’armurerie avant  d’aller au combat !”








## Partie 6 — API royale
### Objectif
Exposer les données du royaume.
### Routes API à créer
```
GET /api/equipements
GET /api/chevaliers/<id>/equipements
```


Format JSON attendu :
```
{
  "chevalier": "Arthur",
  "equipements": ["épée", "casque en fer"]
}
```


Respecter :
- le format JSON
- les codes HTTP





## Bonus (pour les plus braves)
- Limiter les emplacements d’équipement (max 3)
- Ajouter une page “inventaire du chevalier”
- Ajouter une déconnexion, avec le message suivant : “Le gardien vous salue, chevalier.”
- Ajouter une suppression d’équipement

Un bon chevalier prépare son équipement. Un bon développeur prépare son architecture.

