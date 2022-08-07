"""roster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('b_ball.urls')),
    path('base/', include('b_ball.urls')),
    path('register_player/', include('b_ball.urls')),
    path('too_many/', include('b_ball.urls')),
    path('edit_roster/', include('b_ball.urls')),
    path('delete/', include('b_ball.urls')),
    path('send_texts/', include('b_ball.urls')),
    path('sms_to_all/', include('b_ball.urls')),
    path('sms_to_registered/', include('b_ball.urls')),
    path('on_off/', include('b_ball.urls')),
    path('change_status/', include('b_ball.urls')),
    path('turn_status_off/', include('b_ball.urls')),

]
