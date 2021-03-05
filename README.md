**So let’s start from the very beginning. Install Django and DRF using terminal** <br>
  pip install django <br>
  pip install djangorestframework <br>
**Create a new Django project on terminal using terminal** <br>
  django-admin.py startproject projectname  <br>
 **Start a new app. I will call my app auth using terminal** <br>
 django-admin.py startapp appname  <br>
 ** inside the settings.py add rest_framework inside INSTALLED_APPS at the end ** <br>
 **Return to the root project root (the folder where the manage.py script is), and migrate the database:** <br>
  python manage.py migrate<br>
  
  ** unit test and integration test related to the user login and autheticaton present in accounts\test.py
**
