python 3.14.2
pip install djangorestframework
pip install django-cors-headers
pip install djangorestframework-simplejwt

cd back/pyback
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

routes:
- GET     /api/equipements/           Liste des équipements (auth requis)
- POST    /api/login                  Authentification (JWT via cookies)
- POST    /api/login/refresh          Rafraîchissement du token (JWT via cookies)
- POST    /api/equipements/           Création d'un équipement (auth requis)
- POST    /api/register               Enregistrement d'un nouvel utilisateur