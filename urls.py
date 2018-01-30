from django.conf.urls import  url

from . import views

handler404 = "mezzanine.core.views.page_not_found"


urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    url(r'^', views.index, name='index'),
            ]
