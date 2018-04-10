from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^track/$',views.index,name='index'),

]
