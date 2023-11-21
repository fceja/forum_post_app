from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


# override UserCreationForm
class RegisterForm(UserCreationForm):
    # not added by default
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
