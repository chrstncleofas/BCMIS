# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add/', views.add, name='add'),
    path('view_list', views.view_list, name='view_list'),
    path('signout', views.signout, name='signout'),
    path('<int:id>/view_info/', views.view_info, name='view_info'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
]