
from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('application/', views.application, name='application'),
    path('logout/', views.logout, name='logout'),
    path('branch/', views.branches, name='branches'),

]
