python 3.14.2
pip install djangorestframework
pip install django-cors-headers
pip install djangorestframework-simplejwt

cd back/pyback
python manage.py makemigrations
python manage.py migrate
python manage.py runserver