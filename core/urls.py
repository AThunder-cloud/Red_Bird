from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('create-post/',views.create_post,name='create-post'),
    path('delete', views.delete_post,name='delete'),
]
