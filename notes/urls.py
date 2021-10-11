from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from notes import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('logout', views.hlogout, name='notes'),
    path('save', views.save, name='notes'),
    path('delete/<int:inn>', views.dell, name='notes'),
    path('read/<int:innn>', views.read, name='notes'),


]
