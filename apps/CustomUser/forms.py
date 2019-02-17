from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import re
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

class UserCreationForm(UserCreationForm):


    class Meta:
        model = get_user_model()
        fields = ('username','phoneno', 'fullname', 'address', 'category')
    error_messages = {
        'duplicate_username': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }    

    username = forms.EmailField(label='Email', max_length=250)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        print()
        print(user.username)
        user.email = user.username
        user.save()
        return user