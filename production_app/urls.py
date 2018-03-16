from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.production_list, name='production_list'),
]