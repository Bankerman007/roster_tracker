from django.urls import path
from . import views



urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('register_player/', views.register_player,name='register player'),
    path('too_many/', views.too_many,name='Too Many Players'),
    path('edit_roster/<id>', views.edit_roster, name = 'edit_roster'),
    path('edit_full_roster/<id>', views.edit_full_roster, name = 'edit_full_roster'),
    path('delete/<id>', views.delete, name = 'delete'),
    path('delete_full_list/<id>', views.delete_full_list, name = 'delete_full_list'),
    path('sms_to_all/', views.sms_to_all, name = 'sms_messages'),
    path('sms_to_registered/', views.sms_to_registered, name = 'sms_registered'),
    path('send_texts/', views.send_texts, name = 'send_texts' ),
    path('on_off/', views.on_off, name = 'on_off'),
    path('change_status/<id>', views.change_status, name = 'change status'),
    path('turn_status_off/<id>', views.turn_status_off, name = 'turn status off'),
    path('crud_base/', views.crud_base, name = 'CRUD Base'),
    path('register_full_list/', views.register_full_list, name = 'Register full list'),
            
    ]
