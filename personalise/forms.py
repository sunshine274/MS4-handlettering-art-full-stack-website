from django.db import models
from django import forms


from .models import Product


class PersonalisationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'background',
            'text_color',
            'text_content',
            'extra_requirements',
        ]
