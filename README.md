# comingSoon
comingSoon

1 page 
4 sections 
coming soon page 
 django app
 
Custom modules:

Backgrounds:
customize featured image, menu and contact background image.

Coming soon date:
Create multiple coming soon date

Email:
collect names and emails 

Main image: 
Change sections background images 

///////////////////////////////////////////////////////////////
                  Installation 
///////////////////////////////////////////////////////////////

1)
git clone https://github.com/QbasicFan/comingSoon

2)
pip install django-widget-tweaks


3)
pip install django-tracking2
(https://github.com/bruth/django-tracking2)

4)
setting (root app)
INSTALLED_APPS = (

    "widget_tweaks",
    
    "comingSoon",
    
    "tracking",
    
    ....

5)
MIDDLEWARE_CLASSES = (
    ...
    
    'tracking.middleware.VisitorTrackingMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    ...
    
)

    
6)
    url("^$", include("comingSoon.urls")),
    
    url(r'^tracking/', include('tracking.urls')),

7) 
python manage.py makemigrations comingSoon

python manage.py migrate comingSoon

8) 
add extra/w3.css in static css folder

