from django import forms
from .models import Pastes

class PastesFrom(forms.ModelForm):
    title=forms.CharField(max_length=200)
    text=forms.TextInput()
    date=forms.DateTimeField()
    class Meta:
        model=Pastes
        fields=["text","title","date"]

