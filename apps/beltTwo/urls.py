from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^create$', views.create, name='create'),
    url(r'^user/(?P<id>\d+)$', views.user, name='user'),
    url(r'^fav/(?P<id>\d+)$', views.fav, name='fav'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]
