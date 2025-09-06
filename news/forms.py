from django import forms

from .models import News


class CommentForm(forms.Form):
    text = forms.CharField(max_length=500, label="Izoh", widget=forms.TextInput(
        attrs={
            "style": "width: 100%; border-radius: 20px; padding: 10px; margin: 10px;",
            "placeholder": "Izoh matni..."
        }
    ))
