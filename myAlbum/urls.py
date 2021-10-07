from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^vitalisAlbum/$', views.homepage)
]