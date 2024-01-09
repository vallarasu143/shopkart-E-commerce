from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import userimage,User

class customUserform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'off'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'off'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class userimage_form(forms.ModelForm):
    class Meta:
        model=userimage
        fields=['userpic']
