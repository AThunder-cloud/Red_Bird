from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin, name='signin'),
    path('logout/',views.signout, name='signout'),
    path('create-post/',views.create_post,name='create-post'),
    path('delete/<int:item_id>/',views.delete,name='delete'),
    path('like-post/', views.like_post, name='like-post'),
    path('profile/<int:pk>/', views.user_profile, name='profile'),
    path('postpage/<int:post_id>/', views.post_page,name='postpage'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:item_id>/',views.delete_comment,name='delete_comment'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('follow-unfollow/', views.follow, name='follow_unfollow'),

]
