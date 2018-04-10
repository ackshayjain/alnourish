from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^track/$',views.index,name='index'),
    url(r'^track/new/$',views.new_culture,name='new'),
    url(r'^track/test/$',views.testc,name='testc'),
    url(r'^track/delete/(?P<name>\w+)/$',views.delete_culture,name='delete'),

]
