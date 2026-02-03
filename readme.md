python 3.14.2
pip install djangorestframework
pip install django-cors-headers
pip install djangorestframework-simplejwt

cd back/pyback
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

routes:
	GET     /api/equipements                          -> liste de tous les équipements (auth)
	GET     /api/chevalier/equipements               -> équipements du chevalier connecté
	POST    /api/chevalier/equipements/equiper       -> équipe un équipement au chevalier
	DELETE  /api/chevalier/equipements/retirer       -> retire un équipement du chevalier

	POST    /api/login                               -> login (JWT, cookies httpOnly)
	POST    /api/login/refresh                       -> refresh du token
	POST    /api/register                            -> créer un user + chevalier et connecter

	GET     /api/admin/chevaliers                    -> liste des chevaliers (admin)
	POST    /api/admin/chevaliers                    -> créer un chevalier (admin)
	DELETE  /api/admin/chevaliers/delete/<id>        -> supprimer un chevalier (admin)
	POST    /api/admin/create/equipements            -> créer un équipement (admin)
	DELETE  /api/admin/delete/equipements/<id>       -> supprimer un équipement (admin)

comment creer un super user:
python manage.py createsuperuser
met tes infos
python manage.py runserver
tu vas sur postman et tu mets fais un get de /admin avec un basic auth avec ton username et password

tu recup le csrf token dans les cookies
et tu mets dans le header:
X-CSRFToken: <ton csrf token>
et la tu peux faire les requetes en superadmin