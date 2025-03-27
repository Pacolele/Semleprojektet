from django import forms
from .models import Semlor


class SemlorForm(forms.ModelForm):
    class Meta:
        model = Semlor
        fields = "__all__"
