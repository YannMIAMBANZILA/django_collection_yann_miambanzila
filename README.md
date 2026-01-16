# Django — Collection de voitures de luxe

Description
------------
Projet Django pour gérer une collection de voitures de luxe : catalogage, affichage, filtrage et export des données. Idéal pour apprendre Django en construisant une application CRUD simple autour d'un modèle Car.

Fonctionnalités principales
---------------------------
- Gestion des voitures (ajout, modification, suppression, consultation).
- Champs typiques : marque, modèle, année, prix, couleur, description, images.
- Filtrage et recherche par marque/modèle/année/price-range.
- Export/import des données (dumpdata / loaddata).
- Interface d'administration Django pour gestion rapide.

Prérequis
---------
- Python 3.8+
- pip
- virtualenv (recommandé)
- SQLite (par défaut) ou une autre base (Postgres, MySQL)

Installation rapide
-------------------
1. Créer et activer un environnement virtuel :
   python -m venv venv
   venv\Scripts\activate (Windows) ou source venv/bin/activate (Unix)

2. Installer les dépendances :
   pip install -r requirements.txt

3. Appliquer les migrations :
   python manage.py migrate

4. Créer un superutilisateur (pour l'admin) :
   python manage.py createsuperuser

5. Lancer le serveur de développement :
   python manage.py runserver

Export / import des données
---------------------------
- Exporter l'application `carcollect` en JSON (exemple fourni) :
  python manage.py dumpdata carcollect --indent 2 > export_oracle_data.json

- Importer des données :
  python manage.py loaddata export_oracle_data.json

Structure du projet (résumé)
----------------------------
- carcollect/            -> application principale (models, views, templates, urls)
- project settings/      -> configuration Django
- templates/             -> vues côté client
- static/                -> assets (CSS, JS, images)
- requirements.txt       -> dépendances (à créer/maintenir)

Modèles attendus (exemple)
--------------------------
- Car:
  - brand (CharField)
  - model (CharField)
  - year (IntegerField)
  - price (DecimalField)
  - color (CharField)
  - description (TextField)
  - image (ImageField, optionnel)

Points d'amélioration possibles
-------------------------------
- Authentification et profils utilisateurs.
- API REST (Django REST Framework) pour consultation externe.
- Upload d'images via S3 ou service externe.
- Tests automatisés et CI.

Contribution
------------
Contributions bienvenues : ouvrir une issue pour discuter des fonctionnalités ou proposer une PR.

Licence
-------
Précisez la licence choisie (ex: MIT) dans un fichier LICENSE si nécessaire.