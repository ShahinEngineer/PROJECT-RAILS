from django import forms
from .models import Pastes

class PastesFrom(forms.ModelForm):
    class Meta:
        model=Pastes
        fields=["text","title"]
        