from django.db import models
from django import forms


from .models import Personalise


class PersonalisationForm(forms.ModelForm):
    class Meta:
        model = Personalise
        fields = [
            'background',
            'text_color',
            'text_content',
            'extra_requirements',
        ]
