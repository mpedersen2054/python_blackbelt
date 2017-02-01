from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^register$', views.register, name='register'),
    # url(r'^add$', views.add_travel, name='add_travel'),
    url(r'^$', views.index, name='index'),
]
