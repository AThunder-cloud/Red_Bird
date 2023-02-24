from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin, name='signin'),
    path('logout/',views.signout, name='signout'),
    path('create-post/',views.create_post,name='create-post'),
    path('delete/<int:item_id>/',views.delete,name='delete'),

    path('profile/<int:pk>/', views.user_profile, name='profile'),
]
