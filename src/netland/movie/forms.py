from django import forms

from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = [
            "title",
            "length_in_minutes",
            "released_at",
            "country_of_origin",
            "summary",
            "youtube_trailer_id",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "length_in_minutes": forms.TextInput(attrs={"class": "form-control"}),
            "released_at": forms.TextInput(attrs={"class": "form-control"}),
            "country_of_origin": forms.TextInput(attrs={"class": "form-control"}),
            "summary": forms.Textarea(attrs={"class": "form-control"}),
            "youtube_trailer_id": forms.TextInput(attrs={"class": "form-control"}),
        }
