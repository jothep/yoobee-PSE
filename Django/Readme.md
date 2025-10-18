Django Project Quick Guide (Week12)

A minimal guide to setting up a Django app with templates and CSS.

Project: Week12

App: activity

1. Register App in settings.py

Add your app to INSTALLED_APPS in Week12/settings.py:

INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'activity',
]


2. Include App URLs in Project urls.py

In Week12/urls.py, point a path to your app's urls.py file.

# Week12/urls.py
urlpatterns = [
    # ...
    path('', include('activity.urls')),
]

3. Use render in views.py

In activity/views.py, use render() to load an HTML template.

# activity/views.py
def welcome(request, name):
    return render(request, 'activity/welcome.html', {'name': name})

4. Create Correct Folder Structure

For Django to find your files, the paths must be exact:

HTML Template: activity/templates/activity/welcome.html

CSS File: activity/static/activity/style.css

5. Link CSS in HTML

In welcome.html, load static files and link your stylesheet:

{% load static %}
<link rel="stylesheet" href="{% static 'activity/style.css' %}">

6. Run Server

python manage.py runserver
