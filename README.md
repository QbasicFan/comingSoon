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
setting (root app)
INSTALLED_APPS = (
    "widget_tweaks",
    "comingSoon",
    ....
4)
url("^$", include("comingSoon.urls")),

5) 
python manage.py makemigrations comingSoon
python manage.py migrate comingSoon



