from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250,blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='defualt-user.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Genre(models.Model):
    # Field for the genre name
    name = models.CharField(max_length=255)
    genre_img = models.ImageField(upload_to='genre_img', null=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post_title = models.CharField(max_length=30,default=None, editable=True) #by default null is false
    text_body = models.TextField(max_length=2000,null=True) 
    image = models.ImageField(upload_to='post_images', null=True,blank=True, default='None')
    genres = models.ManyToManyField(Genre)
    no_likes = models.IntegerField(default=0)
    no_comments = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.post_title

class Like(models.Model):
    post_id = models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,editable=None, related_name='comments') # related name specifies reverse relationship to user 
    post = models.ForeignKey(Post, on_delete=models.CASCADE,editable=None, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-created_at']

        def __str__(self):
            return self.text

class Followers(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
