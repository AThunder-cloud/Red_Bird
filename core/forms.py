from django.forms import ModelForm, widgets
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
# from cripsy_forms.layout import Layout, Row, Submit, Column

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'text_body', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create'))
        self.helper.layout = Layout(
            Row(
                Column('post_title', css_class='form-group col-md-6 mb-5 mx-auto'),
                Column('text_body', css_class='form-group col-md-6 mb-5 mx-auto'),
                css_class = 'form-row'
            ),
            'image'
        )
        self.helper.form_method ='post'
        self.helper.form_class = 'form'
        self.helper.label_class = 'form-label'
        self.helper.field_class = 'form-control'
        

class GenreForm(forms.Form):
    # Field for selecting one or more genres from a predefined list
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

