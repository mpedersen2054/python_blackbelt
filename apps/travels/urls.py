from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^destination/(?P<id>\d+)$', views.show_travel, name='show_travel'),
    url(r'^add$', views.add_travel, name='add_travel'),
    url(r'^create$', views.create_travel, name='create_travel'),
    url(r'^$', views.index, name='index'),
]
