from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250,blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='defult-profile.png')
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
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.post_title



