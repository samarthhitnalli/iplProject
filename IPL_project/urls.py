"""
URL configuration for IPL_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ipl_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_player/', views.add_player, name='add_player'),
    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('add_stadium/', views.add_stadium, name='add_stadium'),
    path('list_players/', views.list_players, name='list_players'),
    path('list_schedules/', views.list_schedules, name='list_schedules'),
    path('list_stadiums/', views.list_stadiums, name='list_stadiums'),
    path('add_team/', views.add_team, name='add_team'),
    path('team_list/', views.team_list, name='team_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)