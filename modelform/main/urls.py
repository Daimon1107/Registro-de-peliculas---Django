
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='add_movie'),
    path('movie/', views.inicio, name='movie'),
    path('base/', views.base, name='base'),
]


