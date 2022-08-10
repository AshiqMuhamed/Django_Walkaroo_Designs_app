from .models import ratingreview
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ratingreview
        fields = ['rating','review']
