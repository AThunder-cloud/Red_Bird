from django.forms import ModelForm, widgets
from .models import *
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']
        

class GenreForm(forms.Form):
    # Field for selecting one or more genres from a predefined list
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

