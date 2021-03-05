**So let’s start from the very beginning. Install Django and DRF using terminal**
  pip install django
  pip install djangorestframework
**Create a new Django project on terminal using terminal**
  django-admin.py startproject projectname 
 **Start a new app. I will call my app auth using terminal**
 django-admin.py startapp appname 
 ** inside the settings.py add rest_framework inside INSTALLED_APPS at the end **
 **Return to the root project root (the folder where the manage.py script is), and migrate the database:**
  python manage.py migrate
