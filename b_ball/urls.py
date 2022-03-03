from django.urls import path
from . import views



urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('register_player/', views.register_player,name='register player'),
    path('too_many/', views.too_many,name='Too Many Players'),
    path('edit_roster/', views.edit_roster, name = 'edit_roster'),
    path('delete/<id>', views.delete, name = 'delete'),
    ]
