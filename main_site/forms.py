from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Post


# override UserCreationForm
class RegisterForm(UserCreationForm):
    # not added by default
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]

    # added since cause issue when posting
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and email.endswith("@email.com"):
            raise ValidationError(
                "Registration with '@email.com' addresses is not allowed."
            )
        return email


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
