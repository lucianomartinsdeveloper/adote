from django import forms

from divulgar.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['status', 'usuario']
