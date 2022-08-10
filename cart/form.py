from .models import cartlist
from django import forms


class updatstatusform(forms.ModelForm):
    class Meta:
        model = cartlist
        fields = ['status','remarks']
