from django.forms import ModelForm
from app1.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class regisform(ModelForm):
    class Meta:
        model=jana
        fields='__all__'
class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')