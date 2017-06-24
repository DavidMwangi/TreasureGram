from django.conf.urls import  url
from . import views



urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
]

""""
        Second url looks for a number and captures that value and
        sends it to the detail view.

        The current index url does not look for any path meaning 
        will just match localhost

        [0-9]+ will match any number
        () captures the value which will then be passed as a parameter
        to the detail view. --> localhost/10


"""