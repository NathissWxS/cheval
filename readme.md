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
- GET     /api/chevalier/equipements  Liste des équipements d'un chevalier (auth requis)
- POST    /api/login                  Authentification (JWT via cookies)
- POST    /api/login/refresh          Rafraîchissement du token (JWT via cookies)
- POST    /api/register               Enregistrement d'un nouvel utilisateur
- POST    /api/chevalier/equipements  Ajout d'un équipement à un chevalier (auth requis)
- DELETE  /api/chevalier/equipements/retirer Retrait d'un équipement d'un chevalier (auth requis)

comment creer un super user:
python manage.py createsuperuser
met tes infos gros naze
/admin/ sur le navigateur pour acceder a l'admin django
se c