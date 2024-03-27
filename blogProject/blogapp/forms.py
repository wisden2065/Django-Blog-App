

from django import forms


# creating Login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=24)
    password = forms.CharField( max_length=20)
    # email = forms.EmailField(max_length=30)


# creating post form
class createPostForm(forms.Form):
    title = forms.CharField(max_length=20)
    slug = forms.SlugField(max_length=20)
    body = forms.CharField(max_length=56)
