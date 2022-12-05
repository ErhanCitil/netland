from django import forms
from .models import Series

class SerieForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['title', 'rating', 'has_won_awards', 'country', 'summary', 'seasons', 'spoken_in_language']
        wdigets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_won_awards': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'seasons': forms.NumberInput(attrs={'class': 'form-control'}),
            'spoken_in_language': forms.TextInput(attrs={'class': 'form-control'}),
        }