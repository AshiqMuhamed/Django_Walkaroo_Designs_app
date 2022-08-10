from django.contrib.auth.models import User, auth
from django import forms


class resetpasswordform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']