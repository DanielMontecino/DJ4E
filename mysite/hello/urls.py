from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.counter, name='index'),
    path('owner', views.owner, name='owner'),
]
