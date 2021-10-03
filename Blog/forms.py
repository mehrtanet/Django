from Blog.models import Post
from django.forms import ModelForm, fields
from django.contrib.auth import models
from .models import Post

class PostForm(ModelForm) :
    class Meta:
        model = Post
        fields = '__all__'

