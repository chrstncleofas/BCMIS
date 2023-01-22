# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add', views.add, name='add'),
    path('view_list', views.view_list, name='view_list'),
    path('<int:id>', views.view_info, name='view_info'),
    path('signout', views.signout, name='signout'),
]